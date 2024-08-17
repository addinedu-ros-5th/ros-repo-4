import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdVelRelay(Node):
    def __init__(self):
        super().__init__('cmd_vel_relay')
        self.get_logger().info('CmdVelRelay node has been started.')

        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_vel_callback,
            10
        )

        self.publisher = self.create_publisher(
            Twist,
            'base_controller/cmd_vel_unstamped',
            10
        )

    def cmd_vel_callback(self, msg):
        self.publisher.publish(msg)
        self.get_logger().info('Relaying cmd_vel message.')

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelRelay()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
