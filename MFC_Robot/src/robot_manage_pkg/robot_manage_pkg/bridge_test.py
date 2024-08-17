import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped
import random

class DomainBridgeNode(Node):
    def __init__(self):
        super().__init__('domain_bridge_node')
        
        # 발행자 설정
        # self.publisher_40 = self.create_publisher(Twist, 'base_controller/cmd_vel_unstamped_1', 10)
        # self.publisher_88 = self.create_publisher(Twist, 'base_controller/cmd_vel_unstamped_2', 10)
        self.publisher = self.create_publisher(Twist, 'base_controller/cmd_vel_unstamped', 10)
        # 구독자 설정
        self.subscriber = self.create_subscription(
            PoseWithCovarianceStamped,
            'amcl_pose',
            self.amcl_pose_callback,
            10)

        # 타이머 설정 (0.1초마다 발행)
        self.timer = self.create_timer(1, self.publish_cmd_vel)

    def publish_cmd_vel(self):
        twist = Twist()
        twist.linear.x = 1.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0  # 보통 z축 이동은 없으므로 0으로 설정
        twist.angular.x = 0.0  # 보통 x축 회전은 없으므로 0으로 설정
        twist.angular.y = 0.0  # 보통 y축 회전은 없으므로 0으로 설정
        twist.angular.z = 0.0

        # self.publisher_40.publish(twist)
        # self.publisher_88.publish(twist)
        self.publisher.publish(twist)
    
    def amcl_pose_callback(self, msg):
        self.get_logger().info(f"Received amcl_pose: {msg}")

def main(args=None):
    rclpy.init(args=args)
    node = DomainBridgeNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
