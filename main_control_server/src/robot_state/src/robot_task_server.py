#!/usr/bin/env python3

import math
import time
import threading
import yaml
import mysql.connector as con
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.executors import MultiThreadedExecutor
from robot_state.action import RobotTask
from geometry_msgs.msg import PoseWithCovarianceStamped
from data.location_data import pose_dict
from modules.connect import Connect

# threading에서 Lock 함수 가져오기
lock = threading.Lock()  
# 로봇 현재 상태 초기값 세팅
current_pose = [-10.0, -10.0, 10.0, 10.0]
# 디버깅용 임의 pose_dict                   # ["R_A1", "R_B2", "R_C3"] # new
pose_dict = {
    "R_A1": [0.007, 0.970, 0.99, 1.0], "R_A2": [0.007,  0.970, 0.99, 1.0], "R_A3": [0.007,  0.970, 0.99, 1.0],
    "R_B1": [0.445, 0.9057, 0.99, 1.0], "R_B2": [0.445, 0.9057, 0.99, 1.0], "R_B3": [0.445, 0.9057, 0.99, 1.0],
    "R_C1": [-0.020, 1.678, 0.99, 1.0], "R_C2": [-0.020, 1.678, 0.99, 1.0], "R_C3": [-0.020, 1.678, 0.99, 1.0],
    "R_D1": [0.007, 0.970, 0.99, 1.0], "R_D2": [0.007, 0.970, 0.99, 1.0], "R_D3": [0.007, 0.970, 0.99, 1.0],
    "R_E1": [0.445, 0.9057, 0.99, 1.0], "R_E2": [0.445, 0.9057, 0.99, 1.0], "R_E3": [0.445, 0.9057, 0.99, 1.0],
    "R_F1": [-0.020, 1.678, 0.99, 1.0], "R_F2": [-0.020, 1.678, 0.99, 1.0], "R_F3": [-0.020, 1.678, 0.99, 1.0],
    "I1": [0.116, -1.11, 0.0, 1.0], "I2": [0.416, -1.11, 1.0, 0.0],
    "O1": [0.716, -1.11, 0.0, 1.0], "O2": [0.716, -1.11, 1.0, 0.0],
}


# YAML 파일 경로
yaml_file_path = '/home/edu/dev_ws/git_ws2/ros-repo-4/main_control_server/params/db_user_info.yaml'

# YAML 파일을 읽어 파라미터를 가져옴
def load_db_params(file_path):
    with open(file_path, 'r') as file:
        params = yaml.safe_load(file)
    return params['local_db']['id'], params['local_db']['pw']

def get_mysql_connection():
    try:
        db_id, db_pw = load_db_params(yaml_file_path)
        db_instance = Connect(db_id, db_pw)
        return db_instance
    except con.Error as err:
        print(f"Error: {err}")
        return None    
    
class UpdateRobotState():
    def __init__(self, db_instance):
        self.cursor = db_instance.cursor

    # 데이터베이스에서 테이블 정보를 가져오는 함수 정의
    def fetchDataQuery(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def loadDataFromDB(self, query):
        robot_data = self.fetchDataQuery(query)
        return robot_data
    
class AmclSubscriber(Node):
    def __init__(self):
        super().__init__('amcl_subscriber')
        self.amcl = PoseWithCovarianceStamped()
        self.subscription = self.create_subscription(
            PoseWithCovarianceStamped,
            'amcl_pose',  # AMCL 포즈 토픽 이름
            self.amcl_callback,
            10
        )
        self.subscription

    def amcl_callback(self, msg):
        global current_pose
        self.amcl = msg
        position = self.amcl.pose.pose.position
        orientation = self.amcl.pose.pose.orientation
        
        lock.acquire()
        try:
            current_pose[0], current_pose[1] = position.x, position.y
            current_pose[2], current_pose[3] = orientation.z, orientation.w
        finally:
            lock.release()
        
        # self.get_logger().info(
        #     f'I heard: Position(x: {position.x}, y: {position.y}, z: {position.z}), '
        #     f'Orientation(x: {orientation.x}, y: {orientation.y}, z: {orientation.z}, w: {orientation.w})'
        # )
        # self.get_logger().info('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

class RobotTaskServer(Node):
    def __init__(self):
        super().__init__('robot_task_server')
        self._action_server = ActionServer(self, RobotTask, 'robot_action', self.robot_task_callback)
        self.cnt = 0

    def robot_task_callback(self, goal_handle):
        global current_pose
        self.get_logger().info('Executing goal...')                                                                         # 8, 15번 출력

        self.isClientSent = False                   # new
        self.isTaskComplete = False                 # new
        goal_msg = goal_handle.request


        while (self.isClientSent == False):  
            if goal_msg.robot_name != "Debugging":
                self.get_logger().info(f'Client sent: robot_name={goal_msg.robot_name}, goal_location={goal_msg.goal_location}') # 9, 16번 출력 
                self.isClientSent = True
                break

        while(1):
            if self.cnt == 60 or current_pose[0] != -10.0:
                self.get_logger().info(f'Current_pose: pos_x = {current_pose[0]}, pos_y = {current_pose[1]}')                  # 10, 17번 출력 
                break
            self.cnt += 1
            time.sleep(1)

        feedback_msg = RobotTask.Feedback()
        target_pose = pose_dict[goal_msg.goal_location]
        while (self.isTaskComplete == False):                  
            # remaining_distance에 대한 계산
            ## =======================================================
            feedback_msg.remaining_distance = self.calculate_distance(target_pose)
            self.get_logger().info(f'Feedback: {feedback_msg.remaining_distance}')                                              # 11, 18번 출력 
            self.get_logger().info('--------------111111111------------------')
            goal_handle.publish_feedback(feedback_msg)
        
            ## 목표 지점 근처에 도달했을 때 ADJUSTING 상태로 전환
            if feedback_msg.remaining_distance < 0.45:
                self.get_logger().info(f'ADJUSTING MODE')                                                                       # 12, 19번 출력
                ### ADJUSTING 상태 관련 코드 
                #### ------------------------------------- 
                #### ...
                #### -------------------------------------

                ### TaskComplete 업데이트
                self.isTaskComplete = True
                                 
            ## 목표 지점 도달X MOVING 상태 유지
            else:
                self.get_logger().info(f'MOVING MODE')
                time.sleep(1)

            ## =======================================================

        # 조정 완료시 클라이언트에 액션 상태가 변했음을 알림
        goal_handle.succeed()
        result = RobotTask.Result()
        result.task_complete = True
        return result
            
    def calculate_distance(self, target_pose):
        global current_pose

        dx = current_pose[0] - target_pose[0] # 0.75 
        dy = current_pose[1] - target_pose[1] # 0.2  
        
        return math.sqrt(dx * dx + dy * dy)
    
def main(args=None):
    rclpy.init(args=args)
    executor = MultiThreadedExecutor()

    amcl_subscriber = AmclSubscriber()
    robot_task_server = RobotTaskServer()

    executor.add_node(amcl_subscriber)
    executor.add_node(robot_task_server)

    try:
        executor.spin()
    finally:
        executor.shutdown()
        amcl_subscriber.destroy_node()
        robot_task_server.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
