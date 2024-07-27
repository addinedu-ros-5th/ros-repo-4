import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped, Twist, PoseArray
from std_msgs.msg import String
import math
import time
from enum import Enum

# 로봇 상태를 나타내는 열거형(Enum) 클래스
class RobotState(Enum):
    STOP = 1
    MOVING = 2
    ADJUSTING = 3
    OBSTACLE = 4
    STOPOVER1 = 5
    STOPOVER2 = 6
    STOPOVER3 = 7
    FINAL_GOAL = 8

# 로봇 제어를 담당하는 클래스
class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.navigator = BasicNavigator()
        # self.navigator.lifecycleStartup()
        # self.navigator.waitUntilNav2Active()

        # 변수 및 상태 초기화
        self.state = RobotState.STOP
        self.current_pose = None
        self.current_goal = None
        self.arrive = None
        self.obstacle = None

        # 구독자 설정
        self.path_subscriber = self.create_subscription(Path, 'planned_path', self.path_callback, 10)
        self.target_pose_subscriber = self.create_subscription(PoseArray, 'target_poses', self.target_pose_callback, 10)
        self.arrive_pose_subscriber = self.create_subscription(String, 'arrive_pose', self.arrive_topic_callback, 10)
        self.pose_subscriber = self.create_subscription(PoseWithCovarianceStamped, 'amcl_pose', self.amcl_pose_callback, 10)
        self.obstacle_subscriber = self.create_subscription(String, 'obstacle_topic', self.obstacle_topic_callback, 10)
        self.job_subscriber = self.create_subscription(String, 'job', self.job_callback, 10)

        # 퍼블리셔 설정
        self.state_publisher = self.create_publisher(String, 'state_topic', 10)
        self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

        # 목표 포즈 및 초기 상태 설정
        self.target_pose = None
        self.state = RobotState.STOP
        self.home_pose = PoseStamped()
        self.home_pose.pose.position.x = 0.0
        self.home_pose.pose.position.y = 0.0
        self.home_pose.pose.orientation.z = 0.0
        self.home_pose.pose.orientation.w = 1.0
        self.job_done = False

        self.publish_state()

        # AMCL 서비스가 사용 가능해질 때까지 대기
        # self.wait_for_amcl_service()

    # def wait_for_amcl_service(self):
    #     while not self.has_service('/amcl/get_state'):
    #         self.get_logger().info('amcl/get_state service not available, waiting...')
    #         time.sleep(1)

    # def has_service(self, service_name):
    #     return any(service_name in service for service in self.get_service_names_and_types())


    # 경로 정보를 수신하는 콜백 함수
    def path_callback(self, msg):
        if not msg.poses:
            return
        self.path = msg.poses
        self.current_goal_index = 0
        self.navigate_path()

    # 도착 정보를 수신하는 콜백 함수
    def arrive_topic_callback(self, msg):
        self.arrive = msg.data

    # 목표 포즈를 수신하는 콜백 함수
    def target_pose_callback(self, msg):
        self.target_pose = msg
        self.navigate_path()

    # 장애물 정보를 수신하는 콜백 함수
    def obstacle_topic_callback(self, msg):
        self.obstacle = msg.data
        if self.obstacle == "obstacle" and self.state == RobotState.MOVING:
            self.get_logger().warn('Obstacle detected! Stopping the robot.')
            self.stop_robot()
            self.set_state(RobotState.OBSTACLE)
        elif self.obstacle == "clear" and self.state == RobotState.OBSTACLE:
            self.get_logger().info('Obstacle cleared! Resuming movement.')
            self.navigate_path()

    # 현재 위치를 수신하는 콜백 함수
    def amcl_pose_callback(self, msg):
        self.current_pose = msg.pose.pose

    # 경로를 따라 이동하는 함수
    def navigate_path(self):
        if not self.target_pose or not hasattr(self, 'path'):
            return

        self.state = RobotState.MOVING
        self.publish_state()

        self.navigator.goThroughPoses(self.path)
        self.set_state(RobotState.MOVING)

        while not self.navigator.isTaskComplete():
            feedback = self.navigator.getFeedback()

            if feedback:
                distance_remaining = self.calculate_distance(self.current_pose, self.path[-1].pose)
                self.get_logger().info(f'Distance remaining: {distance_remaining:.2f} meters.')

                if distance_remaining < 0.25:
                    self.set_state(RobotState.ADJUSTING)
                    self.publish_state()
                    if self.arrive == "complete":
                        self.stop_robot()
                        self.set_state(RobotState.STOP)
                        self.publish_state()
                        break

        result = self.navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            self.arrive_at_waypoint()
        else:
            self.state = RobotState.STOP
            self.publish_state()

    # 경유지에 도착했을 때 호출되는 함수
    def arrive_at_waypoint(self):
        self.publish_arrive_pose()
        time.sleep(3)  # 3초 대기

        if self.current_goal_index < len(self.path) - 1:
            self.current_goal_index += 1
            self.state = RobotState.STOPOVER1 + self.current_goal_index
        else:
            self.state = RobotState.FINAL_GOAL
        self.publish_state()

        while not self.job_done:
            rclpy.spin_once(self, timeout_sec=1)

        self.job_done = False
        self.navigate_path()

    # 현재 위치와 목표 위치 간의 거리를 계산하는 함수
    def calculate_distance(self, current_pose, target_pose):
        dx = current_pose.position.x - target_pose.position.x
        dy = current_pose.position.y - target_pose.position.y
        return math.sqrt(dx * dx + dy * dy)

    # 로봇을 정지시키는 함수
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

    # 경유지에 도착했음을 알리는 메시지를 발행하는 함수
    def publish_arrive_pose(self):
        arrive_msg = String()
        arrive_msg.data = f'Arrived at waypoint {self.current_goal_index}'
        self.state_publisher.publish(arrive_msg)

    # 현재 로봇의 상태를 발행하는 함수
    def publish_state(self):
        state_msg = String()
        state_msg.data = self.state.name
        self.state_publisher.publish(state_msg)

    # 작업 완료 여부를 수신하는 콜백 함수
    def job_callback(self, msg):
        if msg.data == 'job_done':
            self.job_done = True

    # 다음 목표를 기다리거나 홈으로 돌아가는 함수
    def wait_for_next_target_or_return_home(self):
        timeout = 10  # 10초 동안 다음 목표를 기다림
        start_time = time.time()
        while time.time() - start_time < timeout:
            rclpy.spin_once(self, timeout_sec=1)
            if self.target_pose and (self.target_pose.pose.position.x != 0.0 or self.target_pose.pose.position.y != 0.0):
                self.navigate_path()
                return

        self.target_pose = self.home_pose
        self.navigate_path()

    # 로봇의 상태를 설정하고 발행하는 함수
    def set_state(self, state):
        self.state = state
        self.publish_state()

# 메인 함수
def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    
    try:
        rclpy.spin(node)
    except Exception as e:
        node.get_logger().error(f'Exception occurred: {e}')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


# 2차 시도
# ---------------------------------------------------------------------------------------------------
# import rclpy
# from rclpy.node import Node
# from nav_msgs.msg import Path
# from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
# from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped, Twist
# from rclpy.qos import QoSProfile, ReliabilityPolicy
# from std_msgs.msg import String
# import math
# import time
# from enum import Enum

# class RobotState(Enum):
#     STOP = 1
#     MOVING = 2
#     ADJUSTING = 3
#     OBSTACLE = 4
#     STOPOVER1 = 5
#     STOPOVER2 = 6
#     STOPOVER3 = 7
#     FINAL_GOAL = 8

# # qos_profile = QoSProfile(
# #     reliability=ReliabilityPolicy.RMW_QOS_POLICY_RELIABILITY_RELIABLE,
# #     depth=10
# # )

# class RobotController(Node):
#     def __init__(self):
#         super().__init__('robot_controller')
#         self.navigator = BasicNavigator()
#         self.nav.lifecycleStartup()
#         self.navigator.waitUntilNav2Active()

#         # 변수, 상태 초기화
#         self.state = RobotState.STOP
#         self.current_pose = None
#         self.current_goal = None
#         self.arrive = None
#         self.obstacle = None
        
#         # Subscriber
#         self.path_subscriber        = self.create_subscription(Path, 'planned_path', self.path_callback, 10)
#         self.target_pose_subscriber = self.create_subscription(PoseStamped, 'target_pose', self.target_pose_callback, 10)
#         self.arrive_pose_subscriber = self.create_subscription(String, 'arrive_pose', self.arrive_topic_callback, 10)
#         self.pose_subscriber        = self.create_subscription(PoseWithCovarianceStamped, 'amcl_pose', self.amcl_pose_callback, 10)
#         self.arrive_pose_subscriber = self.create_subscription(String, 'arrive_pose', self.arrive_topic_callback, 10)
#         self.obstacle_subscriber    = self.create_subscription(String, 'obstacle_topic', self.obstacle_topic_callback, 10)
#         self.job_subscriber         = self.create_subscription(String, 'job', self.job_callback, 10)
        
#         # Publisher
#         # self.state_publisher = self.create_publisher(String, 'robot_state', 10)
#         self.state_publisher = self.create_publisher(String, 'state_topic', 10)
#         self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

#         # 목표 포즈 및 초기 상태 설정
#         self.target_pose = None
#         self.state = RobotState.STOP
#         self.home_pose = PoseStamped()
#         self.home_pose.pose.position.x = 0.0
#         self.home_pose.pose.position.y = 0.0
#         self.home_pose.pose.orientation.z = 0.0
#         self.home_pose.pose.orientation.w = 1.0
#         self.job_done = False

#         self.publish_state()
    
#     # 경로 정보를 수신하는 콜백 함수   
#     def path_callback(self, msg):
#         if not msg.poses:
#             return
#         self.path = msg.poses
#         self.current_goal_index = 0
#         self.navigate_path()

#     # 도착 정보를 수신하는 콜백 함수
#     def arrive_topic_callback(self, msg):
#         self.arrive = msg.data
    
#     # 목표 포즈를 수신하는 콜백 함수
#     def target_pose_callback(self, msg):
#         self.target_pose = msg
#         self.navigate_path()
    
#     # AI 서버와 사람 인식 시 발행받는 토픽 / 이동중 장애물 발견 시 속도=0, 장애물 사라지면 최근 위치로 재이동
#     def obstacle_topic_callback(self, msg):
#         self.obstacle = msg.data
#         if self.obstacle == "obstacle" and self.state == RobotState.MOVING:
#             self.get_logger().warn('Obstacle detected! Stopping the robot.')
#             self.stop_robot()
#             self.set_state(RobotState.OBSTACLE)
#         elif self.obstacle == "clear" and self.state == RobotState.OBSTACLE:
#             self.get_logger().info('Obstacle cleared! Resuming movement.')
#             self.navigate_path()
    
#     # 현재 위치를 구독하는 토픽(nav2 map:=mfc.yaml 명령어에서 발행 중인 토픽)
#     def amcl_pose_callback(self, msg):
#         self.current_pose = msg.pose.pose
#         # self.current_pose_x, self.current_pose_y = self.current_pose.position.x, self.current_pose.position.y
#         # self.get_logger().info(f'Current pose: {self.current_pose}')
    
#     # 경로를 따라 이동하는 함수
#     def navigate_path(self):
#         if not self.target_pose:
#             return

#         self.state = RobotState.MOVING
#         self.publish_state()

#         self.navigator.goThroughPoses(self.path)
#         self.set_state(RobotState.MOVING)
        
#         while not self.navigator.isTaskComplete():
#             feedback = self.navigator.getFeedback()
            
#             if feedback:
#                 distance_remaining = self.calculate_distance(self.current_pose, self.target_pose)
#                 self.get_logger().info(f'Distance remaining: {distance_remaining:.2f} meters.')

#                 if distance_remaining < 0.25:
#                     self.state = RobotState.ADJUSTING
#                     self.publish_state()
#                     if self.arrive == "complete":
#                         self.stop_robot()
#                         self.state = RobotState.STOP
#                         self.publish_state()
#                         break

#         result = self.navigator.getResult()
#         if result == TaskResult.SUCCEEDED:
#             self.arrive_at_waypoint()
#             # self.state = RobotState.MOVING
#             # self.publish_state()
#         else:
#             self.state = RobotState.STOP
#             self.publish_state()

#     def arrive_at_waypoint(self):
#         self.publish_arrive_pose()
#         time.sleep(3)  # Wait for 3 seconds

#         if self.current_goal_index < len(self.path) - 1:
#             self.current_goal_index += 1
#             self.state = RobotState.STOPOVER1 + self.current_goal_index
#         else:
#             self.state = RobotState.FINAL_GOAL
#         self.publish_state()
        
#         while not self.job_done:
#             rclpy.spin_once(self, timeout_sec=1)

#         self.job_done = False
#         self.navigate_path()

#     def calculate_distance(self, current_pose, target_pose):
#         dx = current_pose.position.x - target_pose.position.x
#         dy = current_pose.position.y - target_pose.position.y
#         return math.sqrt(dx * dx + dy * dy)


#     def stop_robot(self):
#         stop_msg = Twist()
#         stop_msg.linear.x = 0.0
#         stop_msg.linear.y = 0.0
#         stop_msg.linear.z = 0.0
#         stop_msg.angular.x = 0.0
#         stop_msg.angular.y = 0.0
#         stop_msg.angular.z = 0.0
#         self.cmd_vel_publisher.publish(stop_msg)
#         self.get_logger().info('Robot stopped.')

#     def publish_arrive_pose(self):
#         arrive_msg = String()
#         arrive_msg.data = f'Arrived at waypoint {self.current_goal_index}'
#         self.arrive_pose_publisher.publish(arrive_msg)

#     def publish_state(self):
#         state_msg = String()
#         state_msg.data = self.state.name
#         self.state_publisher.publish(state_msg)

#     def job_callback(self, msg):
#         if msg.data == 'job_done':
#             self.job_done = True

#     def wait_for_next_target_or_return_home(self):
#         timeout = 10  # Wait for 10 seconds for the next target_pose
#         start_time = time.time()
#         while time.time() - start_time < timeout:
#             rclpy.spin_once(self, timeout_sec=1)
#             if self.target_pose and (self.target_pose.pose.position.x != 0.0 or self.target_pose.pose.position.y != 0.0):
#                 self.navigate_path()
#                 return

#         self.target_pose = self.home_pose
#         self.navigate_path()

# def main(args=None):
#     rclpy.init(args=args)
#     node = RobotController()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()


# 1차 시도
# ---------------------------------------------------------------------------------------------------------
# import rclpy
# from rclpy.node import Node
# from nav_msgs.msg import Path
# from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
# from geometry_msgs.msg import PoseStamped, Twist
# from std_msgs.msg import String
# import math
# import time
# from enum import Enum

# class RobotState(Enum):
#     STOP = 1
#     MOVING = 2
#     PICKING_START = 3
#     PICKING_FINISH = 4
#     PICKING_END = 5

# class RobotController(Node):
#     def __init__(self):
#         super().__init__('robot_controller')
#         self.navigator = BasicNavigator()
        
#         self.path_subscriber = self.create_subscription(
#             Path,
#             'planned_path',
#             self.path_callback,
#             10
#         )
#         self.target_pose_subscriber = self.create_subscription(
#             PoseStamped,
#             'target_pose',
#             self.target_pose_callback,
#             10
#         )
#         # self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
#         self.state_publisher = self.create_publisher(String, 'robot_state', 10)

#         self.path = []
#         self.target_pose = None
#         self.current_goal_index = 0
#         self.state = RobotState.STOP
#         self.home_pose = [0.0, 0.0, 0.0, 1.0]
        
#         self.target_pose = None
#         self.state = RobotState.STOP
#         self.home_pose = PoseStamped()
#         self.home_pose.pose.position.x = 0.0
#         self.home_pose.pose.position.y = 0.0
#         self.home_pose.pose.orientation.z = 0.0
#         self.home_pose.pose.orientation.w = 1.0

#     def path_callback(self, msg):
#         self.path = [pose.pose.position for pose in msg.poses]
#         self.current_goal_index = 0
#         self.navigate_path()

#     def target_pose_callback(self, msg):
#         self.target_pose = msg.pose
#         if self.path:
#             self.navigate_path()

#     def navigate_path(self):
#         if not self.path or self.current_goal_index >= len(self.path):
#             return

#         self.state = RobotState.MOVING
#         self.publish_state()

#         goal = self.path[self.current_goal_index]
#         distance_to_goal = math.sqrt((goal.x - self.target_pose.position.x) ** 2 + (goal.y - self.target_pose.position.y) ** 2)

#         if distance_to_goal < 0.1:
#             self.current_goal_index += 1
#             if self.current_goal_index >= len(self.path):
#                 self.stop_robot()
#                 if self.current_goal_index == len(self.path):
#                     self.state = RobotState.PICKING_END
#                 else:
#                     self.state = RobotState.PICKING_FINISH
#                 self.publish_state()
#                 self.rotate_robot(self.target_pose.orientation.z, self.target_pose.orientation.w)
#                 time.sleep(10)  # Picking operation simulation
#                 if self.state == RobotState.PICKING_END:
#                     self.state = RobotState.STOP
#                     self.publish_state()
#                     self.wait_for_next_target_or_return_home()
#                 else:
#                     self.state = RobotState.PICKING_FINISH
#                     self.publish_state()
#                 return

#         self.move_towards_goal(goal)

#     def move_towards_goal(self, goal):
#         twist_msg = Twist()
#         twist_msg.linear.x = 0.5  # Simple proportional controller
#         twist_msg.angular.z = 0.0  # Assuming the robot is already oriented towards the goal
#         self.cmd_vel_publisher.publish(twist_msg)

#     def rotate_robot(self, z, w):
#         twist_msg = Twist()
#         twist_msg.linear.x = 0.0
#         twist_msg.angular.z = 0.5 * (math.atan2(2.0 * (w * z), 1.0 - 2.0 * (z ** 2)))
#         self.cmd_vel_publisher.publish(twist_msg)
#         time.sleep(1)  # Give some time for rotation

#     def stop_robot(self):
#         twist_msg = Twist()
#         twist_msg.linear.x = 0.0
#         twist_msg.angular.z = 0.0
#         self.cmd_vel_publisher.publish(twist_msg)

#     def publish_state(self):
#         state_msg = String()
#         state_msg.data = self.state.name
#         self.state_publisher.publish(state_msg)

#     def wait_for_next_target_or_return_home(self):
#         timeout = 10  # Wait for 10 seconds for the next target_pose
#         start_time = time.time()
#         while time.time() - start_time < timeout:
#             rclpy.spin_once(self, timeout_sec=1)
#             if self.target_pose.position.x != 0.0 or self.target_pose.position.y != 0.0:
#                 self.navigate_path()
#                 return

#         self.target_pose.position.x = self.home_pose[0]
#         self.target_pose.position.y = self.home_pose[1]
#         self.target_pose.orientation.z = self.home_pose[2]
#         self.target_pose.orientation.w = self.home_pose[3]
#         self.navigate_path()

# def main(args=None):
#     rclpy.init(args=args)
#     node = RobotController()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()
