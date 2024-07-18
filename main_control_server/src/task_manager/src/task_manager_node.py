#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from order_list import OrderList  # 임포트 추가
 

import sys
import os


from task_manager.srv import GenerateOrder


class OrderListService(Node):
    def __init__(self):
        super().__init__('order_list_service')
        self.srv = self.create_service(GenerateOrder, 'generate_order', self.generate_order_callback)
        self.order_list_node = OrderList()

    def generate_order_callback(self, request, response):
        random_items = self.order_list_node.get_random_order_list()  # 랜덤 주문 리스트 생성

        response.item_ids = [str(item.item_id) for item in random_items]
        response.names = [item.name for item in random_items]
        response.quantities = [item.quantity for item in random_items]
        response.warehouses = ["A구역" for _ in random_items]  # 임의로 Warehouse 설정
        response.racks = ["A-1" for _ in random_items]  # 임의로 Rack 설정
        response.cells = ["2" for _ in random_items]  # 임의로 Cell 설정
        response.statuses = ["입하완료" for _ in random_items]  # 임의로 Status 설정
        
        self.get_logger().info(f'Received request: {request}')
        self.get_logger().info(f'Sending response: {response}')
        
        return response
    
def main(args=None):
    rclpy.init(args=args)
    order_list_service = OrderListService()

    rclpy.spin(order_list_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()