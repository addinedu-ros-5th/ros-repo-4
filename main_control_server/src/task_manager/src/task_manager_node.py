#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from order_list import OrderList  # 임포트 추가
from task_manager.msg import DbUpdate 
from task_manager.msg import StartInspection
from task_manager.srv import GenerateOrder

class OrderListService(Node):
    def __init__(self):
        super().__init__('order_list_service')
        self.srv = self.create_service(GenerateOrder, 'generate_order', self.generate_order_callback)
        self.order_list_node = OrderList()
        self.inspection_started = False  # 플래그 변수 초기화

        self.subscription = self.create_subscription(
            DbUpdate,
            'db_update_status',
            self.db_update_callback,
            10)
        self.subscription 

        self.publisher = self.create_publisher(StartInspection, 'mfc_start_inspection', 10)

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

    def db_update_callback(self, msg):
        self.get_logger().info(f'Received DB update status: {msg.status}')
        if msg.status == "DB Update Completed" and not self.inspection_started:
            self.send_signal_start_inspection_to_mfc("Start Inspection")
            

    def send_signal_start_inspection_to_mfc(self, signal_message):
        self.inspection_started = True  # 신호 전송 후 플래그 설정
        msg = StartInspection()
        msg.signal = signal_message
        self.publisher.publish(msg)
        self.get_logger().info('Sending inspection start signal.')

def main(args=None):
    rclpy.init(args=args)
    order_list_service = OrderListService()

    rclpy.spin(order_list_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
