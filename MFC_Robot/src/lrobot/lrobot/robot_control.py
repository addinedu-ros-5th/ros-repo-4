import os
import time
import math
import rclpy
from enum import Enum
from rclpy.node import Node
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSDurabilityPolicy, QoSHistoryPolicy
# from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped, Twist
from std_msgs.msg import String
# from rclpy.action import ActionServer
# from robot_move.action import Move

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
    "RH1": [0.0, 0.0, 0.0, 1.0], "RH2": [0.0, 0.0, 0.0, 1.0]
}

# class RobotState(Enum):
#     AtHome = 1
#     To입고 = 2
#     At입고 = 3
#     To적재렉 = 4
#     At적재렉 = 5
#     To출고 = 6
#     At출고 = 7
#     ToHome = 8
#     Charging = 9
#     Error = 10
#     Maintaining = 11

class RobotState(Enum):
    STOP = 1
    MOVING = 2

class Robot(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.pose_dict = pose_dict
        self.nav = BasicNavigator()
        self.nav.lifecycleStartup()
        self.state = RobotState.STOP
        
        # qos_profile_lidar = QoSProfile(
        #     history=QoSHistoryPolicy.KEEP_LAST,
        #     depth=10,
        #     reliability=QoSReliabilityPolicy.BEST_EFFORT,  # LIDAR의 RELIABILITY_QOS_POLICY와 일치시킴
        #     durability=QoSDurabilityPolicy.VOLATILE
        # )
        # qos_profile_default = QoSProfile(
        #     history=QoSHistoryPolicy.KEEP_LAST,
        #     depth=10,
        #     reliability=QoSReliabilityPolicy.RELIABLE,
        #     durability=QoSDurabilityPolicy.VOLATILE
        # )
        
        self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.result_publisher = self.create_publisher(String, 'result_topic', 10)
        self.state_publisher = self.create_publisher(String, 'state_topic', 10)
        # self.create_subscription(LaserScan, '/scan', self.lidar_callback, 10)
        
        self.pose_command_subscriber = self.create_subscription(
            String,
            'pose_commands',
            self.pose_command_callback,
            10
        )
        self.publish_state()

        # self.goal_pose = None
        # self.action_server = ActionServer(
        #     self,
        #     Move,
        #     'move_to_pose',
        #     action_move_callback=self.action_move_callback
        # )
        # self.publish_state()

    def pose_command_callback(self, msg):
        pose_name = msg.data
        if self.state == RobotState.STOP:
            self.get_logger().info(f'Received pose command: {pose_name}')
            self.move_to_pose(pose_name)
        else:
            self.get_logger().warn(f'Currently moving. Ignoring new pose command: {pose_name}')


    def move_to_pose(self, pose_name):
        if pose_name not in self.pose_dict:
            self.get_logger().error(f'Pose {pose_name} not found in pose dictionary.')
            return

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

        i = 0
        while not self.nav.isTaskComplete():
            i += 1
            feedback = self.nav.getFeedback()
            
            if feedback and i % 5 == 0:
                self.get_logger().info(f'Distance remaining: {feedback.distance_remaining:.2f} meters.')
            
            # 네비게이션 타임아웃 설정
            if feedback.navigation_time.sec > 10:
                self.nav.cancelTask()
                self.get_logger().info('Navigation task canceled due to timeout.')
                break

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
    
    # 액션으로 주고 받는 방법
    # def execute_callback(self, goal_handle):
    #     self.get_logger().info('Executing goal...')
    #     pose_name = goal_handle.request.pose_name
    #     if pose_name not in self.pose_dict:
    #         goal_handle.abort()
    #         self.get_logger().error(f'Pose {pose_name} not found in pose dictionary.')
    #         return Move.Result()

    #     self.goal_pose = self.pose_dict[pose_name]
    #     self.state = RobotState.MOVING
    #     self.publish_state()

    #     goal_pose = PoseStamped()
    #     goal_pose.header.frame_id = 'map'
    #     goal_pose.header.stamp = self.nav.get_clock().now().to_msg()
    #     goal_pose.pose.position.x = self.goal_pose[0]
    #     goal_pose.pose.position.y = self.goal_pose[1]
    #     goal_pose.pose.orientation.z = self.goal_pose[2]
    #     goal_pose.pose.orientation.w = self.goal_pose[3]

    #     self.nav.goToPose(goal_pose)

    #     i = 0
    #     while not self.nav.isTaskComplete():
    #         i += 1
    #         feedback = self.nav.getFeedback()
            
    #         if feedback and i % 5 == 0:
    #             self.get_logger().info(f'Distance remaining: {feedback.distance_remaining:.2f} meters.')
            
    #         if feedback.navigation_time.sec > 10:
    #             self.nav.cancelTask()
    #             self.get_logger().info('Navigation task canceled due to timeout.')
    #             self.publish_result('Goal was canceled due to timeout.')
    #             goal_handle.abort()
    #             self.stop_robot()
    #             self.state = RobotState.STOP
    #             self.publish_state()
    #             return Move.Result()

    #     result = self.nav.getResult()
    #     move_result = Move.Result()
    #     move_result.pose_name = pose_name
    #     if result == TaskResult.SUCCEEDED:
    #         self.get_logger().info('Goal succeeded!')
    #         self.publish_result('Goal succeeded!')
    #         goal_handle.succeed()
    #     elif result == TaskResult.CANCELED:
    #         self.get_logger().info('Goal was canceled!')
    #         self.publish_result('Goal was canceled!')
    #         goal_handle.abort()
    #     elif result == TaskResult.FAILED:
    #         self.get_logger().info('Goal failed!')
    #         self.publish_result('Goal failed!')
    #         goal_handle.abort()
            
    #     self.stop_robot()
    #     self.state = RobotState.STOP
    #     self.publish_state()
    #     return move_result
            
        self.stop_robot()
        self.state = RobotState.STOP
        self.publish_state()

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
