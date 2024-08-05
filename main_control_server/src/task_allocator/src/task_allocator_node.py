#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from task_manager.srv import AllocatorTask
from data.location_data import pose_dict, inbound_locations, outbound_locations, product_to_location
import json

# string task_code                # new           # "Task_2"
# string[] product_code_list      # new           # ['P01', 'P05', 'P09']
# string task_type

class TaskAllocator(Node):
    def __init__(self):
        super().__init__('task_allocator')

        self.task_allocator_service = self.create_service(AllocatorTask, 'allocate_task', self.handle_allocate_task)


    def handle_allocate_task(self, request, response):
        self.get_logger().info(f'Received task allocation request for product: {request.product_code_list}')
        product_code_list = request.product_code_list
        rack_list = []

        for product_code in product_code_list:
            location_key = product_to_location.get(product_code)

            if location_key is None:
                self.get_logger().warn(f'No location found for product code {product_code}')
                continue
            
            rack_list.append(location_key)

        if not rack_list:
            response.robot_name = ""
            response.task_code = request.task_code
            response.rack_list = []
            response.task_assignment = f"No valid locations found for product codes {product_code_list}"
            return response
        
        self.get_logger().info(f'{request.task_type}: Locations for product codes {product_code_list} are {rack_list}')
        response.robot_name = "Robo2"#"Robo1"
        response.task_code = request.task_code
        response.rack_list = rack_list
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
