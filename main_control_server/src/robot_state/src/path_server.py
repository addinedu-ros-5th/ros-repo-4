#!/usr/bin/env python3

import rclpy
import threading
# import queue
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped, Quaternion
from nav_msgs.msg import Path # Odometry
from a_star import AStarPlanner  # AStar 클래스 임포트

# robot_task_client에게서 받아야 하는 메세지 타입
from std_msgs.msg import String                                                                                                 # new

class PathServer(Node):
    def __init__(self):
        super().__init__('path_server')

        self.initial_position = (0.0, 0.0)
        self.current_pose = None
        self.goal_pose = None
        
        self.lock = threading.Lock()
        self.new_goal = False
        ## Subscriber
        self.pose_subscription = self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self.pose_callback, 10)

        self.battery_subscription1 = self.create_subscription(String, 'go_to_battery_area_1', self.battery_callback1, 10)        # new
        self.battery_subscription2 = self.create_subscription(String, 'go_to_battery_area_2', self.battery_callback2, 10)        # new

        self.go_to_outbound_subscription1 = self.create_subscription(String, 'go_to_outbound_1', self.go_to_outbound_callback1, 10) # new    
        self.go_to_outbound_subscription2 = self.create_subscription(String, 'go_to_outbound_2', self.go_to_outbound_callback2, 10) # new                        

        self.light_on_subscription1 = self.create_subscription(String, 'light_on_1', self.light_on_callback1, 10)                  #  new
        self.light_on_subscription2 = self.create_subscription(String, 'light_on_2', self.light_on_callback2, 10)                  #  new

        ## Publisher
        self.path_publisher_1 = self.create_publisher(Path, 'planned_path_1', 10)
        # self.path_publisher_2 = self.create_publisher(Path, 'planned_path_2', 10)

        self.path_thread = threading.Thread(target=self.path_processing_thread)
        self.path_thread.start()

    def light_on_callback1(self, msg):                                                                                           # new
        if (msg.data == 'light on1'):
            self.get_logger().info("Rack List 내 직전 goal location LED 켜졌다. 다음 goal location으로 이동해야함")

    def light_on_callback2(self, msg):
        if (msg.data == 'light on2'):
            self.get_logger().info("Rack List 내 직전 goal location LED 켜졌다. 다음 goal location으로 이동해야함")
            
    def go_to_outbound_callback1(self, msg):                                                                                     # new
        if (msg.data == 'OB'):
            self.get_logger().info("OB 지점으로 이동해야함. 도착했음도 robot_task_client한테 알려줘야함")

    def go_to_outbound_callback2(self, msg):                                                                                     # new
        if (msg.data == 'OB'):
            self.get_logger().info("OB 지점으로 이동해야함. 도착했음도 robot_task_client한테 알려줘야함")

    def battery_callback1(self, msg):                                                                                           # new
        if(msg.data == 'R1'):
            self.get_logger().info("R1 지점으로 이동해야함. 도착했음도 robot_task_client한테 알려줘야함")

    def battery_callback2(self, msg):                                                                                           # new
        if(msg.data == 'R2'):
            self.get_logger().info("R2 지점으로 이동해야함. 도착했음도 robot_task_client한테 알려줘야함")
    

    def pose_callback(self, msg):
        # robot_id = 1
        self.current_pose = (
            msg.pose.pose.position.x,
            msg.pose.pose.position.y)
        self.get_logger().info(f'Current pose: {self.current_pose}')

    def path_processing_thread(self):
        while rclpy.ok():
            with self.lock:
                if self.new_goal and self.current_pose:
                    self.new_goal = False
                    self.move_to_target()
            rclpy.spin_once(self, timeout_sec=0.1)


    def move_to_target(self):
        if not self.goal_pose:
            self.get_logger().error("Goal pose is not set.")
            return
        
        sx_real, sy_real = self.current_pose if self.current_pose else self.initial_position
        gx_real, gy_real, gz_real, gw_real = self.goal_pose

        sx_real = round(sx_real, 2)
        sy_real = round(sy_real, 2)
        gx_real = round(gx_real, 2)
        gy_real = round(gy_real, 2)

        # A* 경로 계획 수행
        a_star = AStarPlanner(resolution=1, rr=0.3, padding=1)
        
        rx, ry, tpx, tpy, tvec_x, tvec_y = a_star.planning(sx_real, sy_real, gx_real, gy_real)

        if not tpx or not tpy:
            self.get_logger().error("No path found")
            return
 
        path = Path()
        path.header.frame_id = 'map'
        path.header.stamp = self.get_clock().now().to_msg()  

        for x, y in zip(tpx, tpy):
            pose = PoseStamped()
            pose.header.frame_id = 'map'
            pose.header.stamp = self.get_clock().now().to_msg()
            pose.pose.position.x = x
            pose.pose.position.y = y
            pose.pose.orientation = Quaternion(z=gz_real, w=gw_real)
            path.poses.append(pose)

        self.path_publisher_1.publish(path)
        self.get_logger().info(f"Published path with {len(tpx)} waypoints.")

def main(args=None):
    rclpy.init(args=args)
    path_server = PathServer()

    try:
        rclpy.spin(path_server)
    except KeyboardInterrupt:
        pass
    finally:
        path_server.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

