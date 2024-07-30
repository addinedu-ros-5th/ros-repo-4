import time
import math
import rclpy
import subprocess
from enum import Enum
from rclpy.node import Node
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import PoseWithCovarianceStamped, Twist, PoseStamped
from minibot_interfaces.msg import GoalPose 
from std_msgs.msg import Header, String
# from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Path


class RobotState(Enum):
    STOP = 1
    MOVING = 2
    ADJUSTING = 3
    OBSTACLE = 4
    
class RobotDrive(Node):
    def __init__(self):
        super().__init__('robot_drive')
        self.nav = BasicNavigator()
        
        self.state = RobotState.STOP
        self.current_pose = None
        self.goal_pose = None
        self.saved_path = None
        self.obstacle = None
        
        # Publisher
        self.initial_pose_publisher = self.create_publisher(PoseWithCovarianceStamped, '/initialpose', 10)
        self.state_publisher = self.create_publisher(String, 'state_topic', 10)
        self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # Subscriber
        self.amclPose_subscription = self.create_subscription(PoseWithCovarianceStamped, 'amcl_pose', self.amclPose_callback, 10)
        self.obstacle_subscriber = self.create_subscription(String, 'obstacle_topic', self.obstacle_callback, 10)
        self.goal_subscription = self.create_subscription(GoalPose, 'target_pose', self.goal_callback, 10)
        self.path_subscription = self.create_subscription(Path, 'planned_path', self.path_callback, 10)
        # self.laser_subscription = self.create_subscription(LaserScan, '/scan', self.laser_callback, 10)
        
        self.publish_initial_pose()
        
        self.nav.waitUntilNav2Active()
        self.publish_state()

        time.sleep(2)

    def publish_initial_pose(self):
            pose_msg = PoseWithCovarianceStamped()
            pose_msg.header = Header()
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

    # 현재 위치를 구독하는 토픽(nav2 map:=mfc.yaml 명령어에서 발행 중인 토픽)
    def amclPose_callback(self, msg):
        self.current_pose = msg.pose.pose
    
    # 목표 위치를 구독하고, 변수로 지정해주는 메서드
    def goal_callback(self, msg):
        self.goal_pose = (
            msg.position_x,
            msg.position_y,
            msg.orientation_z,
            msg.orientation_w
        )

    # 라이다로 장애물 감지 시 사용
    # def laser_callback(self, msg):
    #     min_distance = min(msg.ranges)
    #     if min_distance < 0.2:
    #         self.obstacle_detected = True
    #         self.nav.cancelTask()
    #         self.get_logger().info("Obstacle detected! Stopping the robot.")
    #     else:
    #         self.obstacle_detected = False

    def path_callback(self, msg):
        self.saved_path = msg.poses
        self.nav.followWaypoints(self.saved_path)
        self.set_state(RobotState.MOVING)
        self.publish_state()

        # 경로 완료까지 대기
        while not self.nav.isTaskComplete():
            feedback = self.nav.getFeedback()
            if feedback:
                current_waypoint_index = feedback.current_waypoint
                if current_waypoint_index < len(self.saved_path):
                    current_pose = self.saved_path[current_waypoint_index].pose.position
                    remaining_distance = math.hypot(
                        self.saved_path[-1].pose.position.x - current_pose.x,
                        self.saved_path[-1].pose.position.y - current_pose.y
                    )
                    self.get_logger().info(f"Distance remaining: {remaining_distance:.2f} meters")
                    
                    if remaining_distance <= 0.02:
                        self.nav.cancelTask()
                        self.state = RobotState.ADJUSTING
                        self.publish_state()
                        self.reach_goal_orientation()
                        
                        break
                    
            if self.obstacle:
                self.get_logger().info("Stopped due to obstacle")
                return

        # 최종 결과 확인
        result = self.nav.getResult()
        if result == TaskResult.SUCCEEDED:
            self.get_logger().info("Reached the destination successfully!")
        else:
            self.get_logger().info("Failed to reach the destination.")
                
        # AI 서버와 사람 인식 시 발행받는 토픽 / 이동중 장애물 발견 시 속도=0, 장애물 사라지면 최근 위치로 재이동
    def obstacle_callback(self, msg):
        self.obstacle = msg.data
        if self.obstacle == "obstacle": 
            self.nav.cancelTask() 
            self.stop_robot()
            self.get_logger().info("Obstacle detected! Stopping the robot.")
        else: 
            self.get_logger().info('Obstacle cleared! Resuming movement.')
            if self.saved_path:
                self.nav.followWaypoints(self.saved_path)

    def stop_robot(self):
        stop_msg = Twist()
        stop_msg.linear.x = 0.0
        stop_msg.linear.y = 0.0
        stop_msg.linear.z = 0.0
        stop_msg.angular.x = 0.0
        stop_msg.angular.y = 0.0
        stop_msg.angular.z = 0.0
        self.cmd_vel_publisher.publish(stop_msg)

    def reach_goal_orientation(self):
        self.get_logger().info('Adjusting to final goal orientation.')
        
        current_yaw = self.calculate_current_yaw(self.current_pose.orientation)
        goal_yaw = self.calculate_goal_yaw(self.goal_pose[2], self.goal_pose[3])
        yaw_diff = self.normalize_angle(goal_yaw - current_yaw)

        twist = Twist()

        while abs(yaw_diff) > 0.01:
            current_yaw = self.calculate_current_yaw(self.current_pose.orientation)
            yaw_diff = self.normalize_angle(goal_yaw - current_yaw)
            
            twist.angular.z = 0.1 * yaw_diff
            self.cmd_vel_publisher.publish(twist)
            rclpy.spin_once(self, timeout_sec=0.1)
        
        self.stop_robot()
        self.get_logger().info('Reached final orientation.')
        self.set_state(RobotState.STOP)
        self.publish_state()

    def calculate_current_yaw(self, orientation):
        siny_cosp = 2 * (orientation.w * orientation.z + orientation.x * orientation.y)
        cosy_cosp = 1 - 2 * (orientation.y * orientation.y + orientation.z * orientation.z)
        return math.atan2(siny_cosp, cosy_cosp)

    def calculate_goal_yaw(self, orientation_z, orientation_w):
        siny_cosp = 2 * (orientation_w * orientation_z)
        cosy_cosp = 1 - 2 * (orientation_z * orientation_z)
        return math.atan2(siny_cosp, cosy_cosp)

    def normalize_angle(self, angle):
        while angle > math.pi:
            angle -= 2.0 * math.pi
        while angle < -math.pi:
            angle += 2.0 * math.pi
        return angle

    # def reach_goal_orientation(self):

    #     goal_pose = PoseStamped()
    #     goal_pose.header.frame_id = 'map'
    #     goal_pose.header.stamp = self.nav.get_clock().now().to_msg()
    #     goal_pose.pose.orientation.z = self.goal_pose[2]
    #     goal_pose.pose.orientation.w = self.goal_pose[3]
    #     self.nav.goToPose(goal_pose)
        
    #     if self.goal_pose[3] == goal_pose.pose.orientation.w:
    #         self.stop_robot()
    #         self.state = RobotState.STOP
    #         self.publish_state()

    def publish_state(self):
        state_msg = String()
        state_msg.data = f'{self.state}'
        self.state_publisher.publish(state_msg)
            
def main(args=None):
    rclpy.init(args=args)
    robot_drive = RobotDrive()
    rclpy.spin(robot_drive)
    robot_drive.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
