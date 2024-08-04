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

# Robot에 보내야 하는 메세지 타입
from robot_state.action import RobotTask
# Robot State Manger한테 보내야 하는 메세지 타입
from std_msgs.msg import String
# Task Manager한테 보내야 하는 메세지 타입
from robot_state.msg import TaskProgressUpdate

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
        # Action Client
        self._action_client = ActionClient(self, RobotTask, "robot_action")
        # Publisher
        self.publisher_task_complete_results = self.create_publisher(TaskProgressUpdate, 'send_task_complete_results', 10)
        self.result_publisher = self.create_publisher(String, 'result_topic', 10)

        self.db_instance = get_mysql_connection()
        self.update_robot_state = UpdateRobotState(self.db_instance)

        self.num = 0
        self.robot_name = "None"
        self.rack_list = []

    def receive_goal_list(self, robot_name, rack_list, task_assignment):

        # Rack_List와 동일한 길이의 bool 타입 리스트
        self.is_current_one_done = []
        for _ in range(len(rack_list)):
            self.is_current_one_done.append(False)

        self.robot_name = robot_name
        self.rack_list = rack_list                            
        self.send_goal()

    def send_goal(self):

        goal_msg = RobotTask.Goal() 
        goal_msg.robot_name = self.robot_name
        goal_msg.goal_location = self.rack_list[self.num]       # goal_location 1개 

        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callbak) # 13
        self._send_goal_future.add_done_callback(self.goal_response_callback)                                           # 7 

    def feedback_callbak(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f"Received feedback: {feedback.remaining_distance}")                                      # 13번 출력                 
        self.get_logger().info("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal_rejected :(")
            return
        self.get_logger().info("Goal accepted: )")                                                                      # 7번 출력 

        self._get_result_futre = goal_handle.get_result_async()
        self._get_result_futre.add_done_callback(self.get_result_callback)                                              # 14

    def get_result_callback(self, future):
        result = future.result().result
        if result.task_complete == True:
            self.get_logger().info(f"Result task_complete(T/F): {result.task_complete}")                                # 14번 출력 
            #---------------------------------- 여기서 다음 goal_location  보내야 함 ----------------------------------#       
            self.is_current_one_done[self.num] = True
            ####################### 여기서 task_manager한테 현재 goal_location에 대해 LED 키라고 보내야 함 ##############
            self.send_task_complete_results()
            ####################### 여기서 DB상의 'Estimated_Completion_Time'열 데이터 1 차감 ########################
            self.update_estimated_completion_time()                     # new 0801

            if False in self.is_current_one_done:
                #### send new goal_location ### 
                self.num += 1
                # time.sleep(1)
                # self.robot_name = "Debugging"
                self.send_goal()
            #------------------------------------------------------------------------------------------------------#
            else:
                self.publish_result("All done")

        ## elif result.task_complete == False:
        ##    self.check_robot_state()

    # def check_robot_state(self):
        ## 배터리 상태 체크 -> 20% 이하면 -> self.publish_result("LOW Battery") -> elif (msg.data == "LOW Battery") -> 

    def update_estimated_completion_time(self):                         # new 0801                  
        self.get_logger().info(f"@@@@@@@@@@@@@@@@UPDATE ESTIMATED_COMPLETION_TIME@@@@@@@@@@@@@@@@")         
        self.get_logger().info(f"Robot Name: {self.robot_name}, Rack List: {self.rack_list}")
        
        rack_list_str = str(self.rack_list).replace('[', '').replace(']', '').replace("'", "")  # Format Rack_List correctly
        self.get_logger().info(f"Rack List Str: {rack_list_str}")
        query = f"""
                UPDATE Robot_manager
                SET Estimated_Completion_Time = Estimated_Completion_Time - 1,
                    Battery_Status = CONCAT(CAST(CAST(SUBSTRING(Battery_Status, 1, LENGTH(Battery_Status) - 1) AS DECIMAL(5, 2)) - 20 AS CHAR), '%')
                WHERE Robot_Name = '{self.robot_name}'
                    AND Rack_List = '{rack_list_str}' 
                    AND Error_Codes = 'None';
                """
        self.update_robot_state.updateData(query)

    def send_task_complete_results(self):
        taskprogress = TaskProgressUpdate()
        taskprogress.robot_name = self.robot_name
        taskprogress.current_rack = self.rack_list[self.num] 
        taskprogress.task_complete = self.is_current_one_done[self.num]
        
        self.publisher_task_complete_results.publish(taskprogress)

    def publish_result(self, result_msg):
        result = String()
        result.data = result_msg
        self.result_publisher.publish(result)
        
