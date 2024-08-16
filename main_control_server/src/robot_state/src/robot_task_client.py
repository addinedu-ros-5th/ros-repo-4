#!/usr/bin/env python3

import rclpy
import os
import sys
import queue
import yaml
import time
import threading
import mysql.connector as con
from rclpy.node import Node
from rclpy.action import ActionClient
from modules.connect import Connect

# Path Server한테 보내야 하는 메세지 타입
from std_msgs.msg import String
from robot_state.msg import RackList
# Robot_drive에게서 받아야 하는 메세지 타입
from robot_state.msg import GoalStatus
# Task Manager한테 보내야 하는 메세지 타입
from robot_state.msg import TaskProgressUpdate
# Robot_State_Manager 한테 보내야 하는 메세지 타입
from robot_state.msg import AllTaskDone
# Task Manager로부터 받아야 하는 메세지 타입
from task_manager.msg import SendLightOnResults

LIGHT_ON_COMPLETE = False

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
        
class RobotTask:  # new 0807 로봇 별로 관리하겠습니다~
    def __init__(self, robot_name, task_assignment, rack_list):  # new 0807
        self.robot_name = robot_name  # new 0807
        self.task_assignment = task_assignment  # new 0807
        self.rack_list = rack_list  # new 0807
        self.current_index = 0  # new 0807
        self.is_current_one_done = [False] * len(rack_list)  # new 0807
        self.low_battery = False  # new 0807
        self.light_off_COMPLETE = False  # new 0807

    def mark_task_completed(self):  # new 0807
        if self.current_index < len(self.is_current_one_done):  # new 0807
            self.is_current_one_done[self.current_index] = True  # new 0807
            self.current_index += 1  # new 0807

    def all_tasks_completed(self):  # new 0807
        return all(self.is_current_one_done)  # new 0807
    
    def get_current_rack(self):  # new 0807 어느 로봇이 보낸 명령어인지 역추적용도
        if self.current_index < len(self.rack_list):  # new 0807
            return self.rack_list[self.current_index]  # new 0807
        return None  # new 0807
        
class RobotTaskClient(Node):
    def __init__(self):
        super().__init__("robot_task_client")
        # Publisher
        self.publisher_task_complete_results = self.create_publisher(TaskProgressUpdate, 'send_task_complete_results', 10) 
        self.publisher_all_task_done_results = self.create_publisher(AllTaskDone, 'send_all_task_done_results', 10)         # new 0805                                  

        self.battery_publisher1 = self.create_publisher(String, 'go_to_battery_area_1', 10)                                 # new 0804
        self.battery_publisher2 = self.create_publisher(String, 'go_to_battery_area_2', 10)                                 # new 0804

        self.rack_list_publisher1 = self.create_publisher(RackList, 'rack_list_1', 10)
        self.rack_list_publisher2 = self.create_publisher(RackList, 'rack_list_2', 10)

        self.publisher_go_to_outbound1 = self.create_publisher(String, 'go_to_outbound_1', 10)                              # new 0805
        self.publisher_go_to_outbound2 = self.create_publisher(String, 'go_to_outbound_2', 10)                              # new 0805

        self.publisher_light_off1 = self.create_publisher(Bool, 'light_off_1', 10)    #도착했다면 True                         # new 0805
        self.publisher_light_off2 = self.create_publisher(Bool, 'light_off_2', 10)                                           # new 0805

        # Subscriber
        self.goal_status_subscriber = self.create_subscription(GoalStatus, 'goal_status', self.get_result_callback, 10)
        self.goal_status_subscriber

        self.light_off_results_subscriber = self.create_subscription(                                                        # new 0805
            SendLightOffResults, 'send_light_off_results', self.send_light_off_callback, 10)
        self.light_off_results_subscriber

        # DB connection
        self.db_instance = get_mysql_connection()
        self.update_robot_state = UpdateRobotState(self.db_instance)

        # 초기 값 세팅
        self.num = 0
        self.robot_name = "None"
        self.rack_list = []
        self.low_battery = False                                                                                         
        self.light_off_COMPLETE = False   
        self.robot_tasks = {}                                                                                                  # new 0807

    def receive_goal_list(self, robot_name, rack_list, task_assignment):  #개별로봇별로 관리하기 위해 인스턴스 생성
        task = RobotTask(robot_name, task_assignment, rack_list)                                                                # new 0807
        self.robot_tasks[robot_name] = task                                                                                     # new 0807
        self.send_rack_list(task)                                                                                               # new 0807

    def send_rack_list(self, task):
        msg = RackList()
        msg.rack_list = task.rack_list

        if task.task_assignment == "입고":                                                                                                                  
            msg.scenario = False
        else:
            msg.scenario = True

        if self.robot_name == "Robo1":
            self.rack_list_publisher1.publish(msg)
        else:
            self.rack_list_publisher2.publish(msg)

    def go_to_start(self, task):                                # new 0807                                                                                                                          # new 0804
        go_command = String()
        if task.low_battery:                                     # new 0807                                                                                               
            if task.robot_name == "Robo1":
                ############ 'R1' 지점으로 가라는 토픽 publish ########
                go_command.data = "R1"
                self.battery_publisher1.publish(go_command)                     
            else:
                ############ 'R2' 지점으로 가라는 토픽 publish ########
                go_command.data = "R2"
                self.battery_publisher2.publish(go_command)

    def send_light_off_callback(self, msg):                                                                                                   
        if msg.complete == True:
            self.light_off_COMPLETE = True
            self.get_logger().info(f'Received message for light off: {msg.current_rack}, {msg.complete}') 
            self.get_logger().info('-------------------------------------------------------------------------')
            self.get_logger().info(f'light_off_COMPLETE: {self.light_off_COMPLETE}')

    def get_result_callback(self, msg):
        current_rack = msg.current_rack  # new 0807 도착했다는데 어느로봇에서 보냈는지 확인해보자
        robot_name = None  # new 0807

        for name, task in self.robot_tasks.items():  # new 0807
            if current_rack in task.rack_list:  # new 0807
                robot_name = name  # new 0807
                break  # new 0807

        if not robot_name:  # new 0807
            self.get_logger().error(f"Task for rack {current_rack} not found")  # new 0807
            return  # new 0807
        
        task = self.robot_tasks.get(robot_name)  # new 0807

        result = msg.status
        if result == "completed":                                                                                       # new 0805
            self.get_logger().info(f"Result task_complete(T/F): {result}")                                              # 14번 출력 
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!! 여기서 다음 goal_location  보내야 함 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       
            # self.is_current_one_done[self.num] = True
            task.mark_task_completed()                      # new 0807 

            ####################### 여기서 task_manager한테 현재 goal_location에 대해 LED 키라고 보내야 함 ##############
            ####################### & node.py한테도 랙 정보 업데이트 하라고 보내야 함 ##############
            # self.send_task_complete_results()
            self.send_task_complete_results(task)           # new 0807

            ####################### 여기서 DB상의 'Estimated_Completion_Time'열 데이터 1 차감 ########################
            # self.update_estimated_completion_time()         
            self.update_estimated_completion_time(task)     # new 0807                                                                      # new 0801

            # if False in self.is_current_one_done:
            if not task.all_tasks_completed():              # new 0807
                start_time = time.time()
                timeout = 600  # 타임아웃 시간을 600초로 설정    

                # while not self.light_off_COMPLETE:
                while not task.light_off_COMPLETE:            # new 0807
                    if time.time() - start_time > timeout:
                        self.get_logger().error("Timeout waiting for light_off_COMPLETE")
                        break
                    time.sleep(0.1)  

                # if self.light_off_COMPLETE:
                if task.light_off_COMPLETE:                     # new 0807
                    #### send that LIGHT ON SUCCEESS ### 
                    light_off_msg = Bool()
                    self.num += 1
                    light_off_msg.data = task.light_off_COMPLETE

                if self.robot_name == "Robo1":
                    if light_off_msg.data:
                        self.publisher_light_off1.publish(light_off_msg)
                else:
                    if light_off_msg.data:
                        self.publisher_light_off2.publish(light_off_msg)
                # time.sleep(1)
                # self.robot_name = "Debugging"                                                                         
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            else:
                self.publish_result(task, "All done")

                ########## 여기서 task_assignment가 '입고' or '출고' 였는지에 따라 달라질 수도 ##########                      
                # if self.task_assignment == "출고":
                if task.task_assignment == "출고":             
                    ############ 'OB' 지점으로 가라는 토픽 publish ########
                    go_command = String()
                    go_command.data = "OB"

                    # if self.robot_name == "Robo1":
                    if task.robot_name == "Robo1":
                        self.publisher_go_to_outbound1.publish(go_command)
                    else:
                        self.publisher_go_to_outbound2.publish(go_command)
                else:
                    self.get_logger().info(f"배터리 상태 확인 후 다음 명령 받기") 

                self.check_robot_state(task)        # new 0807

    ############################## 여기서 estimated_completion_time response 업데이트 ################
    def update_estimated_completion_time(self, task):  # new 0807                                                                                             
        self.get_logger().info(f"@@@@@@@@@@@@@@@@ UPDATE ESTIMATED_COMPLETION_TIME @@@@@@@@@@@@@@@@")         
        self.get_logger().info(f"Robot Name: {task.robot_name}, Rack List: {task.rack_list}")

        rack_list_str = str(task.rack_list).replace('[', '').replace(']', '').replace("'", "")
        self.get_logger().info(f"Rack List Str: {rack_list_str}")
        query = f"""
                UPDATE Robot_manager
                SET Estimated_Completion_Time = Estimated_Completion_Time - 1,
                    Battery_Status = CONCAT(CAST(CAST(SUBSTRING(Battery_Status, 1, LENGTH(Battery_Status) - 1) AS DECIMAL(5, 0)) - 10 AS CHAR), '%')
                WHERE Robot_Name = '{task.robot_name}'
                    AND Rack_List = '{rack_list_str}'
                    AND Task_Assignment = '{task.task_assignment}'
                    AND Error_Codes = 'None';
                """
        self.update_robot_state.updateData(query)

    def send_task_complete_results(self, task):                             # new 0807
        taskprogress = TaskProgressUpdate()
        taskprogress.robot_name = task.robot_name                           # new 0807
        taskprogress.current_rack = task.rack_list[task.current_index - 1]  # new 0807
        taskprogress.task_complete = task.is_current_one_done[task.current_index - 1]  # new 0807
        # Task Manager 및 node.py 한테 publishing
        self.publisher_task_complete_results.publish(taskprogress)

    def publish_result(self, task, msg):  # new 0807
        allocation_result_msg = AllTaskDone()
        allocation_result_msg.robot_name = task.robot_name  # new 0807
        allocation_result_msg.result_msg = msg  # new 0807
        allocation_result_msg.task_assignment = task.task_assignment  # new 0807
        
        self.publisher_all_task_done_results.publish(allocation_result_msg)
        
 def check_robot_state(self, task):  # new 0807                                                                                     
        ############################# 여기에 'Battery_Status' 20% 이하 찾기 #############################
        rack_list_str = str(task.rack_list).replace('[', '').replace(']', '').replace("'", "")
        query = f"""
                SELECT Robot_Name, Rack_List, Battery_Status
                FROM Robot_manager
                where Robot_Name = '{task.robot_name}' AND Rack_List = '{rack_list_str}';
                """
        robot_data = self.update_robot_state.loadDataFromDB(query)
        r_battery_status = float(robot_data[0][2].rstrip('%'))
        # r_name = robot_data[0][0]
        # r_list = robot_data[0][1]                                                    # new 0804

        if r_battery_status <= 20.0: # 20.0
            task.low_battery = True  # new 0807
            query = f"""
                    UPDATE Robot_manager
                    SET Status = '충전중'
                    WHERE Robot_Name = '{task.robot_name}' AND Rack_List = '{rack_list_str}' AND (Status = '대기중' OR Status = '작업중');
                    """
            self.update_robot_state.updateData(query)
            
            self.go_to_start(task)  # new 0807
            self.get_logger().info("처음 지점으로 이동")
        else:
            self.low_battery = False
