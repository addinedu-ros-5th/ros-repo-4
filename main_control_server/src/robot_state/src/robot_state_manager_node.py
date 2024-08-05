#!/usr/bin/env python3
import sys
import os
import re
import yaml
import threading
import queue
import time
import mysql.connector as con
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor

from modules.connect import Connect
from robot_task_client import RobotTaskClient

# 서비스 서버
from robot_state.srv import UpdateDB
# Task Manager로부터 오는 메세지 타입
from task_manager.msg import SendAllocationResults
# Robot Task Client으로부터 오는 메세지 타입
from robot_state.msg import AllTaskDone     
# RackList 메시지 타입
from robot_state.msg import RackList

# YAML 파일 경로
yaml_file_path = '/home/min/dev_ws/ros-repo-4/main_control_server/params/db_user_info.yaml'

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
        self.conn = db_instance.conn

        if not self.conn or not self.cursor:
            self.get_logger().error("Failed to connect to the database")
            return
    
    # 데이터베이스에서 테이블 정보를 가져오는 함수 정의
    def fetchDataQuery(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def loadDataFromDB(self, query):
        robot_data = self.fetchDataQuery(query)
        return robot_data
    
    def updateData(self, query):
        self.cursor.execute(query)
        self.conn.commit()
            
## Version 1.
Robot_Name = "Debugging"
Rack_List = ["Debugging", "Debugging", "Debugging"]
Task_Assignment = "Debugging"
isTaskAssigned = False

class MFCRobotManager(Node):
    def __init__(self):
        super().__init__('mfc_robot_manager')
        self.db_instance = get_mysql_connection()
        self.update_robot_state = UpdateRobotState(self.db_instance)

        # 'UpdateDb' 메세지 타입 서비스 서버
        self.server = self.create_service(UpdateDB, 'update_db', self.update_db_callback)

        # 'SendAllocationResults' 메세지 타입 subscriber
        self.allocation_results_sub = self.create_subscription(
            SendAllocationResults,
            'send_allocation_results',
            self.task_assignment_callback,
            10)
        
        # 'String' 메세지 타입 subscriber                                # new 0801        
        self.task_completes_results_sub = self.create_subscription(
            String,
            'result_topic',
            self.task_complete_callback,
            10)

    def task_complete_callback(self, msg):                            # new 0801
        global Robot_Name
        global Rack_List
        global Task_Assignment

        ## 여기에 'Status' 열 작업 중 -> 작업 완료 필요 ##
        if (msg.data == "All done"):
            query = f"""
                    update Robot_manager 
                    set Status = '작업완료' 
                    where Robot_Name = {Robot_Name} AND Rack_List = {Rack_List} AND Status = '작업중' OR Status = '대기중';
                    """
            self.update_robot_state.updateData(query)
        else:
            self.get_logger().info("작업 중...")
        # elif (msg.data == "dddd")                                  # new 0801

    def update_db_callback(self, request, response):
        # 디버깅용
        print(f"Request : , \n{request}")                                                                      # 4번 출력
        print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')

        ## 여기에 mysql문으로 불러온 것 필요
        robot_name = request.robot_name

        ##############################여기서 estimated_completion_time response 업데이트################
        # timestamp 기준으로 각 로봇 최신 상태 대한 query문  
        if robot_name == "Robo1":    
            query = f"SELECT Robot_Name, Status, Estimated_Completion_Time, Battery_Status FROM Robot_manager WHERE Robot_Name = '{robot_name}' ORDER BY Time DESC LIMIT 1;"
        else:
            query = f"SELECT Robot_Name, Status, Estimated_Completion_Time, Battery_Status FROM Robot_manager WHERE Robot_Name = '{robot_name}' ORDER BY Time DESC LIMIT 1;"
        
        robot_data = self.update_robot_state.loadDataFromDB(query)

        self.get_logger().info(f'{robot_data}')
        
        response.robot_name = robot_data[0][0]
        response.status = robot_data[0][1]
        response.estimated_completion_time = robot_data[0][2]          # new 
        response.battery_status = robot_data[0][3]

        return response

    def task_assignment_callback(self, msg):
        global isTaskAssigned
        global Robot_Name
        global Task_Code
        global Rack_List
        global Task_Assignment
        
        self.get_logger().info(f'Received task assignment for robot: {msg.robot_name}')  # 1번 출력
        self.get_logger().info(f'Task Code: {msg.task_code}')                                                   
        self.get_logger().info(f'Rack List: {msg.rack_list}')
        self.get_logger().info(f'Task Assignment: {msg.task_assignment}')
        ##############################여기 아래에 robot_name & goal_location 전달##############################
        isTaskAssigned = True
        Robot_Name = msg.robot_name
        Task_Code = msg.task_code
        Rack_List = msg.rack_list
        Task_Assignment = msg.task_assignment
        
        print(f"It is in MFCRobotManager")                                              # 2번 출력
        print(Robot_Name, Task_Code, Rack_List, Task_Assignment)                        
        print('################################################################')

        estimated_completion_time = len(Rack_List)
        print(estimated_completion_time)
        print('################################################################')
        rack_list_str = str(Rack_List).replace('[', '').replace(']', '').replace("'", "")  # Format Rack_List correctly
        ######## 여기서 Robot_manager 테이블에 등록하기  ########
        query = f"""
                INSERT INTO Robot_manager (Num, Robot_Name, Location_X, Location_Y, Rack_List, Status, Estimated_Completion_Time, Battery_Status, Task_Assignment, Error_Codes, Time)
                SELECT
                    IFNULL(MAX(Num), 0) + 1,
                    '{Robot_Name}',
                    0.,
                    0.,
                    '{rack_list_str}',
                    '작업중',
                    {float(estimated_completion_time)},
                    IFNULL((SELECT Battery_Status FROM Robot_manager ORDER BY Num DESC LIMIT 1), '100%'),
                    '{Task_Assignment}',
                    "None",
                    NOW()
                FROM
                    Robot_manager;
        """
        self.update_robot_state.updateData(query)
        print("Succeeding to insert in Robot_manager")
        ####################################################

def main(args=None):
    global Robot_Name
    global Rack_List
    global isTaskAssigned

    rclpy.init(args=args)
    executor = MultiThreadedExecutor()

    node1 = MFCRobotManager()
    node2 = RobotTaskClient()

    executor.add_node(node1)
    executor.add_node(node2)

    print("Update 전 초기값")                                                               # 0번 출력
    print(Robot_Name, Rack_List, Task_Assignment)   
    print('################################################################')
    
    try:
        while rclpy.ok():    
            executor.spin_once(timeout_sec=0.1)
            if isTaskAssigned:
                print("Update 후")                                                         # 3번 출력
                print(Robot_Name, Task_Code, Rack_List, Task_Assignment)                   # 5번 출력
                print('################################################################')  
                
                node2.receive_goal_list(Robot_Name, Rack_List, Task_Assignment)            # 6번 출력
                isTaskAssigned = False              # Send goal only once
    finally:
        node1.update_robot_state.conn.close()  # 프로그램 종료 시 연결 닫기
        executor.shutdown()
        node1.destroy_node()
        node2.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
