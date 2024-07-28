#!/usr/bin/env python3
import sys
import os
import threading
import queue
import time

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor

from modules.connect import *
from robot_task_client import RobotTaskClient

# 서비스 서버
from robot_state.srv import UpdateDB
# Task Manager로부터 오는 메세지 타입
from task_manager.msg import SendAllocationResults

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

## Version 1.
Robot_Name = "Debugging"
Goal_Location = "Debugging"
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
        
    def update_db_callback(self, request, response):
        # 디버깅용
        print(f"Request : , \n{request}")
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
        global isTaskAssigned
        global Robot_Name
        global Goal_Location
        global Task_Assignment
        
        self.get_logger().info(f'Received task assignment for robot: {msg.robot_name}')
        self.get_logger().info(f'Goal Location: {msg.goal_location}')
        self.get_logger().info(f'Task Assignment: {msg.task_assignment}')
        ##############################여기 아래에 robot_name & goal_location 전달##############################
        
        isTaskAssigned = True
        Robot_Name = msg.robot_name
        Goal_Location = msg.goal_location
        Task_Assignment = msg.task_assignment
        
        print(f"It's in TellTaskManager")
        print(Robot_Name, Goal_Location, Task_Assignment)
        print('################################################################')

def main(args=None):
    global Robot_Name
    global Goal_Location
    global isTaskAssigned

    rclpy.init(args=args)
    executor = MultiThreadedExecutor()

    node1 = MFCRobotManager()
    node2 = RobotTaskClient()

    executor.add_node(node1)
    executor.add_node(node2)

    print("Update 전 초기값")
    print(Robot_Name, Goal_Location, Task_Assignment)
    print('################################################################')
    
    try:
        while rclpy.ok():
            executor.spin_once(timeout_sec=0.1)
            if isTaskAssigned:
                node2.send_goal(Goal_Location, Robot_Name)
                # Send goal only once
                isTaskAssigned = False
        print("Update 후")
        print(Robot_Name, Goal_Location, Task_Assignment)
        print('################################################################')
    finally:
        executor.shutdown()
        node1.destroy_node()
        node2.destroy_node()
        rclpy.shutdown()
# ----------------------------------------------------------------------------------------------------------------------------
## Version 2.
## 'task_assignment_callback' 호출될 때마다 다른 'msg.robot_name' 등 보내기
# class MFCRobotManager(Node):
#     def __init__(self, node2):
#         super().__init__('mfc_robot_manager')
#         self.db_instance = get_mysql_connection()
#         self.update_robot_state = UpdateRobotState(self.db_instance)
#         self.node2 = node2

#         # 'UpdateDb' 메세지 타입 서비스 서버
#         self.server = self.create_service(UpdateDB, 'update_db', self.update_db_callback)
#         # 'SendAllocationResults' 메세지 타입 subscriber
#         self.allocation_results_sub = self.create_subscription(
#             SendAllocationResults,
#             'send_allocation_results',
#             self.task_assignment_callback,
#             10)
        
#     def update_db_callback(self, request, response):
#         # 디버깅용
#         print(f"Request : , \n{request}")
#         print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')

#         ## 여기에 mysql문으로 불러온 것 필요
#         robot_name = request.robot_name

#         # timestamp 기준으로 각 로봇 최신 상태 대한 query문  
#         query = f"SELECT Robot_Name, Status, Battery_Status FROM Robot_manager WHERE Robot_Name = '{robot_name}' ORDER BY Time DESC LIMIT 1;"
             
#         robot_data = self.update_robot_state.loadDataFromDB(query)
#         self.db_instance.disConnection()

#         response.robot_name = robot_data[0][0]
#         response.status = robot_data[0][1]
#         response.battery_status = robot_data[0][2]
   
#         return response

#     def task_assignment_callback(self, msg):
#         self.get_logger().info(f'Received task assignment for robot: {msg.robot_name}')
#         self.get_logger().info(f'Goal Location: {msg.goal_location}')
#         self.get_logger().info(f'Task Assignment: {msg.task_assignment}')

#         # goal을 보내기 위해 node2 사용
#         self.node2.send_goal(msg.goal_location, msg.robot_name)
        
#         print(f"It's in TellTaskManager")
#         print(msg.robot_name, msg.goal_location, msg.task_assignment)
#         print('################################################################')

# def main(args=None):
#     rclpy.init(args=args)
#     executor = MultiThreadedExecutor()

#     node2 = RobotTaskClient()
#     node1 = MFCRobotManager(node2)

#     executor.add_node(node1)
#     executor.add_node(node2)
    
#     try:
#         executor.spin()
#     finally:
#         executor.shutdown()
#         node1.destroy_node()
#         node2.destroy_node()
#         rclpy.shutdown()

if __name__ == '__main__':
    main()
