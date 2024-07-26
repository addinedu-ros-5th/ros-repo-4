import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import PoseStamped, Twist
from std_msgs.msg import String
import math
import time
from enum import Enum

class RobotState(Enum):
    STOP = 1
    MOVING = 2
    PICKING_START = 3
    PICKING_FINISH = 4
    PICKING_END = 5

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.navigator = BasicNavigator()

        self.path_subscriber = self.create_subscription(
            Path,
            'planned_path',
            self.path_callback,
            10
        )
        self.target_pose_subscriber = self.create_subscription(
            PoseStamped,
            'target_pose',
            self.target_pose_callback,
            10
        )
        self.arrive_pose_subscriber = self.create_subscription(
            String,
            'arrive_pose',
            self.arrive_topic_callback,
            10
        )
        
        self.state_publisher = self.create_publisher(String, 'robot_state', 10)

        self.target_pose = None
        self.state = RobotState.STOP
        self.home_pose = PoseStamped()
        self.home_pose.pose.position.x = 0.0
        self.home_pose.pose.position.y = 0.0
        self.home_pose.pose.orientation.z = 0.0
        self.home_pose.pose.orientation.w = 1.0

    def path_callback(self, msg):
        if not msg.poses:
            return
        self.path = msg.poses
        self.current_goal_index = 0
        self.navigate_path()

    def target_pose_callback(self, msg):
        self.target_pose = msg
        self.navigate_path()

    def navigate_path(self):
        if not self.target_pose:
            return

        self.state = RobotState.MOVING
        self.publish_state()

        self.navigator.waitUntilNav2Active()

        self.navigator.goThroughPoses(self.path)

        result = self.navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            self.state = RobotState.PICKING_FINISH
            self.publish_state()
            time.sleep(10)  # Picking operation simulation
            self.state = RobotState.PICKING_END
            self.publish_state()
            self.wait_for_next_target_or_return_home()
        else:
            self.state = RobotState.STOP
            self.publish_state()

    def publish_state(self):
        state_msg = String()
        state_msg.data = self.state.name
        self.state_publisher.publish(state_msg)

    def wait_for_next_target_or_return_home(self):
        timeout = 10  # Wait for 10 seconds for the next target_pose
        start_time = time.time()
        while time.time() - start_time < timeout:
            rclpy.spin_once(self, timeout_sec=1)
            if self.target_pose and (self.target_pose.pose.position.x != 0.0 or self.target_pose.pose.position.y != 0.0):
                self.navigate_path()
                return

        self.target_pose = self.home_pose
        self.navigate_path()

def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


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
