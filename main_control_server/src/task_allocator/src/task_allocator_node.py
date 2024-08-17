#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from task_manager.srv import AllocatorTask
from data.location_data import pose_dict, inbound_locations, outbound_locations, product_to_location
from module.TSP_Algorithms import *
import json

class TaskAllocator(Node):
    def __init__(self):
        super().__init__('task_allocator')
        self.task_allocator_service = self.create_service(AllocatorTask, 'allocate_task', self.handle_allocate_task)

    def handle_allocate_task(self, request, response):
        self.get_logger().info(f'Received task allocation request for product: {request}')
        product_code_list = request.product_code_list
        task_code = request.task_code

        # 로봇 정보 구성
        robots = {}
        for i in range(len(request.robot_name)):
            robots[request.robot_name[i]] = {
                'battery_level': int(request.battery_status[i].replace('%', '')),
                'status': request.status[i],
                'total_workload': int(float(request.estimated_completion_time[i].split(',')[0])) if request.estimated_completion_time[i] else 0
            }
            
        rack_list = [product_to_location[product_code] for product_code in product_code_list]
        
        # Define tasks
        tasks = {task_code: product_code_list}
        
        # Check if specific task codes should be assigned to specific robots
        if task_code == 'Task_1':
            response.robot_name = 'Robo1'
        elif task_code == 'Task_2' or task_code == 'Task_3':
            response.robot_name = 'Robo2'
        else:
            task_allocations = auction_based_task_allocation(tasks, robots)
            if not task_allocations:
                response.robot_name = ""
                response.task_code = request.task_code
                response.rack_list = []
                response.task_assignment = f"No valid locations found for product codes {product_code_list}"
                
                return response
            
            allocation = task_allocations[0]  # 요청이 하나일 것이므로 첫 번째 할당만 사용~~
            response.robot_name = allocation["robot_name"]

        response.task_code = request.task_code
        response.rack_list = rack_list
        response.task_assignment = request.task_type
        self.get_logger().info(f'Assigned task {task_code} to {response.robot_name} with racks {rack_list}')
        
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
