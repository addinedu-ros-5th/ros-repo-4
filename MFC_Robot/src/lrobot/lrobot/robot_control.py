import os
import time
import math
import rclpy
from enum import Enum
from rclpy.node import Node
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from geometry_msgs.msg import PoseStamped, Twist
from std_msgs.msg import String
from rclpy.qos import QoSProfile, ReliabilityPolicy
# from lrobot.astar_planner import AStarPlanner, ObstacleAvoider, load_map
# from lrobot.robot_pose import RobotPose
# from lrobot.sensor_data_collector import SensorDataCollector
# from geometry_msgs.msg import Quaternion
# from ament_index_python.packages import get_package_share_directory


pose_dict = {
    "R_A1": [-0.034, 1.56, 0.99, 1.0], "R_A2": [-0.034, 1.56, 0.99, 1.0], "R_A3": [-0.034, 1.56, 0.99, 1.0],
    "R_B1": [0.566, 1.56, 0.99, 1.0], "R_B2": [0.566, 1.56, 0.99, 1.0], "R_B3": [0.566, 1.56, 0.99, 1.0],
    "R_C1": [1.166, 1.56, 0.99, 1.0], "R_C2": [1.166, 1.56, 0.99, 1.0], "R_C3": [1.166, 1.56, 0.99, 1.0],
    "R_D1": [-0.334, 0.96, 0.99, 1.0], "R_D2": [-0.334, 0.96, 0.99, 1.0], "R_D3": [-0.334, 0.96, 0.99, 1.0],
    "R_E1": [0.566, 0.96, 0.99, 1.0], "R_E2": [0.566, 0.96, 0.99, 1.0], "R_E3": [0.566, 0.96, 0.99, 1.0],
    "R_F1": [1.166, 0.96, 0.99, 1.0], "R_F2": [1.166, 0.96, 0.99, 1.0], "R_F3": [1.166, 0.96, 0.99, 1.0],
    "I1": [0.116, -1.11, 0.0, 1.0], "I2": [0.416, -1.11, 1.0, 0.0],
    "O1": [0.716, -1.11, 0.0, 1.0], "O2": [0.716, -1.11, 1.0, 0.0],
    "RH1": [0.0, 0.0, 0.0, 1.0], "RH2": [0.0, 0.0, 0.0, 1.0],
    "test": [0.00, 1.5, 0.99, 1.0]
}

# class RobotState(Enum):
#     AtHome = 1
#     ToInbound = 2
#     AtInbound = 3
#     ToRack = 4
#     AtRack = 5
#     ToOutbound = 6
#     AtOutbound = 7
#     ToHome = 8
#     Charging = 9
#     Error = 10
#     Maintaining = 11

class RobotState(Enum):
    STOP = 1
    MOVING = 2
    ADJUSTING = 3
    OBSTACLE = 4

# qos_profile = QoSProfile(
#     reliability=ReliabilityPolicy.RMW_QOS_POLICY_RELIABILITY_RELIABLE,
#     depth=10
# )

class Robot(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.pose_dict = pose_dict
        self.nav = BasicNavigator()
        self.nav.lifecycleStartup()
        self.nav.waitUntilNav2Active()
        
        # 변수, 상태 초기화
        self.state = RobotState.STOP
        self.current_pose = None
        self.current_goal = None
        self.arrive = None
        self.obstacle = None
        
        initial_pose = PoseWithCovarianceStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.pose.pose.position.x = 0.0
        initial_pose.pose.pose.position.y = 0.0
        initial_pose.pose.pose.orientation.w = 1.0
        initial_pose.pose.covariance = [0.0] * 36  # Example covariance

        publisher = self.create_publisher(PoseWithCovarianceStamped, 'initialpose', 10)
        publisher.publish(initial_pose)
        
        # Publisher
        self.result_publisher = self.create_publisher(String, 'result_topic', 10)
        self.state_publisher = self.create_publisher(String, 'state_topic', 10)
        self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # Subscriber
        self.pose_command_subscriber = self.create_subscription(String, 'pose_commands', self.pose_command_callback, 10)
        self.pose_subscriber = self.create_subscription(PoseWithCovarianceStamped, 'amcl_pose', self.amcl_pose_callback, 10)
        self.arrive_pose_subscriber = self.create_subscription(String, 'arrive_pose', self.arrive_topic_callback, 10)
        self.obstacle_subscriber = self.create_subscription(String, 'obstacle_topic', self.obstacle_topic_callback, 10)
        
        self.publish_state()

    def pose_command_callback(self, msg):
        pose_name = msg.data
        if self.state in [RobotState.STOP]:
            self.get_logger().info(f'Received pose command: {pose_name}')
            self.move_to_pose(pose_name)
        else:
            self.get_logger().warn(f'Currently moving. Ignoring new pose command: {pose_name}')

    def arrive_topic_callback(self, msg):
        self.arrive = msg.data

    # AI 서버와 사람 인식 시 발행받는 토픽 / 이동중 장애물 발견 시 속도=0, 장애물 사라지면 최근 위치로 재이동
    def obstacle_topic_callback(self, msg):
        self.obstacle = msg.data
        if self.obstacle == "obstacle" and self.state == RobotState.MOVING:
            self.get_logger().warn('Obstacle detected! Stopping the robot.')
            self.stop_robot()
            self.set_state(RobotState.OBSTACLE)
        elif self.obstacle == "clear" and self.state == RobotState.OBSTACLE:
            self.get_logger().info('Obstacle cleared! Resuming movement.')
            self.move_to_pose(self.current_goal)
    
    # 현재 위치를 구독하는 토픽(nav2 map:=mfc.yaml 명령어에서 발행 중인 토픽)
    def amcl_pose_callback(self, msg):
        self.current_pose = msg.pose.pose
        self.current_pose_x, self.current_pose_y = self.current_pose.position.x, self.current_pose.position.y
        # self.get_logger().info(f'Current pose: {self.current_pose}')
    
    # 목표 위치로 이동하는 메서드
    def move_to_pose(self, pose_name):
        if pose_name not in self.pose_dict:
            self.get_logger().error(f'Pose {pose_name} not found in pose dictionary.')
            return

        self.current_goal = pose_name
        target = self.pose_dict[pose_name]
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = self.nav.get_clock().now().to_msg()
        goal_pose.pose.position.x = target[0]
        goal_pose.pose.position.y = target[1]
        goal_pose.pose.orientation.z = target[2]
        goal_pose.pose.orientation.w = target[3]

        # 목표 위치로 이동
        self.nav.goToPose(goal_pose)
        self.set_state(RobotState.MOVING)

        while not self.nav.isTaskComplete():
            feedback = self.nav.getFeedback()
            
            if feedback:
                distance_remaining = self.calculate_distance(self.current_pose, target)
                self.get_logger().info(f'Distance remaining: {distance_remaining:.2f} meters.')

                if distance_remaining < 0.25:
                    self.set_state(RobotState.ADJUSTING)
                    self.publish_state()
                    if self.arrive == "complete":
                        self.stop_robot()
                        self.set_state(RobotState.STOP)
                        self.publish_state()
                        break

        # i = 0
        # while not self.nav.isTaskComplete():
        #     i += 1
        #     feedback = self.nav.getFeedback()
            
        #     if feedback and i % 5 == 0:
        #         self.get_logger().info(f'Distance remaining: {feedback.distance_remaining:.2f} meters.')
            
        #     # 목표 지점 근처에 도달했을 때 ADJUSTING 상태로 전환 및 완료 메세지 구독 시 로봇 정
        #     if feedback and feedback.distance_remaining < 0.25:
        #         self.set_state(RobotState.ADJUSTING)
        #         self.publish_state()
        #         if self.arrive == "complete":
        #             self.stop_robot()
        #             self.set_state(RobotState.STOP)
        #             self.publish_state()
        #             break
        #         else:
        #             return
                        
        result = self.nav.getResult()
        if result == TaskResult.SUCCEEDED:
            self.get_logger().info('Goal succeeded!')
            self.publish_result('Goal succeeded!')
            # self.stop_robot()
        elif result == TaskResult.CANCELED:
            self.get_logger().info('Goal was canceled!')
            self.publish_result('Goal was canceled!')
            # self.stop_robot()
        elif result == TaskResult.FAILED:
            self.get_logger().info('Goal failed!')
            self.publish_result('Goal failed!')
            # self.stop_robot()    
            
        # self.stop_robot()
        # self.state = RobotState.STOP
        # self.publish_state()

    def calculate_distance(self, current_pose, target_pose):
        dx = current_pose.position.x - target_pose[0]
        dy = current_pose.position.y - target_pose[1]
        return math.sqrt(dx * dx + dy * dy)

    def stop_robot(self):
        stop_msg = Twist()
        stop_msg.linear.x = 0.0
        stop_msg.linear.y = 0.0
        stop_msg.linear.z = 0.0
        stop_msg.angular.x = 0.0
        stop_msg.angular.y = 0.0
        stop_msg.angular.z = 0.0
        self.cmd_vel_publisher.publish(stop_msg)
        self.get_logger().info('Robot stopped.')
    
    def publish_result(self, result_msg):
        result = String()
        result.data = result_msg
        self.result_publisher.publish(result)
        
    def set_state(self, state):
        self.state = state
        self.publish_state()

    def publish_state(self):
        state_msg = String()
        state_msg.data = f'Robot state: {self.state.name}'
        self.state_publisher.publish(state_msg)
    
def main(args=None):
    rclpy.init(args=args)
    node = Robot()
    
    try:
        rclpy.spin(node)
    except Exception as e:
        node.get_logger().error(f'Exception occurred: {e}')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
