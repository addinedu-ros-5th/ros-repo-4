#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from task_manager.msg import StartInspection
from modules.esp32_master import ESP32Master
import sqlite3


class MFCNetworkManager(Node):
    def __init__(self):
        super().__init__('mfc_network_manager')
        
        self.subscription = self.create_subscription(
            StartInspection,
            'mfc_start_inspection',
            self.start_inspection_callback,
            10)
        
        self.esp32_master = ESP32Master('192.168.0.12', 80) # 시리얼 통신 클래스 인스턴스 생성


    def start_inspection_callback(self, msg):
        self.get_logger().info(f'Received start inspection signal for {msg.product_code}:{msg.product_name}')
        self.esp32_master.send_signal(f'START_INSPECTION:{msg.product_code}')
    

    def destroy_node(self):
        self.esp32_master.close()
        super().destroy_node()




def main(args=None):
    rclpy.init(args=args)
    MFC_network_manager = MFCNetworkManager()

    try:
        rclpy.spin(MFC_network_manager)
    except KeyboardInterrupt:
        pass

    MFC_network_manager.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
