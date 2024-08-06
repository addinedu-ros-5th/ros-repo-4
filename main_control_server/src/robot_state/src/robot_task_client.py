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

        self.publisher_light_on1 = self.create_publisher(String, 'light_on_1', 10)                                           # new 0805
        self.publisher_light_on2 = self.create_publisher(String, 'light_on_2', 10)                                           # new 0805

        # Subscriber
        self.goal_status_subscriber = self.create_subscription(GoalStatus, 'goal_status', self.get_result_callback, 10)
        self.goal_status_subscriber

        self.light_on_results_subscriber = self.create_subscription(                                                        # new 0805
            SendLightOnResults, 'send_light_on_results', self.send_light_on_callback, 10)
        self.light_on_results_subscriber

        # DB connection
        self.db_instance = get_mysql_connection()
        self.update_robot_state = UpdateRobotState(self.db_instance)

        # 초기 값 세팅
        self.num = 0
        self.robot_name = "None"
        self.rack_list = []
        self.low_battery = False                                                                                         # new 0804

    def receive_goal_list(self, robot_name, rack_list, task_assignment):

        # Rack_List와 동일한 길이의 bool 타입 리스트
        self.is_current_one_done = []
        for _ in range(len(rack_list)):
            self.is_current_one_done.append(False)

        self.robot_name = robot_name
        self.rack_list = rack_list  
        self.task_assignment = task_assignment                          
        self.send_rack_list()


    def send_rack_list(self):
        msg = RackList()
        msg.rack_list = self.rack_list

        if self.robot_name == "Robo1":
            self.rack_list_publisher1.publish(msg)
        else:
            self.rack_list_publisher2.publish(msg)

    def go_to_start(self):                                                                                               # new 0804
        go_command = String()
        if self.low_battery:                                                                                        
            if self.robot_name == "Robo1":
                ############ 'R1' 지점으로 가라는 토픽 publish ########
                go_command.data = "R1"
                self.battery_publisher1.publish(go_command)                           # !!!!!!!!!중요!!!!!!!!! 이거 토픽 or 서비스 중 뭐야하나
            else:
                ############ 'R2' 지점으로 가라는 토픽 publish ########
                go_command.data = "R2"
                self.battery_publisher2.publish(go_command)

    def send_light_on_callback(self, msg):   
        global LIGHT_ON_COMPLETE                                                                                          # new 0805
                                            
        self.get_logger().info(f'Received message for light on: {msg.current_rack}, {msg.complete}') 
        
        if msg.complete == True:
            LIGHT_ON_COMPLETE = True

        self.get_logger().info(f'LIGHT_ON_COMPLETE: {LIGHT_ON_COMPLETE}')

    def get_result_callback(self, msg):
        global LIGHT_ON_COMPLETE

        result = msg.status
        if result == "completed":                                                                                       # new 0805
            self.get_logger().info(f"Result task_complete(T/F): {result}")                                              # 14번 출력 
            #------------------!!!!!!!!!!!! 여기서 다음 goal_location  보내야 함 !!!!!!!!!!!!------------------------#       
            self.is_current_one_done[self.num] = True
            ####################### 여기서 task_manager한테 현재 goal_location에 대해 LED 키라고 보내야 함 ##############
            self.send_task_complete_results()
            ####################### 여기서 DB상의 'Estimated_Completion_Time'열 데이터 1 차감 ########################
            self.update_estimated_completion_time()                                                                     # new 0801

            if False in self.is_current_one_done:
                start_time = time.time()
                timeout = 10  # 타임아웃 시간을 10초로 설정                                                                   # new 0805
                while not LIGHT_ON_COMPLETE:
                    if time.time() - start_time > timeout:
                        self.get_logger().error("Timeout waiting for LIGHT_ON_COMPLETE")
                        break
                    time.sleep(0.1)  

                if LIGHT_ON_COMPLETE:
                    #### send that LIGHT ON SUCCEESS ### 
                    self.num += 1
                    light_on_msg = String()
                    if self.robot_name == "Robo1":
                        light_on_msg.data = "light on1"
                        self.publisher_light_on1.publish(light_on_msg)
                    else:
                        light_on_msg.data = "light on2"
                        self.publisher_light_on2.publish(light_on_msg)
                    # time.sleep(1)
                    # self.robot_name = "Debugging"                                                                     # new 0805
            #-----------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!------------------------------#
            else:
                self.publish_result("All done")
                ########## 여기서 task_assignment가 '입고' 였는지 '출고' 였는지에 따라 달라질 수도 ##########                      
                if self.task_assignment == "출고":                                                                       # new 0805
                    ############ 'OB' 지점으로 가라는 토픽 publish ########
                    go_command = String()
                    go_command.data = "OB"
                    if self.robot_name == "Robo1":
                        self.publisher_go_to_outbound1.publish(go_command)
                    else:
                        self.publisher_go_to_outbound2.publish(go_command)
                else:
                    self.get_logger().info(f"배터리 상태 확인 후 다음 명령 받기")
                self.check_robot_state()                                                                                # new 0804

    ############################## 여기서 estimated_completion_time response 업데이트 ################
    def update_estimated_completion_time(self):                                                                         # new 0801                  
        self.get_logger().info(f"@@@@@@@@@@@@@@@@UPDATE ESTIMATED_COMPLETION_TIME@@@@@@@@@@@@@@@@")         
        self.get_logger().info(f"Robot Name: {self.robot_name}, Rack List: {self.rack_list}")
        
        rack_list_str = str(self.rack_list).replace('[', '').replace(']', '').replace("'", "")  # Format Rack_List correctly
        self.get_logger().info(f"Rack List Str: {rack_list_str}")
        query = f"""
                UPDATE Robot_manager
                SET Estimated_Completion_Time = Estimated_Completion_Time - 1,
                    Battery_Status = CONCAT(CAST(CAST(SUBSTRING(Battery_Status, 1, LENGTH(Battery_Status) - 1) AS DECIMAL(5, 2)) - 10 AS CHAR), '%')
                WHERE Robot_Name = '{self.robot_name}'
                    AND Rack_List = '{rack_list_str}'
                    AND Task_Assignment = '{self.task_assignment}'
                    AND Error_Codes = 'None';
                """
        self.update_robot_state.updateData(query)

    def send_task_complete_results(self):
        taskprogress = TaskProgressUpdate()
        taskprogress.robot_name = self.robot_name
        taskprogress.current_rack = self.rack_list[self.num] 
        taskprogress.task_complete = self.is_current_one_done[self.num]
        
        self.publisher_task_complete_results.publish(taskprogress)

    def publish_result(self, msg):
        allocation_result_msg = AllTaskDone()
        allocation_result_msg.robot_name = self.robot_name
        allocation_result_msg.result_msg = msg
        allocation_result_msg.task_assignment = self.task_assignment
        
        self.publisher_all_task_done_results.publish(allocation_result_msg)
        
    def check_robot_state(self):                                                                                        # new 0804
        ## 1. 배터리 상태 체크 --> '20%' 이하면 --> 
        ##      --> Status: '대기중' or '작업중' => '충전중' --> 충전 or 시작 구역으로 이동 
        ##      --> ... 
        ##      --> 1초 후 '10%' --> Esimated_Completion_Time != 0 & Status = '충전중'
        ##                              --> Status: '충전중' => '작업중' --> 남은 Esimated_Completion_Time !=0 인 것 먼저 처리

        ############################# 여기에 'Battery_Status' 20% 이하 찾기 #############################
        rack_list_str = str(self.rack_list).replace('[', '').replace(']', '').replace("'", "")  
        query = f"""
                SELECT Robot_Name, Rack_List, Battery_Status
                FROM Robot_manager
                where Robot_Name = '{self.robot_name}' AND Rack_List = '{rack_list_str}';
                """
        robot_data = self.update_robot_state.loadDataFromDB(query)
        # r_name = robot_data[0][0]
        # r_list = robot_data[0][1]
        r_battery_status = robot_data[0][2]
        r_battery_status = float(r_battery_status.rstrip('%'))                                                          # new 0804

        if r_battery_status <= 60.0: # 20.0
            self.low_battery = True
            query = f"""
                    UPDATE Robot_manager
                    SET Status = '충전중'
                    WHERE Robot_Name = '{self.robot_name}' AND Rack_List = '{rack_list_str}' AND (Status = '대기중' OR Status = '작업중');
                    """
            self.update_robot_state.updateData(query)
            
            self.go_to_start()  # send goal to START
        else:
            self.low_battery = False
