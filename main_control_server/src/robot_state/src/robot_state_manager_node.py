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
# Task Manager한테 보내야 하는 메세지 타입
from std_msgs.msg import String 

def get_mysql_connection():
    try:
        db_instance = Connect("root", "0")
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

        # 'String' 메세지 타입 publisher
        self.update_robot_state_pub = self.create_publisher(String, 'update_robot_state', 10)

        # 'SendAllocationResults' 메세지 타입 subscriber
        self.allocation_results_sub = self.create_subscription(
            SendAllocationResults,
            'send_allocation_results',
            self.task_assignment_callback,
            10)
        self.allocation_results_sub

        # 'AllTaskDone' 메세지 타입의 subscriber
        self.all_task_done_sub = self.create_subscription(                                  # new 0805
            AllTaskDone,
            'send_all_task_done_results',
            self.all_task_done_callback,
            10
            )
        self.all_task_done_sub    

        self.set_initial_robot_state()

    def set_initial_robot_state(self):
        ############################### Robot 초기 상태 아니면 초기 값들로 세팅 ###############################
        query = f"""
                UPDATE Robot_manager
                    SET 
                        Location_X = 0,
                        Location_Y = 0,
                        Rack_List = '',
                        Status = '대기중',
                        Estimated_Completion_Time = 0,
                        Battery_Status = '100%',
                        Task_Assignment = 'None',
                        Error_Codes = 'None',
                        Call_Num = 0,
                        Time = NOW()
                    WHERE 
                        Rack_List != '' OR Task_Assignment != 'None' ;
                """
        self.update_robot_state.updateData(query)
        self.get_logger().info(f'Set to the Initial State')
        ################################################################################################

    def all_task_done_callback(self, msg):                                                  # new 0801
        global Robot_Name
        global Rack_List
        global Task_Assignment
        
        if (msg.result_msg == "All done"):
            rack_list_str = str(Rack_List).replace('[', '').replace(']', '').replace("'", "")  
            ############################# 여기에 'Status' 열 == 작업중 ->  대기중 필요 #######################
            query = f"""
                    update Robot_manager 
                    set Status = '대기중' 
                    where Robot_Name = '{Robot_Name}' 
                            AND Rack_List = '{rack_list_str}' 
                            AND Status = '작업중' 
                            AND Task_Assignment = '{Task_Assignment}';
                    """
            self.update_robot_state.updateData(query)
        else:
            self.get_logger().info("작업중...")
    
    def update_db_callback(self, request, response):
        # 디버깅용
        print(f"Request : , \n{request}")                                                                      # 4번 출력
        print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')

        ## 여기에 mysql문으로 불러온 것 필요
        robot_name = request.robot_name

        if robot_name == "Robo1":    
            query = f"SELECT Robot_Name, Status, Estimated_Completion_Time, Battery_Status FROM Robot_manager WHERE Robot_Name = '{robot_name}';"
        else:
            query = f"SELECT Robot_Name, Status, Estimated_Completion_Time, Battery_Status FROM Robot_manager WHERE Robot_Name = '{robot_name}';"
        
        robot_data = self.update_robot_state.loadDataFromDB(query)

        self.get_logger().info(f'Robot Data: {robot_data}')
        
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

        estimated_completion_time = len(Rack_List)
        rack_list_str = str(Rack_List).replace('[', '').replace(']', '').replace("'", "")  # Format Rack_List correctly
        print(estimated_completion_time)
        print(rack_list_str)
        print('################################################################')

        ######## 여기서 Robot_manager 테이블의 Call_Num 읽기 ########
        query = f"SELECT Call_Num FROM Robot_manager WHERE Robot_Name = '{Robot_Name}';"
        current_call_num = self.update_robot_state.loadDataFromDB(query)
        if current_call_num:
            call_num = current_call_num[0][0]
            self.get_logger().info(f"Current Call_Num for {Robot_Name}: {call_num}")
        else:
            call_num = 0 
            self.get_logger().info(f"Default Call_Num for {Robot_Name}")
        ############################################################

        ######## 여기서 Robot_manager 테이블에 업데이트하기  ########
        num = 1 if Robot_Name == 'Robo1' else 2
        call_num += 1
        query = f"""
            UPDATE Robot_manager
            SET
                Num = {num},
                Location_X = 0.0,
                Location_Y = 0.0,
                Rack_List = '{rack_list_str}',
                Status = '작업중',
                Estimated_Completion_Time = {float(estimated_completion_time)},
                Battery_Status = '100%',
                Task_Assignment = '{Task_Assignment}',
                Error_Codes = 'None',
                Call_Num = {call_num},
                Time = NOW()
            WHERE
                Robot_Name = '{Robot_Name}';
        """
        self.update_robot_state.updateData(query)
        self.get_logger().info(f"Succeeding to update in Robot_manager")
        ###########################################################

        ######## 여기서 Task_Manager에게 업데이트됬다는 신호 쏘기  ########
        msg = String()
        msg.data = 'robot_state_updated'
        self.update_robot_state_pub.publish(msg)
        self.get_logger().info(f"Send robot_state_updated to Task Manager")
        self.get_logger().info(f"&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*")
        ############################################################

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
