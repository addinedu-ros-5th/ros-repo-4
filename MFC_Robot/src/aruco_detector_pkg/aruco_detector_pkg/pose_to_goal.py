import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class PoseToGoal(Node):
    def __init__(self):
        super().__init__('pose_to_goal')
        
        self.goal_publisher = self.create_publisher(PoseStamped, 'goal_pose', 10)
        self.subscription = self.create_subscription(PoseStamped, '/robot_pose', self.pose_callback, 10)

    def pose_callback(self, msg):
        # 로봇의 현재 위치를 기반으로 목표 위치 계산
        x = msg.pose.position.x + 1.0  # 예시로 현재 위치에서 1m 전방
        y = msg.pose.position.y
        z = msg.pose.position.z
        qx = msg.pose.orientation.x
        qy = msg.pose.orientation.y
        qz = msg.pose.orientation.z
        qw = msg.pose.orientation.w

        self.set_goal(x, y, z, qx, qy, qz, qw)

    def set_goal(self, x, y, z, qx, qy, qz, qw):
        goal = PoseStamped()
        goal.header.frame_id = 'odom'
        goal.header.stamp = self.get_clock().now().to_msg()
        goal.pose.position.x = x
        goal.pose.position.y = y
        goal.pose.position.z = z
        goal.pose.orientation.x = qx
        goal.pose.orientation.y = qy
        goal.pose.orientation.z = qz
        goal.pose.orientation.w = qw
        
        self.goal_publisher.publish(goal)
        self.get_logger().info('Goal published: x={}, y={}, z={}, qx={}, qy={}, qz={}, qw={}'.format(x, y, z, qx, qy, qz, qw))

def main(args=None):
    rclpy.init(args=args)
    node = PoseToGoal()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
