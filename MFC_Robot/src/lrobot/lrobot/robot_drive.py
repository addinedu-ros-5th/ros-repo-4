import rclpy
import math
import time
import threading
import math
import time
import threading
from enum import Enum
from rclpy.node import Node
from nav_msgs.msg import Path
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from rclpy.executors import SingleThreadedExecutor
from minibot_interfaces.msg import GoalPose
from std_msgs.msg import String
# class RobotState(Enum):
#     STOP = 1
#     MOVING = 2
#     ADJUSTING = 3
#     OBSTACLE = 4

class PathFollower(Node):
    def __init__(self):
        super().__init__('robot_drive_unique')

        self.subscription = self.create_subscription(Path, 'robo_1/planned_path', self.path_callback, 10)
        self.goal_subscription = self.create_subscription(GoalPose, 'target_pose', self.goal_callback, 10)
        self.initial_pose_publisher = self.create_publisher(PoseWithCovarianceStamped, 'initialpose', 10)
        self.amcl_subscription = self.create_subscription(PoseWithCovarianceStamped, 'robo_1/amcl_pose', self.amcl_callback, 10)
        self.arrive_goal_publisher = self.create_publisher(String, 'robo_1/adjust_topic', 10)

        self.nav = BasicNavigator()
        self.nav.waitUntilNav2Active()

        # 초기 위치 퍼블리시
        self.publish_initial_pose()

        # 경로 추종을 비동기적으로 처리하기 위한 스레드
        self.current_position = None
        self.current_orientation = None
        self.path_following_thread = None
        
        self.lock = threading.Lock()

    def publish_initial_pose(self):
        pose_msg = PoseWithCovarianceStamped()
        pose_msg.header.frame_id = 'map'
        pose_msg.header.stamp = self.get_clock().now().to_msg()

        pose_msg.pose.pose.position.x = 0.0
        pose_msg.pose.pose.position.y = 0.0
        pose_msg.pose.pose.position.z = 0.0
        pose_msg.pose.pose.orientation.x = 0.0
        pose_msg.pose.pose.orientation.y = 0.0
        pose_msg.pose.pose.orientation.z = 0.0
        pose_msg.pose.pose.orientation.w = 1.0

        pose_msg.pose.covariance = [0.0] * 36

        self.initial_pose_publisher.publish(pose_msg)
        self.get_logger().info("Published initial pose")

    def amcl_callback(self, msg):
        # AMCL 포즈를 사용하여 현재 위치 갱신
        self.current_position = msg.pose.pose.position
        self.current_orientation = msg.pose.pose.orientation

    def goal_callback(self, msg):
        self.goal_pose = (
            msg.position_x,
            msg.position_y,
            msg.orientation_z,
            msg.orientation_w)

    def path_callback(self, msg):
        self.get_logger().info(f"Received path with {len(msg.poses)} points.")

        with self.lock:
            if self.path_following_thread is not None and self.path_following_thread.is_alive():
                self.get_logger().info("Interrupting previous path following.")
                self.nav.cancelTask()
                self.path_following_thread.join()

            # 새로운 스레드에서 경로 추종 시작
            self.path_following_thread = threading.Thread(target=self.follow_path, args=(msg.poses,))
            self.path_following_thread.start()

    def follow_path(self, poses):
        valid_poses = []

        # 유효한 PoseStamped만을 리스트에 추가
        for i, pose in enumerate(poses):
            if isinstance(pose, PoseStamped):
                valid_poses.append(pose)
                self.get_logger().info(f"Waypoint {i + 1}/{len(poses)}: ({pose.pose.position.x}, {pose.pose.position.y})")
            else:
                self.get_logger().error(f"Invalid pose at index {i}, skipping.")

        if not valid_poses:
            self.get_logger().error("No valid waypoints received, aborting path following.")
            return

        # 여러 개의 웨이포인트를 따라 이동
        self.nav.followWaypoints(valid_poses)

        # 목표 도달까지 대기
        while not self.nav.isTaskComplete():
            if self.current_position is not None:
                target_pose = valid_poses[-1].pose.position
                remaining_distance = math.hypot(
                    target_pose.x - self.current_position.x,
                    target_pose.y - self.current_position.y
                )
                self.get_logger().info(
                    # f"Current position: ({self.current_position.x:.2f}, {self.current_position.y:.2f}), "
                    # f"Target position: ({target_pose.x:.2f}, {target_pose.y:.2f}), "
                    f"Distance remaining to final waypoint: {remaining_distance:.2f} meters"
                )

                # 목표에 도달했는지 판단
                if remaining_distance <= 0.1:  # 허용 오차를 설정
                    self.get_logger().info("Arrived at final waypoint within tolerance")
                    break

            time.sleep(0.05)  # CPU 사용률 감소를 위해 잠시 대기

        # 최종 결과 확인
        result = self.nav.getResult()
        if result == TaskResult.SUCCEEDED:
            self.get_logger().info("Successfully followed all waypoints!")
            adjust_msg = String()
            adjust_msg.data = "ADJUSTING"
            self.arrive_goal_publisher.publish(adjust_msg)
        else:
            self.get_logger().info(f"Failed to reach final waypoint: {result}")

def main(args=None):
    rclpy.init(args=args)
    node = PathFollower()
    executor = SingleThreadedExecutor()

    try:
        rclpy.spin(node, executor=executor)
    except KeyboardInterrupt:
        pass
    finally:
        if node.path_following_thread is not None:
            node.nav.cancelTask()
            node.path_following_thread.join()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

