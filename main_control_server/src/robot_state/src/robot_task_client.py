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
from std_msgs.msg import String

class RobotTaskClient(Node):
    def __init__(self):
        super().__init__("robot_task_client")
        # Action Client
        self._action_client = ActionClient(self, RobotTask, "robot_action")
        # Publisher
        self.result_publisher = self.create_publisher(String, 'result_topic', 10)

    def send_goal(self, goal_location, robot_name):
        goal_msg = RobotTask.Goal()
        goal_msg.robot_name = robot_name
        goal_msg.goal_location = goal_location

        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callbak)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def feedback_callbak(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f"Received feedback: {feedback.remaining_distance}")
        self.get_logger().info("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal_rejected :(")
            return
        self.get_logger().info("Goal accepted: )")

        self._get_result_futre = goal_handle.get_result_async()
        self._get_result_futre.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        if result.result_msg == 'done':
            self.get_logger().info(f"Result: {result.result_msg}")
            self.publish_result(result.result_msg)

    def publish_result(self, result_msg):
        result = String()
        result.data = result_msg
        self.result_publisher.publish(result)

def main(args=None):
    rclpy.init(args=args)

    client = RobotTaskClient()

    client.send_goal("I1", "Robo1")
    rclpy.spin(client)

if __name__ == "__main__":
    main()
