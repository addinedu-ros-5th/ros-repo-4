#!/usr/bin/env python3

import sys
import os
import rclpy
import queue
from rclpy.node import Node
from rclpy.action import ActionClient
from robot_state.action import RobotTask            # 사용자 정의된 로봇(액션 클라이언트)과 액션 통신 메세지 타입.

class MFCRobotClient(Node):

    def __init__(self):
        super().__init__('mfc_robot_action_client')
        self._action_client = ActionClient(self, RobotTask, 'mfc_robot')
    
    def send_goal(self, robot_name, goal_location):
        goal_msg = RobotTask.Goal()
        goal_msg.robot_name = robot_name
        goal_msg.goal_location = goal_location

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return
        
        self.get_logger().info('Goal accepted :)')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Result: {result.done}')
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f'Received feedback: {feedback_msg.remained_dist}')

def main(args=None):
    rclpy.init(args=args)
    action_client = MFCRobotClient()

    # 여기에 로봇 이름과 목표 위치를 입력합니다.
    robot_name = 'Robo1'
    goal_location = 'I1'

    action_client.send_goal(robot_name, goal_location)

    rclpy.spin(action_client)

if __name__ == '__main__':
    main()
