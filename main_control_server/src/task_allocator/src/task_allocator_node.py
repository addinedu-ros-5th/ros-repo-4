#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from task_manager.srv import AllocatorTask
from data.location_data import pose_dict, inbound_locations, outbound_locations, product_to_location
import json

# string task_code                # new           # "Task_2"
# string[] product_code_list      # new           # ['P01', 'P05', 'P09']
# string task_type

## Version 1. 수정 후 버전
# ---------------------------------------------------------------------------------------------------------------
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
        response.robot_name = "Robo1"
        response.task_code = request.task_code
        response.rack_list = rack_list
        response.task_assignment = request.task_type

        return response
# ---------------------------------------------------------------------------------------------------------------
## Version 2. 수정 전 버전
# class TaskAllocator(Node):
#     def __init__(self):
#         super().__init__('task_allocator')

#         self.task_allocator_service = self.create_service(AllocatorTask, 'allocate_task', self.handle_allocate_task)

#     def handle_allocate_task(self, request, response):
#         self.get_logger().info(f'Received task allocation request for task: {request.task_code}')
#         assignment = self.allocate_task(request.task_code, request.product_code_list, request.task_type)
#         response.robot_name = assignment['robot_name']
#         response.task_code = assignment['task_code']
#         response.rack_list = assignment['rack_list']
#         response.task_assignment = assignment['task_assignment']

#         return response

#     def allocate_task(self, task_code, product_code_list, task_type):
#         # 여기 수정해야함!!!
#         location_key = [] 
#         for i in range(len(product_code_list)):
#             location_key.append(product_to_location.get(product_code_list[i]))

#         if len(location_key) == 0:
#             self.get_logger().warn(f'No location found for task code {task_code}')
#             return f"No location found for task code {task_code}"
        
#         location_pose = location_key

#         if len(location_pose) == 0:
#             self.get_logger().warn(f'No pose found for location key {location_key}')
#             return {"robot_name": "", "task_code": "", "rack_list": "", "task_assignment": "No pose found"}
        
#         self.get_logger().info(f'{task_type}:Location for task code {task_code} is {location_pose}')

#         # 작업 할당 정보 생성 -> Response 값들
#         assignment = {
#             "robot_name": "Robo1",
#             "task_code": "Task_2",                  # task_code
#             "rack_list": location_pose,             # rack_list      # ["R_A1", "R_B2", "R_C3"]
#             "task_assignment": "입고"                # task_assignment
#         }

#         return assignment
 # ---------------------------------------------------------------------------------------------------------------
           
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
