#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from task_manager.srv import AllocatorTask
from data.location_data import pose_dict, inbound_locations, outbound_locations, product_to_location
import json
class TaskAllocator(Node):
    def __init__(self):
        super().__init__('task_allocator')

        self.task_allocator_service = self.create_service(AllocatorTask, 'allocate_task', self.handle_allocate_task)


    def handle_allocate_task(self, request, response):
        self.get_logger().info(f'Received task allocation request for product: {request.product_code}')
        location_key = product_to_location.get(request.product_code)

        if location_key is None:
            self.get_logger().warn(f'No location found for product code {request.product_code}')
            response.robot_name = ""
            response.goal_location = ""
            response.task_assignment = f"No location found for product code {request.product_code}"
            return response
        
        location_pose = location_key

        if location_pose is None:
            self.get_logger().warn(f'No pose found for location key {location_key}')
            response.robot_name = ""
            response.goal_location = ""
            response.task_assignment = "No pose found"
            return response
        
        self.get_logger().info(f'{request.task_type}: Location for product code {request.product_code} is {location_pose}')
        response.robot_name = "Robo1"
        response.goal_location = location_pose
        response.task_assignment = request.task_type

        return response

        
def main(args=None):
    rclpy.init(args=args)
    task_allocator = TaskAllocator()

    try:
        rclpy.spin(task_allocator)
    except KeyboardInterrupt:
        pass

    task_allocator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
