import os
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
import numpy as np
import cv2
import yaml
import heapq
from scipy.spatial import distance
from ament_index_python.packages import get_package_share_directory

class JPSPlanner:
    def __init__(self, map_image_path, map_yaml_path):
        self.map = cv2.imread(map_image_path, cv2.IMREAD_GRAYSCALE)
        self.load_map_yaml(map_yaml_path)

    def load_map_yaml(self, map_yaml_path):
        with open(map_yaml_path, 'r') as f:
            self.map_metadata = yaml.safe_load(f)
        self.resolution = self.map_metadata['resolution']
        self.origin = self.map_metadata['origin']

    def world_to_map(self, world_coords):
        mx = int((world_coords[0] - self.origin[0]) / self.resolution)
        my = int((world_coords[1] - self.origin[1]) / self.resolution)
        return mx, my

    def map_to_world(self, map_coords):
        wx = map_coords[0] * self.resolution + self.origin[0]
        wy = map_coords[1] * self.resolution + self.origin[1]
        return wx, wy

    def plan_path(self, start, goals):
        waypoints = sorted(goals, key=lambda goal: distance.euclidean(start, goal))
        path = []
        current_position = start
        for waypoint in waypoints:
            sub_path = self.jps_algorithm(self.world_to_map(current_position), self.world_to_map(waypoint))
            path.extend(sub_path)
            current_position = waypoint
        return [self.map_to_world(p) for p in path]

    def jps_algorithm(self, start, goal):
        open_list = []
        closed_list = set()
        came_from = {}

        heapq.heappush(open_list, (self.heuristic(start, goal), start, None))

        while open_list:
            _, current, parent = heapq.heappop(open_list)

            if current in closed_list:
                continue

            came_from[current] = parent

            if current == goal:
                return self.reconstruct_path(came_from, current)

            closed_list.add(current)

            for neighbor in self.get_jump_points(current, goal):
                if neighbor not in closed_list and self.is_walkable(neighbor):
                    heapq.heappush(open_list, (self.heuristic(neighbor, goal), neighbor, current))

        return []

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_jump_points(self, pos, goal):
        jump_points = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for direction in directions:
            jump_point = self.jump(pos, direction, goal)
            if jump_point:
                jump_points.append(jump_point)
        return jump_points

    def jump(self, pos, direction, goal):
        x, y = pos
        dx, dy = direction
        next_pos = (x + dx, y + dy)

        if not self.is_walkable(next_pos):
            return None

        if next_pos == goal:
            return next_pos

        if self.has_forced_neighbors(next_pos, direction):
            return next_pos

        if dx != 0 and dy != 0:
            if self.jump((x + dx, y), (dx, 0), goal) or self.jump((x, y + dy), (0, dy), goal):
                return next_pos
        else:
            if dx != 0:
                if self.jump((x + dx, y), (dx, 0), goal):
                    return next_pos
            if dy != 0:
                if self.jump((x, y + dy), (0, dy), goal):
                    return next_pos

        return self.jump(next_pos, direction, goal)

    def has_forced_neighbors(self, pos, direction):
        x, y = pos
        dx, dy = direction
        if dx != 0 and dy != 0:
            return (self.is_walkable((x - dx, y + dy)) and not self.is_walkable((x - dx, y))) or \
                   (self.is_walkable((x + dx, y - dy)) and not self.is_walkable((x, y - dy)))
        if dx != 0:
            return (self.is_walkable((x + dx, y + 1)) and not self.is_walkable((x, y + 1))) or \
                   (self.is_walkable((x + dx, y - 1)) and not self.is_walkable((x, y - 1)))
        if dy != 0:
            return (self.is_walkable((x + 1, y + dy)) and not self.is_walkable((x + 1, y))) or \
                   (self.is_walkable((x - 1, y + dy)) and not self.is_walkable((x - 1, y)))
        return False

    def is_walkable(self, pos):
        return 0 <= pos[0] < self.map.shape[1] and 0 <= pos[1] < self.map.shape[0] and self.map[pos[1], pos[0]] == 255

    def reconstruct_path(self, came_from, current):
        path = []
        while current is not None:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

class JPSPathPlanner(Node):
    def __init__(self):
        super().__init__('jps_path_planner')
        package_share_directory = get_package_share_directory('lrobot')
        map_image_path = os.path.join(package_share_directory, 'maps', 'mfl.pgm')
        map_yaml_path = os.path.join(package_share_directory, 'maps', 'mfl.yaml')
        self.jps_planner = JPSPlanner(map_image_path, map_yaml_path)
        # self.declare_parameters(
        #     namespace='',
        #     parameters=[
        #         ('map_image_path', '../maps/mfl.pgm'),
        #         ('map_yaml_path', '../maps//mfl.yaml')
        #     ]
        # )
        # map_image_path = self.get_parameter('map_image_path').get_parameter_value().string_value
        # map_yaml_path = self.get_parameter('map_yaml_path').get_parameter_value().string_value
        # self.jps_planner = JPSPlanner(map_image_path, map_yaml_path)

        self.amcl_pose_subscriber = self.create_subscription(
            PoseStamped,
            'amcl_pose',
            self.amcl_pose_callback,
            10
        )
        self.target_pose_subscriber = self.create_subscription(
            PoseStamped,
            'target_pose',
            self.target_pose_callback,
            10
        )

        self.path_publisher = self.create_publisher(Path, 'planned_path', 10)

        self.current_pose = None
        self.target_pose = None
        self.waypoints = []

    def amcl_pose_callback(self, msg):
        self.current_pose = msg.pose

    def target_pose_callback(self, msg):
        self.waypoints.append([msg.pose.position.x, msg.pose.position.y])
        if self.current_pose:
            self.generate_path()

    def generate_path(self):
        if self.current_pose and self.waypoints:
            start = [self.current_pose.position.x, self.current_pose.position.y]
            path = self.jps_planner.plan_path(start, self.waypoints)
            path_msg = Path()
            path_msg.header.stamp = self.get_clock().now().to_msg()
            path_msg.header.frame_id = 'map'
            for waypoint in path:
                pose = PoseStamped()
                pose.pose.position.x = waypoint[0]
                pose.pose.position.y = waypoint[1]
                path_msg.poses.append(pose)
            self.path_publisher.publish(path_msg)
            self.waypoints = []  # Clear waypoints after generating path

def main(args=None):
    rclpy.init(args=args)
    node = JPSPathPlanner()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
