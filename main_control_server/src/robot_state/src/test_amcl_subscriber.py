#!/usr/bin/env python3

import rclpy as rp
from rclpy.node import Node 
from geometry_msgs.msg import PoseWithCovarianceStamped 

class AmclSubscriber(Node):
    def __init__(self):
        super().__init__('amcl_subscriber')
        self.amcl = PoseWithCovarianceStamped()
        self.pose1_sub = self.create_subscription(PoseWithCovarianceStamped, 'amcl_pose', self.amcl_callback1, 10)

    def amcl_callback1(self, msg):
        self.get_logger().info("Received AMCL Pose in RobotStateWindow:", msg)        
        self.get_logger().info('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        self.amcl = msg

    def get_amcl_pose(self):
        return self.amcl
    
def main(args=None):
	rp.init(args=args)
      
    ## 구독자 노드 인스턴스 생성  
	amcl_sub = AmclSubscriber()
	rp.spin(amcl_sub)

	amcl_sub.destroy_node()
	rp.shutdown()

if __name__ == '__main__':
	main()