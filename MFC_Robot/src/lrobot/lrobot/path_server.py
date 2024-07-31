import rclpy
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
        
        self.goal_subscription = self.create_subscription(
            GoalPose,
            'target_pose',
            self.goal_callback,
            10)
        self.pose_subscription = self.create_subscription(
            PoseWithCovarianceStamped,
            '/amcl_pose',
            self.pose_callback,
            10)
        self.path_publisher = self.create_publisher(Path, 'planned_path', 10)

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
        if self.current_pose:
            self.calculate_path()

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
            
            self.path_publisher.publish(path_msg)
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