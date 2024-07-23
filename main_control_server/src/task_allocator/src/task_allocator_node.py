#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from task_manager.srv import AllocatorTask
from data.location_data import pose_dict, inbound_locations, outbound_locations, product_to_location

class TaskAllocator(Node):
    def __init__(self):
        super().__init__('task_allocator')

        self.task_allocator_service = self.create_service(AllocatorTask, 'allocate_task', self.handle_allocate_task)


    def handle_allocate_task(self, request, response):
        self.get_logger().info(f'Received task allocation request for product: {request.product_code}')
        assignment = self.allocate_task(request.product_code, request.task_type)
        response.robot_name = assignment['robot_name']
        response.goal_location = assignment['goal_location']
        response.task_assignment = assignment['task_assignment']
        return response


    def allocate_task(self, product_code, task_type):
        location_key = product_to_location.get(product_code)

        if location_key is None:
            self.get_logger().warn(f'No location found for product code {product_code}')
            return f"No location found for product code {product_code}"
        
        location_pose = location_key

        if location_pose is None:
            self.get_logger().warn(f'No pose found for location key {location_key}')
            return {"robot_name": "", "goal_location": "", "task_assignment": "No pose found"}
        
        self.get_logger().info(f'{task_type}:Location for product code {product_code} is {location_pose}')

        # 작업 할당 정보 생성
        assignment = {
            "robot_name": "Robo1",
            "goal_location": str(location_pose),
            "task_assignment":  str(task_type)
        }
        return assignment

        
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
