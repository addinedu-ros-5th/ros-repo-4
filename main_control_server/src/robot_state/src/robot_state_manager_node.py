#!/usr/bin/env python3
import rclpy as rp
from rp.node import Node
from rp.action import ActionServer
import math
import time
import sys
import os
# Connect 클래스 인스턴스 생성
from modules.connect import *
# AmclSubscriber 클래스 인스턴스 생성
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../network_manager/lib/network_manager')))
from communication_robot_node import AmclSubscriber 

# 서비스 서버.
from robot_state.srv import UpdateDB
# 로봇에게 task allocate할 메세지 타입.
from task_manager.msg import SendAllocationResults
<<<<<<< HEAD
from std_msgs.msg import String
=======
# 사용자 정의된 로봇(액션 클라이언트)과 액션 통신 메세지 타입.
from robot_state.action import RobotTask

from rp.executors import MultiThreadedExecutor
>>>>>>> 96233de270818c380ca6186861bd32e9f7b2a54f


def get_mysql_connection():
    try:
        db_instance = Connect("team4", "0444")
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

class TellTaskManager(Node):
    def __init__(self):
        super().__init__('tell_task_manager_service')
        self.db_instance = get_mysql_connection()
        self.update_robot_state = UpdateRobotState(self.db_instance)

        # 'UpdateDB' 메세지 타입의 서비스 서버
        self.server = self.create_service(UpdateDB, 'update_db', self.callback_service)

        # 'SendAllocationResults' 메세지 타입의 subscriber
        self.allocation_results_subscription = self.create_subscription(
            SendAllocationResults,
            'send_allocation_results',
            self.task_assignment_callback,
            10)
        
        self.publisher_pose_commands = self.create_publisher(String, 'pose_commands', 10)

        # self.robot_name = None
        # self.goal_location = None

    def callback_service(self, request, response):
        # 디버깅용
        print(f"Request : \n{request}")
        print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')

        ## 여기에 mysql문으로 불러온 것 필요
        robot_name = request.robot_name

        # timestamp 기준으로 각 로봇 최신 상태 대한 query문  
        if robot_name == "Robo1":    
            query = f"SELECT Robot_Name, Status, Battery_Status FROM Robot_manager WHERE Robot_Name = '{robot_name}' ORDER BY Time DESC LIMIT 1;"
        else:
            query = f"SELECT Robot_Name, Status, Battery_Status FROM Robot_manager WHERE Robot_Name = '{robot_name}' ORDER BY Time DESC LIMIT 1;"  
             
        robot_data = self.update_robot_state.loadDataFromDB(query)
        self.db_instance.disConnection()

        response.robot_name = robot_data[0][0]
        response.status = robot_data[0][1]
        response.battery_status = robot_data[0][2]
   
        return response
    
    def task_assignment_callback(self, msg):
        self.get_logger().info(f'Received task assignment for robot: {msg.robot_name}')  # Robo1
        self.get_logger().info(f'Goal Location: {msg.goal_location}')                    # I1
        self.get_logger().info(f'Task Assignment: {msg.task_assignment}')                # 입고

<<<<<<< HEAD
        pose_command = String()
        pose_command.data = msg.goal_location
        self.publisher_pose_commands.publish(pose_command)
        self.get_logger().info(f'Published pose command: {pose_command.data}')
=======
        ##############################여기다가 robot_state_manager -> robot으로 robot_name goal_location 전달##############################
        # self.robot_name = msg.robot_name
        # self.goal_location = msg.goal_location
        # self.task_assignment = msg.task_assignment

# class TaskManagerSub_Action(TellTaskManager):
#     def __init__(self):
#         super().__init__()
#         self.amcl_subscriber = AmclSubscriber()
#         self.amcl_1 = self.amcl_subscriber.get_amcl_pose()

    
# class MFCRobotServer(Node):
#     def __init__(self):
# 	  ## 구독자 노드 이름 설정
#       super().__init__('mfc_robot_action_server')
#       self.total_dist = 0 
#       self.is_first_time = True 
#       self._action_server = ActionServer(
#             self,
#             RobotTask,
#             'mfc_robot',
#             self.execute_callback)
        
>>>>>>> 96233de270818c380ca6186861bd32e9f7b2a54f
    
def main(args=None):
    db_instance = get_mysql_connection()
    update_robot_state = UpdateRobotState(db_instance)

    ## Case 1.
    # query_A = "SELECT * FROM Robot_manager WHERE  Robot_Name = 'Robo1'"
    # robot_data = update_robot_state.loadDataFromDB(query_A)

    ## Case 2.
    # query2 = "SELECT * FROM Robot_manager WHERE Robot_Name = 'Robo1' ORDER BY Time DESC LIMIT 1;"
    # robot_data = update_robot_state.loadDataFromDB(query2)
    # robot_status = robot_data[0][3] 
    # print(robot_status)

    db_instance.disConnection()

    rp.init(args=args)
    node = TellTaskManager()
    rp.spin(node)
    rp.shutdown()

if __name__ == '__main__':
    main()