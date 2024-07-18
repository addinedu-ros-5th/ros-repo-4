#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped  # AMCL 포즈 메시지 타입

class CommunicationRobotNode(Node):
    def __init__(self):
        super().__init__('communication_robot_node')
        self.subscription = self.create_subscription(
            PoseWithCovarianceStamped,
            '/amcl_pose',  # AMCL 포즈 토픽 이름
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        position = msg.pose.pose.position
        orientation = msg.pose.pose.orientation
        self.get_logger().info(
            f'I heard: Position(x: {position.x}, y: {position.y}, z: {position.z}), '
            f'Orientation(x: {orientation.x}, y: {orientation.y}, z: {orientation.z}, w: {orientation.w})'
        )

def main(args=None):
    rclpy.init(args=args)
    node = CommunicationRobotNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
