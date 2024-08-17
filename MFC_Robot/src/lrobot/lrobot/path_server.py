import rclpy
import threading
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped, Quaternion
from nav_msgs.msg import Path
from robot_state.msg import RackList
from lrobot.a_star import AStarPlanner  # AStar 클래스 임포트
from std_msgs.msg import String

pose_dict = {
    "R_A1": [0.16, 1.50, 0.7, 0.7], "R_A2": [0.16, 1.50, 0.7, 0.7], "R_A3": [0.14, 1.50, 0.7, 0.7],
    "R_B1": [0.68, 1.50, 0.7, 0.7], "R_B2": [0.68, 1.50, 0.7, 0.7], "R_B3": [0.6, 1.50, 0.7, 0.7],
    "R_C1": [1.05, 1.50, 0.7, 0.7], "R_C2": [1.05, 1.50, 0.7, 0.7], "R_C3": [1.05, 1.50, 0.7, 0.7],
    "R_D1": [0.16, 0.35, 0.7, 0.7], "R_D2": [0.16, 0.35, 0.7, 0.7], "R_D3": [0.16, 0.35, 0.7, 0.7],
    "R_E1": [0.68, 0.35, 0.7, 0.7], "R_E2": [0.68, 0.35, 0.7, 0.7], "R_E3": [0.68, 0.35, 0.7, 0.7],
    "R_F1": [1.08, 0.35, 0.7, 0.7], "R_F2": [1.08, 0.35, 0.7, 0.7], "R_F3": [1.08, 0.35, 0.7, 0.7],
    "IB": [0.4, -0.80, -0.7, 0.6], "OB": [0.85, -0.80, -0.7, 0.6],
    "R1": [0.0, 0.0, 0.0, 1.0], # "R2": [0.0, 0.3, 0.0, 1.0],
}
class PathServer(Node):
    def __init__(self):
        super().__init__('path_server')
        self.initial_position = (0.0, 0.0)
        self.current_pose = None
        self.goal_pose = None
        self.path_index = 0  # 현재 목표 인덱스
        self.rack_lsit = []
        self.light_on = False
        self.lock = threading.Lock()
        self.new_goal = False
        self.light_on_2 = False  # task_done 플래그 초기화
        # Subscriber
        self.pose_subscription = self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self.pose_callback, 10)
        self.rack_list_subscription = self.create_subscription(RackList, 'rack_list_2', self.goal_callback, 10)
        self.task_done_subscription = self.create_subscription(String, 'light_on_2', self.light_on_callback2, 10)
        # Publisher
        self.path_publisher_2 = self.create_publisher(Path, 'planned_path_2', 10)
        self.path_thread = threading.Thread(target=self.path_processing_thread)
        self.path_thread.start()
    def pose_callback(self, msg):
        self.current_pose = (
            msg.pose.pose.position.x,
            msg.pose.pose.position.y)
        self.get_logger().info(f'Current pose: {self.current_pose}')
    def light_on_callback2(self, msg):
        if (msg.data == 'light on2'):
            self.light_on = True
            self.get_logger().info("Rack List 내 직전 goal location LED 켜졌다. 다음 goal location으로 이동해야함")
            self.process_next_goal()  # 다음 목표로 이동
    # 렉 리스트 수신
    def goal_callback(self, msg):
        with self.lock:
            # rack_list 메시지를 수신하여 목표 리스트 갱신
            self.goal_list = msg.rack_list
            self.new_goal = True
            self.path_index = 0  # 새로운 목표 리스트가 수신되면 인덱스를 초기화
            self.light_on = True  # 첫 목표로 이동할 준비
            self.get_logger().info(f'Received new rack list: {self.goal_list}')
    def path_processing_thread(self):
        while rclpy.ok():
            rclpy.spin_once(self, timeout_sec=0.1)
    def process_next_goal(self):
        with self.lock:
            if self.light_on and self.current_pose and self.path_index < len(self.goal_list):
                key = self.goal_list[self.path_index]
                self.goal_pose = pose_dict.get(key, None)
                if self.goal_pose:
                    self.light_on = False
                    self.move_to_target()
            elif self.path_index >= len(self.goal_list):
                self.get_logger().info("All Complete!!")
                self.new_goal = False
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
        self.path_publisher_2.publish(path)
        self.get_logger().info(f"Published path with {len(tpx)} waypoints.")
        self.path_index += 1  # 다음 목표로 인덱스 증가
        
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
#--------------------------------------------------------------
# import rclpy
# import threading
# # import queue
# from rclpy.node import Node
# from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped, Quaternion
# from nav_msgs.msg import Path # Odometry
# from minibot_interfaces.msg import GoalPose  # 사용자 정의 메시지 임포트
# from lrobot.a_star import AStarPlanner  # AStar 클래스 임포트
# from robot_state.msg import RackList


# class PathServer(Node):
#     def __init__(self):
#         super().__init__('path_server')

#         self.initial_position = (0.0, 0.0)
#         self.current_pose = None
#         self.goal_pose = None
        
#         self.lock = threading.Lock()
#         self.new_goal = False
        
#         self.goal_subscription = self.create_subscription(GoalPose, 'target_pose', self.goal_callback, 10)
#         self.pose_subscription = self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self.pose_callback, 10)
#         self.path_publisher_1 = self.create_publisher(Path, 'planned_path_1', 10)
#         # self.path_publisher_2 = self.create_publisher(Path, 'planned_path_2', 10)

#         self.path_thread = threading.Thread(target=self.path_processing_thread)
#         self.path_thread.start()
        
#     def pose_callback(self, msg):
#         # robot_id = 1
#         self.current_pose = (
#             msg.pose.pose.position.x,
#             msg.pose.pose.position.y)
#         self.get_logger().info(f'Current pose: {self.current_pose}')

#     def goal_callback(self, msg):
#         with self.lock:
#             self.goal_pose = (
#                 msg.position_x,
#                 msg.position_y,
#                 msg.orientation_z,
#                 msg.orientation_w)
#             self.new_goal = True
#         self.get_logger().info(f'New goal pose: {self.goal_pose}')

#     def path_processing_thread(self):
#         while rclpy.ok():
#             with self.lock:
#                 if self.new_goal and self.current_pose:
#                     self.new_goal = False
#                     self.move_to_target()
#             rclpy.spin_once(self, timeout_sec=0.1)


#     def move_to_target(self):
#         if not self.goal_pose:
#             self.get_logger().error("Goal pose is not set.")
#             return
        
#         sx_real, sy_real = self.current_pose if self.current_pose else self.initial_position
#         gx_real, gy_real, gz_real, gw_real = self.goal_pose

#         sx_real = round(sx_real, 2)
#         sy_real = round(sy_real, 2)
#         gx_real = round(gx_real, 2)
#         gy_real = round(gy_real, 2)

#         # A* 경로 계획 수행
#         a_star = AStarPlanner(resolution=1, rr=0.3, padding=1)
        
#         rx, ry, tpx, tpy, tvec_x, tvec_y = a_star.planning(sx_real, sy_real, gx_real, gy_real)

#         if not tpx or not tpy:
#             self.get_logger().error("No path found")
#             return
 
#         path = Path()
#         path.header.frame_id = 'map'
#         path.header.stamp = self.get_clock().now().to_msg()  

#         for x, y in zip(tpx, tpy):
#             pose = PoseStamped()
#             pose.header.frame_id = 'map'
#             pose.header.stamp = self.get_clock().now().to_msg()
#             pose.pose.position.x = x
#             pose.pose.position.y = y
#             pose.pose.orientation = Quaternion(z=gz_real, w=gw_real)
#             path.poses.append(pose)

#         self.path_publisher_1.publish(path)
#         self.get_logger().info(f"Published path with {len(tpx)} waypoints.")

# def main(args=None):
#     rclpy.init(args=args)
#     path_server = PathServer()
#     try:
#         rclpy.spin(path_server)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         path_server.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()

