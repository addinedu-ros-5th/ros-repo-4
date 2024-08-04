import rclpy
import math
import time
import threading
from rclpy.node import Node
from nav_msgs.msg import Path
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import PoseWithCovarianceStamped
from rclpy.executors import SingleThreadedExecutor

class PathFollower(Node):
    def __init__(self):
        super().__init__('robot_drive_unique')

        self.subscription = self.create_subscription(Path, 'planned_path_1', self.path_callback, 10)
        self.initial_pose_publisher = self.create_publisher(PoseWithCovarianceStamped, 'initialpose', 10)

        self.nav = BasicNavigator()
        self.nav.waitUntilNav2Active()

        # 초기 위치 퍼블리시
        self.publish_initial_pose()

        # 경로 추종을 비동기적으로 처리하기 위한 스레드
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
        for i, pose in enumerate(poses):
            self.get_logger().info(f"Moving to waypoint {i + 1}/{len(poses)}: ({pose.pose.position.x}, {pose.pose.position.y})")

            # 목표 설정
            self.nav.goToPose(pose)

            # 목표 도달까지 대기
            while not self.nav.isTaskComplete():
                feedback = self.nav.getFeedback()
                if feedback:
                    current_pose = feedback.current_pose.position
                    remaining_distance = math.hypot(
                        pose.pose.position.x - current_pose.x,
                        pose.pose.position.y - current_pose.y
                    )
                    self.get_logger().info(f"Distance remaining to waypoint {i + 1}: {remaining_distance:.2f} meters")
                    if remaining_distance <= 0.05:
                        self.get_logger().info(f"Arrived at waypoint {i + 1}")
                        break

                time.sleep(0.1)  # CPU 사용률 감소를 위해 잠시 대기

            # 최종 결과 확인
            result = self.nav.getResult()
            if result == TaskResult.SUCCEEDED:
                self.get_logger().info(f"Reached waypoint {i + 1} successfully!")
            else:
                self.get_logger().info(f"Failed to reach waypoint {i + 1}: {result}")
                break  # 경로의 나머지 웨이포인트로 이동하지 않고 중단

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


# import rclpy
# import threading
# import math
# from rclpy.node import Node
# from nav_msgs.msg import Path
# from nav2_simple_commander.robot_navigator import BasicNavigator, PoseStamped, TaskResult
# from geometry_msgs.msg import PoseWithCovarianceStamped
# from rclpy.qos import QoSProfile, HistoryPolicy
# from sensor_msgs.msg import LaserScan
# # from behavior_tree import BehaviorTree
# from std_srvs.srv import Trigger
# from std_msgs.msg import Header, String
# import time

# # behavior_tree = BehaviorTree(tick_rate=50)

# class PathFollower(Node):
#     def __init__(self):
#         super().__init__('robot_drive_unique')
        
#         # self.declare_parameter('use_sim_time', False)

#         # self.robot_id = '1'
#         # self.current_robot_id = None
        
        

#         # self.id_subscription = self.create_subscription(String, 'robot_id', self.id_callback, 10)
#         qos_profile = QoSProfile(depth=10, history=HistoryPolicy.KEEP_LAST)
#         self.subscription = self.create_subscription(Path, 'planned_path_1', self.path_callback, qos_profile)
#         self.initial_pose_publisher = self.create_publisher(PoseWithCovarianceStamped, 'initialpose', 10)
        
        
#         self.nav = BasicNavigator()
#         self.nav.waitUntilNav2Active()
        
#         self.publish_initial_pose()        
#         self.path_following_thread = None
        
#         # time.sleep(2)

#     def publish_initial_pose(self):
#         pose_msg = PoseWithCovarianceStamped()
#         # pose_msg.header = Header()
#         pose_msg.header.frame_id = 'map'
#         pose_msg.header.stamp = self.get_clock().now().to_msg()
        
#         pose_msg.pose.pose.position.x = 0.0
#         pose_msg.pose.pose.position.y = 0.0
#         pose_msg.pose.pose.position.z = 0.0
#         pose_msg.pose.pose.orientation.x = 0.0
#         pose_msg.pose.pose.orientation.y = 0.0
#         pose_msg.pose.pose.orientation.z = 0.0
#         pose_msg.pose.pose.orientation.w = 1.0

#         pose_msg.pose.covariance = [0.0] * 36
        
#         self.initial_pose_publisher.publish(pose_msg)
#         self.get_logger().info("Published initial pose")
    
#     # def id_callback(self, msg):
#     #     self.current_robot_id = msg.data
#     #     self.get_logger().info(f"Received Robot ID: {self.current_robot_id}")
    
    
#     def path_callback(self, msg):
        
#         # if self.current_robot_id != self.robot_id:
#         #     return
        
#         self.get_logger().info(f"Received path with {len(msg.poses)} points.")
#         # for i, pose in enumerate(msg.poses):
#         #     self.get_logger().info(f"Waypoint {i}: {pose.pose.position.x}, {pose.pose.position.y}")
#         if self.path_following_thread is not None and self.path_following_thread.is_alive():
#             self.get_logger().info("Interrupting previous path following.")
#             self.nav.cancelTask()
#             self.path_following_thread.join()
            
#         self.path_following_thread = threading.Thread(target=self.follow_path, args=(msg.poses,))
#         self.path_following_thread.start()

#     def follow_path(self, poses):
#         # 비동기적으로 목표 전송
#         send_goal_future = self.nav.followWaypoints(poses)

#         # 결과가 완료될 때까지 기다림
#         rclpy.spin_until_future_complete(self, send_goal_future)

#         while not self.nav.isTaskComplete():
#             feedback = self.nav.getFeedback()
#             if feedback:
#                 current_waypoint_index = feedback.current_waypoint
#                 if current_waypoint_index < len(poses):
#                     current_pose = poses[current_waypoint_index].pose.position
#                     remaining_distance = math.hypot(
#                         poses[-1].pose.position.x - current_pose.x,
#                         poses[-1].pose.position.y - current_pose.y
#                     )
#                     self.get_logger().info(f"Distance remaining: {remaining_distance:.2f} meters")
#                     if remaining_distance <= 0.05:
#                         self.get_logger().info("Arrived at the Target")
#                         break

#             time.sleep(0.1)  # CPU 사용률 감소를 위해 잠시 대기

#         # 최종 결과 확인
#         result = self.nav.getResult()
#         if result == TaskResult.SUCCEEDED:
#             self.get_logger().info("Reached the destination successfully!")
#         else:
#             self.get_logger().info(f"Failed to reach the destination: {result}")

# # --------------------
#         # # 경로 따라가기
#         # self.nav.followWaypoints(msg.poses)

#         # # 경로 완료까지 대기
#         # while not self.nav.isTaskComplete():
#         #     feedback = self.nav.getFeedback()
#         #     if feedback:
#         #         current_waypoint_index = feedback.current_waypoint
#         #         if current_waypoint_index < len(msg.poses):
#         #             current_pose = msg.poses[current_waypoint_index].pose.position
#         #             remaining_distance = math.hypot(
#         #                 msg.poses[-1].pose.position.x - current_pose.x,
#         #                 msg.poses[-1].pose.position.y - current_pose.y
#         #             )
#         #             self.get_logger().info(f"Distance remaining: {remaining_distance:.2f} meters")
#         #             if remaining_distance <= 0.05:
#         #                 self.get_logger().info("Arrived at the Target")
#         #                 break

#         # # 최종 결과 확인
#         # result = self.nav.getResult()
#         # if result == TaskResult.SUCCEEDED:
#         #     self.get_logger().info("Reached the destination successfully!")
#         # else:
#         #     self.get_logger().info("Failed to reach the destination.")
        
# def main(args=None):
#     rclpy.init(args=args)
#     node = PathFollower()
#     try:
#         rclpy.spin(node)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         if node.path_following_thread is not None:
#             node.nav.cancelTask()
#             node.path_following_thread.join()
#         node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()