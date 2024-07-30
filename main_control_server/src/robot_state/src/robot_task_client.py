#!/usr/bin/env python3

import rclpy
import os
import sys
import queue
import threading
from rclpy.node import Node
from rclpy.action import ActionClient
# Robot에 보내야 하는 메세지 타입
from robot_state.action import RobotTask
# Task Manager한테 보내야 하는 메세지 타입
from robot_state.msg import TaskProgressUpdate
from std_msgs.msg import String


class RobotTaskClient(Node):
    def __init__(self):
        super().__init__("robot_task_client")
        # Action Client
        self._action_client = ActionClient(self, RobotTask, "robot_action")
        # Publisher
        self.publisher_task_complete_results = self.create_publisher(TaskProgressUpdate, 'send_task_complete_results', 10)
        
        self.num = 0
        self.robot_name = "None"
        self.rack_list = []

    def receive_goal_list(self, robot_name, rack_list):

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
            ####################### 여기서 task_manager한테 현재 goal_location에 대해 LED 키라고 보내야 함 #########################
            self.send_task_complete_results()
            ################################################################################################################
            if False in self.is_current_one_done:
                #### send new goal_location ### 
                self.num += 1
                #self.robot_name = "Debugging"
                self.send_goal()
            #------------------------------------------------------------------------------------------------------#
            else:
                self.publish_result("All done")

    def send_task_complete_results(self):
        taskprogress = TaskProgressUpdate()
        taskprogress.robot_name = self.robot_name
        taskprogress.current_rack = self.rack_list[self.num] 
        taskprogress.task_complete = self.is_current_one_done[self.num]
        
        self.publisher_task_complete_results.publish(taskprogress)

    def publish_result(self, result_msg):
        result = String()
        result.data = result_msg
        # self.result_publisher.publish(result)
        
