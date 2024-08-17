#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped  # AMCL 포즈 메시지 타입

class AmclSubscriber(Node):
    def __init__(self):
        super().__init__('amcl_subscriber')
        self.amcl = PoseWithCovarianceStamped()
        self.subscription = self.create_subscription(
            PoseWithCovarianceStamped,
            'amcl_pose',                       # AMCL 포즈 토픽 이름
            self.amcl_callback1,
            10)
        self.subscription

    def amcl_callback1(self, msg):
        self.amcl = msg
        position = self.amcl.pose.pose.position
        orientation = self.amcl.pose.pose.orientation
        self.get_logger().info(f'I heard: Position(x: {position.x}, y: {position.y}, z: {position.z}), '
                               f'Orientation(x: {orientation.x}, y: {orientation.y}, z: {orientation.z}, w: {orientation.w})'
                               )
        self.get_logger().info("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=")

    def get_amcl_pose(self):
        return self.amcl
    
def main(args=None):
    rclpy.init(args=args)
    node = AmclSubscriber()

    try:
        while rclpy.ok():
            rclpy.spin_once(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
