import rclpy
# import queue
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from nav_msgs.msg import Path # Odometry
from minibot_interfaces.msg import GoalPose  # 사용자 정의 메시지 임포트
from lrobot.a_star import AStarPlanner  # AStar 클래스 임포트



class PathServer(Node):
    def __init__(self):
        super().__init__('path_server')

        self.initial_position = (0.0, 0.0)
        self.current_pose = None
        self.goal_pose = None
        
        self.goal_subscription = self.create_subscription(GoalPose, 'target_pose', self.goal_callback, 10)
        self.pose_subscription = self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self.pose_callback, 10)
        self.path_publisher_1 = self.create_publisher(Path, 'planned_path_1', 10)
        # self.path_publisher_2 = self.create_publisher(Path, 'planned_path_2', 10)

        # self.queue = queue.Queue()
        # self.processing = False

        self.astar = AStarPlanner(1, 0.2, 1)  # grid_size, robot_radius, padding을 설정
        
    def pose_callback(self, msg):
        # robot_id = 1
        self.current_pose = (
            msg.pose.pose.position.x,
            msg.pose.pose.position.y)
        self.get_logger().info(f'Current pose: {self.current_pose}')

    def goal_callback(self, msg):
        # robot_id = msg.robot_id
        self.goal_pose = (
            msg.position_x,
            msg.position_y,
            msg.orientation_z,
            msg.orientation_w)
        self.get_logger().info(f'New goal pose: {self.goal_pose}')
        # self.queue.put(msg)
        # if not self.processing:
        #     self.process_next_location()
        #     if self.current_pose:
        #         self.calculate_path()

    def calculate_path(self):
        self.get_logger().info(f'Calculating path from {self.current_pose} to {(self.goal_pose[0], self.goal_pose[1])}')
        
        if self.current_pose:
            current_pose_x, current_pose_y = self.current_pose
        else:
            current_pose_x, current_pose_y = self.initial_position

        self.current_pose = (current_pose_x, current_pose_y)
        path = self.astar.planning(self.current_pose[0], self.current_pose[1], self.goal_pose[0], self.goal_pose[1])
        
        if len(path) == 6:  # 올바른 반환값인지 확인
            rx, ry, tpx, tpy, tvec_x, tvec_y = path
        else:
            self.get_logger().error("Unexpected path format")
            return
        
        if tpx:
            path_msg = Path()
            path_msg.header.frame_id = 'map'
            path_msg.header.stamp = self.get_clock().now().to_msg()
            for x, y in zip(tpx, tpy):
                pose = PoseStamped()
                pose.header.frame_id = 'map'
                pose.header.stamp = self.get_clock().now().to_msg()
                pose.pose.position.x = x
                pose.pose.position.y = y
                pose.pose.orientation.z = self.goal_pose[2]
                pose.pose.orientation.w = self.goal_pose[3]
                path_msg.poses.append(pose)
            
            self.path_publisher_1.publish(path_msg)
            # self.path_publisher_2.publish(path_msg)
            self.get_logger().info('Publishing computed path')
            self.get_logger().info(f'-----------------------Waypoints: {list(zip(tpx, tpy))}')
        else:
            self.get_logger().error('No path found')

def main(args=None):
    rclpy.init(args=args)
    path_server = PathServer()
    rclpy.spin(path_server)
    path_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------------------------------------------------------------------

# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import PoseStamped
# from nav_msgs.msg import Odometry, Path
# from minibot_interfaces.msg import GoalPose  # 사용자 정의 메시지 임포트
# from lrobot.astar import AStar  # AStar 클래스 임포트

# class PathServer(Node):
#     def __init__(self):
#         super().__init__('path_server')
        
#         self.declare_parameter('map_pgm', '/home/ys/5-ros-repo-4/lrobot/install/lrobot/share/lrobot/maps/mfc.pgm')
#         self.declare_parameter('map_yaml', '/home/ys/5-ros-repo-4/lrobot/install/lrobot/share/lrobot/maps/mfc.yaml')

#         map_pgm = self.get_parameter('map_pgm').get_parameter_value().string_value
#         map_yaml = self.get_parameter('map_yaml').get_parameter_value().string_value

        
#         self.goal_subscription = self.create_subscription(
#             GoalPose,
#             'target_pose',
#             self.goal_callback,
#             10)
#         self.pose_subscription = self.create_subscription(
#             Odometry,
#             'amcl_pose',
#             self.pose_callback,
#             10)
#         self.path_publisher = self.create_publisher(Path, 'computed_path', 10)
#         self.astar = AStar(map_pgm, map_yaml)
#         self.goal_pose = None
#         self.current_pose = None

#     def pose_callback(self, msg):
#         self.current_pose = (
#             msg.pose.pose.position.x,
#             msg.pose.pose.position.y
#         )
#         self.get_logger().info(f'Current pose: {self.current_pose}')

#     def goal_callback(self, msg):
#         self.goal_pose = (
#             msg.position_x,
#             msg.position_y,
#             msg.orientation_z,
#             msg.orientation_w
#         )
#         self.get_logger().info(f'New goal pose: {self.goal_pose}')
#         if self.current_pose:
#             self.calculate_path()

#     def calculate_path(self):
#         self.path = self.astar.astar(self.current_pose, (self.goal_pose[0], self.goal_pose[1]))
#         if self.path:
#             path_msg = Path()
#             path_msg.header.frame_id = 'map'
#             path_msg.header.stamp = self.get_clock().now().to_msg()
#             for point in self.path:
#                 pose = PoseStamped()
#                 pose.header.frame_id = 'map'
#                 pose.header.stamp = self.get_clock().now().to_msg()
#                 pose.pose.position.x = point[0]
#                 pose.pose.position.y = point[1]
#                 pose.pose.orientation.z = self.goal_pose[2]
#                 pose.pose.orientation.w = self.goal_pose[3]
#                 path_msg.poses.append(pose)
#             self.publish_path(path_msg)
            
#             # 웨이포인트 전체 리스트 로그 출력
#             self.get_logger().info(f'Waypoints: {self.path}')
#         else:
#             self.get_logger().error('No path found')

#     def publish_path(self, path_msg):
#         self.path_publisher.publish(path_msg)
#         self.get_logger().info('Publishing computed path')

# def main(args=None):
#     rclpy.init(args=args)
#     path_server = PathServer()
#     rclpy.spin(path_server)
#     path_server.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

#---------------------------------------------------------------------------------------------------------------------------------------
# 성공 예시

# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
# from nav_msgs.msg import Path
# from minibot_interfaces.msg import GoalPose
# from lrobot.a_star import AStarPlanner

# class PathServer(Node):
#     def __init__(self):
#         super().__init__('path_server')

#         self.astar = AStarPlanner(0.3, 0.2, 3)
        
#         self.goal_subscription = self.create_subscription(
#             GoalPose,
#             'target_pose',
#             self.goal_callback,
#             10)
#         self.pose_subscription = self.create_subscription(
#             PoseWithCovarianceStamped,
#             'amcl_pose',
#             self.pose_callback,
#             10)
#         self.path_publisher = self.create_publisher(Path, 'computed_path', 10)

#         self.goal_pose = None
#         self.current_pose = None
#         self.robot_current_position = {}
#         self.robot_initial_position = {
#             1: (0.0, 0.0),  # 예시 로봇 ID와 초기 위치
#             2: (1.0, 1.0)
#         }

#     def pose_callback(self, msg):
#         robot_id = 1  # 예시로 고정된 로봇 ID를 사용합니다. 실제로는 msg에서 로봇 ID를 가져와야 합니다.
#         self.robot_current_position[robot_id] = (
#             msg.pose.pose.position.x,
#             msg.pose.pose.position.y
#         )
#         self.get_logger().info(f'Current pose of robot {robot_id}: {self.robot_current_position[robot_id]}')

#     def goal_callback(self, msg):
#         robot_id = msg.robot_id
#         self.goal_pose = (
#             msg.position_x,
#             msg.position_y,
#             msg.orientation_z,
#             msg.orientation_w
#         )
#         self.get_logger().info(f'New goal pose for robot {robot_id}: {self.goal_pose}')
#         self.move_to_target(robot_id)

#     def move_to_target(self, robot_id):
#         if robot_id in self.robot_current_position:
#             current_pose_x, current_pose_y = self.robot_current_position[robot_id]
#         else:
#             current_pose_x, current_pose_y = self.robot_initial_position[robot_id]

#         self.current_pose = (current_pose_x, current_pose_y)
#         self.get_logger().info(f'Moving robot {robot_id} from {self.current_pose} to {self.goal_pose[:2]}')

#         if self.current_pose:
#             self.calculate_path()

#     def calculate_path(self):
#         self.get_logger().info(f'Calculating path from {self.current_pose} to {(self.goal_pose[0], self.goal_pose[1])}')
#         tpx, tpy = self.astar.planning(self.current_pose[0], self.current_pose[1], self.goal_pose[0], self.goal_pose[1])
        
#         if tpx:
#             path_msg = Path()
#             path_msg.header.frame_id = 'map'
#             path_msg.header.stamp = self.get_clock().now().to_msg()
#             for x, y in zip(tpx, tpy):
#                 pose = PoseStamped()
#                 pose.header.frame_id = 'map'
#                 pose.header.stamp = self.get_clock().now().to_msg()
#                 pose.pose.position.x = x
#                 pose.pose.position.y = y
#                 pose.pose.orientation.z = self.goal_pose[2]
#                 pose.pose.orientation.w = self.goal_pose[3]
#                 path_msg.poses.append(pose)
#             self.publish_path(path_msg)
            
#             self.get_logger().info(f'Waypoints: {list(zip(tpx, tpy))}')
#         else:
#             self.get_logger().error('No path found')

#     def publish_path(self, path_msg):
#         self.path_publisher.publish(path_msg)
#         self.get_logger().info('Publishing computed path')

# def main(args=None):
#     rclpy.init(args=args)
#     path_server = PathServer()
#     rclpy.spin(path_server)
#     path_server.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

# ------------------------------------------------------------------------------------------------


# import os
# import heapq as hq
# import math
# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
# from nav_msgs.msg import Path  # Odometry
# from minibot_interfaces.msg import GoalPose  # 사용자 정의 메시지 임포트
# import yaml
# import numpy as np
# from PIL import Image
# from ament_index_python.packages import get_package_share_directory

# # 기존 A* 알고리즘 함수 및 클래스 정의
# class NodeAStar:
#     def __init__(self, x, y, theta=0, parent=None):
#         self.x = x
#         self.y = y
#         self.theta = theta
#         self.parent = parent
#         self.g = 0
#         self.h = 0
#         self.f = 0

#     def euclidean_distance(self, other):
#         return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

#     def is_valid(self, grid_map):
#         return (0 <= self.x < len(grid_map)) and (0 <= self.y < len(grid_map[0])) and (grid_map[self.x][self.y] == 0)

#     def is_move_valid(self, grid_map, move):
#         new_x = self.x + move[0]
#         new_y = self.y + move[1]
#         return (0 <= new_x < len(grid_map)) and (0 <= new_y < len(grid_map[0])) and (grid_map[new_x][new_y] == 0)

#     def apply_move(self, move):
#         return NodeAStar(self.x + move[0], self.y + move[1], self.theta, self)

#     def is_similar(self, other):
#         return (self.x == other.x) and (self.y == other.y)

# MOVES = [(0.2, 0), (-0.2, 0), (0, 0.2), (0, -0.2)]
# G_MULTIPLIER = 0.2
# TOLERANCE = 0.2

# def a_star(start, end, grid_map):
#     if not end.is_valid(grid_map):
#         return None
#     opened = []
#     closed = []
#     final = None
#     hq.heappush(opened, (0.0, start))

#     while final is None and opened:
#         q = hq.heappop(opened)[1]
#         for move in MOVES:
#             if q.is_move_valid(grid_map, move):
#                 next_node = q.apply_move(move)
#             else:
#                 next_node = None
#             if next_node is not None:
#                 if next_node.euclidean_distance(end) < TOLERANCE:
#                     next_node.parent = q
#                     final = next_node
#                     break
#                 next_node.h = next_node.euclidean_distance(end)
#                 next_node.g = q.g + next_node.euclidean_distance(q)
#                 next_node.f = G_MULTIPLIER * next_node.g + next_node.h
#                 next_node.parent = q

#                 potential_open = any(other_f <= next_node.f and other_next.is_similar(next_node) for other_f, other_next in opened)
#                 if not potential_open:
#                     potential_closed = any(other_next.is_similar(next_node) and other_next.f <= next_node.f for other_next in closed)
#                     if not potential_closed:
#                         hq.heappush(opened, (next_node.f, next_node))
#         closed.append(q)

#     return final

# def construct_path(end):
#     path = []
#     current = end
#     while current is not None:
#         path.append((current.x, current.y))
#         current = current.parent
#     path.reverse()
#     return path

# class PathServer(Node):
#     def __init__(self):
#         super().__init__('path_server')

#         self.grid_map = self.load_map('lrobot', 'maps/mfc.yaml')

#         self.goal_subscription = self.create_subscription(
#             GoalPose,
#             'target_pose',
#             self.goal_callback,
#             10)
#         self.pose_subscription = self.create_subscription(
#             PoseWithCovarianceStamped,
#             'amcl_pose',
#             self.pose_callback,
#             10)
#         self.path_publisher = self.create_publisher(Path, 'computed_path', 10)

#         self.goal_pose = None
#         self.current_pose = None

#     def load_map(self, package_name, relative_path):
#         package_path = get_package_share_directory(package_name)
#         yaml_path = os.path.join(package_path, relative_path)

#         with open(yaml_path, 'r') as file:
#             map_data = yaml.safe_load(file)

#         image_path = os.path.join(package_path, map_data['image'])
#         image = Image.open(image_path)
#         map_array = np.array(image)

#         # Convert to binary map (0: free, 1: obstacle)
#         grid_map = np.where(map_array == 0, 1, 0)

#         return grid_map

#     def pose_callback(self, msg):
#         self.current_pose = (msg.pose.pose.position.x, msg.pose.pose.position.y)
#         self.get_logger().info(f'Current pose: {self.current_pose}')

#     def goal_callback(self, msg):
#         self.goal_pose = (msg.position_x, msg.position_y, msg.orientation_z, msg.orientation_w)
#         self.get_logger().info(f'New goal pose: {self.goal_pose}')
#         if self.current_pose:
#             self.calculate_path()

#     def calculate_path(self):
#         self.get_logger().info(f'Calculating path from {self.current_pose} to {(self.goal_pose[0], self.goal_pose[1])}')
        
#         start_node = NodeAStar(float(self.current_pose[0]), float(self.current_pose[1]))
#         goal_node = NodeAStar(float(self.goal_pose[0]), float(self.goal_pose[1]))
        
#         final_node = a_star(start_node, goal_node, self.grid_map)
        
#         if final_node:
#             path = construct_path(final_node)
#             path_msg = Path()
#             path_msg.header.frame_id = 'map'
#             path_msg.header.stamp = self.get_clock().now().to_msg()
#             for (x, y) in path:
#                 pose = PoseStamped()
#                 pose.header.frame_id = 'map'
#                 pose.header.stamp = self.get_clock().now().to_msg()
#                 pose.pose.position.x = x
#                 pose.pose.position.y = y
#                 pose.pose.orientation.z = self.goal_pose[2]
#                 pose.pose.orientation.w = self.goal_pose[3]
#                 path_msg.poses.append(pose)
#             self.publish_path(path_msg)
            
#             # 웨이포인트 전체 리스트 로그 출력
#             self.get_logger().info(f'Waypoints: {path}')
#         else:
#             self.get_logger().error('No path found')

#     def publish_path(self, path_msg):
#         self.path_publisher.publish(path_msg)
#         self.get_logger().info('Publishing computed path')

# def main(args=None):
#     rclpy.init(args=args)
#     path_server = PathServer()
#     rclpy.spin(path_server)
#     path_server.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

# -------------------------------------------------------------------------------------------------------------------------------