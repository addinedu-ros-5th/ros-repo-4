#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import sys
import os
from modules.connect import *
# 서비스 서버
from robot_state.srv import UpdateDB
from task_manager.msg import SendAllocationResults
from std_msgs.msg import String


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

        self.server = self.create_service(UpdateDB, 'update_db', self.callback_service)

        self.allocation_results_subscription = self.create_subscription(
            SendAllocationResults,
            'send_allocation_results',
            self.task_assignment_callback,
            10)
        
        self.publisher_pose_commands = self.create_publisher(String, 'pose_commands', 10)

    def callback_service(self, request, response):
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
        self.get_logger().info(f'Received task assignment for robot: {msg.robot_name}')
        self.get_logger().info(f'Goal Location: {msg.goal_location}')
        self.get_logger().info(f'Task Assignment: {msg.task_assignment}')

        pose_command = String()
        pose_command.data = msg.goal_location
        self.publisher_pose_commands.publish(pose_command)
        self.get_logger().info(f'Published pose command: {pose_command.data}')
    
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

    rclpy.init(args=args)
    node = TellTaskManager()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()