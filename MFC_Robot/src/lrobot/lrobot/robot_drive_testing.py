import rclpy
import math
import time
import threading
from enum import Enum
from rclpy.node import Node
from nav_msgs.msg import Path
# from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSDurabilityPolicy, QoSHistoryPolicy
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from rclpy.executors import SingleThreadedExecutor
from std_msgs.msg import String
from minibot_interfaces.msg import GoalPose

class RobotState(Enum):
    STOP = 1
    MOVING = 2
    ADJUSTING = 3
    OBSTACLE = 4

class PathFollower(Node):
    def __init__(self):
        super().__init__('robot_drive_unique')

        # QoS 설정
        # qos_profile_default = QoSProfile(
        #     history=QoSHistoryPolicy.KEEP_LAST,
        #     depth=10,
        #     reliability=QoSReliabilityPolicy.BEST_EFFORT,
        #     durability=QoSDurabilityPolicy.VOLATILE
        # )

        # Publisher
        self.initial_pose_publisher = self.create_publisher(PoseWithCovarianceStamped, 'initialpose', 10)
        self.state_publisher = self.create_publisher(String, 'state_topic', 10)
        
        
        # Subcriber
        self.subscription_path_1 = self.create_subscription(Path, 'planned_path_1', self.path_callback, 10)
        # self.subscription_path_2 = self.create_subscription(Path, 'planned_path_2', self.path_callback, 10)
        
        self.obstacle_subscription = self.create_subscription(String, 'obstacle_topic', self.obstacle_callback, 10)
        self.goal_subscription = self.create_subscription(GoalPose, 'target_pose', self.goal_callback, 10)
        self.amcl_subscription = self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self.amcl_callback, 10)
        # self.laser_subscription = self.create_subscription(LaserScan, '/scan', self.laser_callback, 10)
        
        
        self.nav = BasicNavigator()
        self.nav.waitUntilNav2Active()

        # 초기 위치 퍼블리시
        self.publish_initial_pose()

        # 경로 추종을 비동기적으로 처리하기 위한 스레드
        self.state = RobotState.STOP
        self.current_position = None
        self.current_orientation = None
        self.path_following_thread = None
        self.obstacle = None
        
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
        self.set_state(RobotState.MOVING)

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
                    self.set_state(RobotState.ADJUSTING)
                    break

            time.sleep(0.05)  # CPU 사용률 감소를 위해 잠시 대기

        # 최종 결과 확인
        result = self.nav.getResult()
        if result == TaskResult.SUCCEEDED:
            self.get_logger().info("Successfully followed all waypoints!")
        else:
            self.get_logger().info(f"Failed to reach final waypoint: {result}")

    # def obstacle_callback(self, msg):
    #     self.obstacle = msg.data
    #     if self.obstacle == "obstacle": 
    #         self.nav.cancelTask() 
    #         self.stop_robot()
    #         self.get_logger().info("Obstacle detected! Stopping the robot.")
    #     else: 
    #         self.get_logger().info('Obstacle cleared! Resuming movement.')
    #         if self.saved_path:
    #             self.nav.followWaypoints(self.saved_path)

    # 라이다로 장애물 감지 시 사용
    # def laser_callback(self, msg):
    #     min_distance = min(msg.ranges)
    #     if min_distance < 0.2:
    #         self.obstacle_detected = True
    #         self.nav.cancelTask()
    #         self.get_logger().info("Obstacle detected! Stopping the robot.")
    #     else:
    #         self.obstacle_detected = False

    def set_state(self, state):
        self.state = state
        self.get_logger().info(f'State set to: {self.state}')
        self.publish_state()

    def publish_state(self):
        state_msg = String()
        state_msg.data = f'{self.state}'
        self.state_publisher.publish(state_msg)

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








# -----------------------------------------------------------------------------

# import time
# import math
# import rclpy
# import subprocess
# from enum import Enum
# from rclpy.node import Node
# # from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSDurabilityPolicy, QoSHistoryPolicy
# from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
# from geometry_msgs.msg import PoseWithCovarianceStamped, Twist, PoseStamped
# from minibot_interfaces.msg import GoalPose 
# from std_msgs.msg import Header, String
# # from sensor_msgs.msg import LaserScan
# from nav_msgs.msg import Path

# class RobotState(Enum):
#     STOP = 1
#     MOVING = 2
#     ADJUSTING = 3
#     OBSTACLE = 4

# class RobotDrive(Node):
#     def __init__(self):
#         super().__init__('robot_drive')
#         self.nav = BasicNavigator()
        
#         # QoS 설정
#         # qos_profile_default = QoSProfile(
#         #     history=QoSHistoryPolicy.KEEP_LAST,
#         #     depth=10,
#         #     reliability=QoSReliabilityPolicy.RELIABLE,
#         #     durability=QoSDurabilityPolicy.VOLATILE
#         # )
        
#         self.state = RobotState.STOP
#         self.current_pose = None
#         self.goal_pose = None
#         self.saved_path = None
#         self.obstacle = None
#         self.obstacle_detected = False
        
#         self.kp_linear = 0.5
#         self.ki_linear = 0.0
#         self.kd_linear = 0.1
#         self.kp_angular = 1.0
#         self.ki_angular = 0.0
#         self.kd_angular = 0.1
#         self.prev_error_linear = 0.0
#         self.prev_error_angular = 0.0
#         self.integral_linear = 0.0
#         self.integral_angular = 0.0

#         # Publisher
#         self.initial_pose_publisher = self.create_publisher(PoseWithCovarianceStamped, '/initialpose', 10)
#         self.state_publisher = self.create_publisher(String, 'state_topic', 10)
#         self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        
#         # Subscriber
#         self.amclPose_subscription = self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self.amclPose_callback, 10)
#         self.obstacle_subscriber = self.create_subscription(String, 'obstacle_topic', self.obstacle_callback, 10)
#         self.goal_subscription = self.create_subscription(GoalPose, 'target_pose', self.goal_callback, 10)
#         self.path_subscription = self.create_subscription(Path, 'planned_path', self.path_callback, 10)
#         # self.laser_subscription = self.create_subscription(LaserScan, '/scan', self.laser_callback, 10)
        
#         self.publish_initial_pose()
        
#         self.nav.waitUntilNav2Active()
#         self.publish_state()

#         time.sleep(2)

#     def publish_initial_pose(self):
#         pose_msg = PoseWithCovarianceStamped()
#         pose_msg.header = Header()
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

#     # 라이다로 장애물 감지 시 사용
#     # def laser_callback(self, msg):
#     #     min_distance = min(msg.ranges)
#     #     if min_distance < 0.2:
#     #         self.obstacle_detected = True
#     #         self.nav.cancelTask()
#     #         self.get_logger().info("Obstacle detected! Stopping the robot.")
#     #     else:
#     #         self.obstacle_detected = False

#     def amclPose_callback(self, msg):
#         self.current_pose = msg.pose.pose
    
#     def goal_callback(self, msg):
#         self.goal_pose = (
#             msg.position_x,
#             msg.position_y,
#             msg.orientation_z,
#             msg.orientation_w)
#         self.get_logger().info(f"---------------------------Received new goal pose: {self.goal_pose}")

#     def path_callback(self, msg):
#         if not msg.poses:
#             self.get_logger().error("---------------------------Received empty path")
#             return
        
#         self.saved_path = msg.poses
#         self.get_logger().info("------------------------Received new path and starting navigation")
#         self.nav.followWaypoints(self.saved_path)
#         self.set_state(RobotState.MOVING)
#         self.publish_state()

#         while not self.nav.isTaskComplete():
#             feedback = self.nav.getFeedback()
#             if feedback:
#                 current_waypoint_index = feedback.current_waypoint
#                 if current_waypoint_index < len(self.saved_path):
#                     current_pose = self.saved_path[current_waypoint_index].pose.position
#                     remaining_distance = math.hypot(
#                         self.saved_path[-1].pose.position.x - current_pose.x,
#                         self.saved_path[-1].pose.position.y - current_pose.y
#                     )
#                     self.get_logger().info(f"Distance remaining: {remaining_distance:.2f} meters")
                    
#                     if remaining_distance <= 0.02:
#                         self.nav.cancelTask()
#                         self.set_state(RobotState.ADJUSTING)
#                         self.publish_state()
#                         self.reach_goal_orientation()
#                         break
                    
#                     if self.current_pose:
#                         self.follow_path(current_pose, self.saved_path[-1].pose.position)
                    
#             # if self.obstacle:
#             #     self.get_logger().info("Stopped due to obstacle")
#             #     return

#         result = self.nav.getResult()
#         if result == TaskResult.SUCCEEDED:
#             self.get_logger().info("Reached the destination successfully!")
#         else:
#             self.get_logger().info("Failed to reach the destination.")
#         self.set_state(RobotState.STOP)
#         self.publish_state()
    
#     def follow_path(self, current_pose, goal_pose):
#         error_linear = math.hypot(goal_pose.x - current_pose.x, goal_pose.y - current_pose.y)
#         goal_yaw = math.atan2(goal_pose.y - current_pose.y, goal_pose.x - current_pose.x)
#         current_yaw = self.calculate_current_yaw(self.current_pose.orientation)
#         error_angular = self.normalize_angle(goal_yaw - current_yaw)
        
#         self.integral_linear += error_linear
#         self.integral_angular += error_angular
        
#         derivative_linear = error_linear - self.prev_error_linear
#         derivative_angular = error_angular - self.prev_error_angular
        
#         self.prev_error_linear = error_linear
#         self.prev_error_angular = error_angular
        
#         control_signal_linear = (self.kp_linear * error_linear +
#                                  self.ki_linear * self.integral_linear +
#                                  self.kd_linear * derivative_linear)
        
#         control_signal_angular = (self.kp_angular * error_angular +
#                                   self.ki_angular * self.integral_angular +
#                                   self.kd_angular * derivative_angular)
        
#         twist = Twist()
#         twist.linear.x = control_signal_linear
#         twist.angular.z = control_signal_angular
        
#         self.cmd_vel_publisher.publish(twist)
                
#     # def obstacle_callback(self, msg):
#     #     self.obstacle = msg.data
#     #     if self.obstacle == "obstacle": 
#     #         self.nav.cancelTask() 
#     #         self.stop_robot()
#     #         self.get_logger().info("Obstacle detected! Stopping the robot.")
#     #     else: 
#     #         self.get_logger().info('Obstacle cleared! Resuming movement.')
#     #         if self.saved_path:
#     #             self.nav.followWaypoints(self.saved_path)

#     def stop_robot(self):
#         stop_msg = Twist()
#         stop_msg.linear.x = 0.0
#         stop_msg.linear.y = 0.0
#         stop_msg.linear.z = 0.0
#         stop_msg.angular.x = 0.0
#         stop_msg.angular.y = 0.0
#         stop_msg.angular.z = 0.0
#         self.cmd_vel_publisher.publish(stop_msg)

#     def reach_goal_orientation(self):
#         self.get_logger().info('Adjusting to final goal orientation.')
        
#         current_yaw = self.calculate_current_yaw(self.current_pose.orientation)
#         goal_yaw = self.calculate_goal_yaw(self.goal_pose[2], self.goal_pose[3])
#         yaw_diff = self.normalize_angle(goal_yaw - current_yaw)

#         twist = Twist()

#         while abs(yaw_diff) > 0.01:
#             current_yaw = self.calculate_current_yaw(self.current_pose.orientation)
#             yaw_diff = self.normalize_angle(goal_yaw - current_yaw)
            
#             twist.angular.z = 0.1 * yaw_diff
#             self.cmd_vel_publisher.publish(twist)
#             rclpy.spin_once(self, timeout_sec=0.1)
        
#         self.stop_robot()
#         self.get_logger().info('Reached final orientation.')
#         self.set_state(RobotState.STOP)
#         self.publish_state()

#     def calculate_current_yaw(self, orientation):
#         siny_cosp = 2 * (orientation.w * orientation.z + orientation.x * orientation.y)
#         cosy_cosp = 1 - 2 * (orientation.y * orientation.y + orientation.z * orientation.z)
#         return math.atan2(siny_cosp, cosy_cosp)

#     def calculate_goal_yaw(self, orientation_z, orientation_w):
#         siny_cosp = 2 * (orientation_w * orientation_z)
#         cosy_cosp = 1 - 2 * (orientation_z * orientation_z)
#         return math.atan2(siny_cosp, cosy_cosp)

#     def normalize_angle(self, angle):
#         while angle > math.pi:
#             angle -= 2.0 * math.pi
#         while angle < -math.pi:
#             angle += 2.0 * math.pi
#         return angle

#     def set_state(self, state):
#         self.state = state
#         self.get_logger().info(f'State set to: {self.state}')

#     def publish_state(self):
#         state_msg = String()
#         state_msg.data = f'{self.state}'
#         self.state_publisher.publish(state_msg)
            
# def main(args=None):
#     rclpy.init(args=args)
#     robot_drive = RobotDrive()
#     rclpy.spin(robot_drive)
#     robot_drive.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()
