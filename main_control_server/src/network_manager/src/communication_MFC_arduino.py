#!/usr/bin/env python3

import serial
import time
import rclpy
from rclpy.node import Node
from task_manager.msg import StartInspection
import sqlite3


class MFCNetworkManager(Node):
    def __init__(self):
        super().__init__('mfc_network_manager')
        
        self.subscription = self.create_subscription(
            StartInspection,
            'mfc_start_inspection',
            self.start_inspection_callback,
            10)
        
        # self.publisher = self.create_publisher(InspectionComplete, 'inspection_complete', 10)
        
        # self.db_connection = sqlite3.connect('path_to_your_db.db')
        # self.cursor = self.db_connection.cursor()

        # # 아두이노 통신 클래스 인스턴스 저장
        # self.arduino = arduino

    def start_inspection_callback(self, msg):
        self.get_logger().info(f'Received start inspection signal: {msg.signal}')
        
    #     # Inbound_Manager 테이블에서 1행 가져오기
    #     self.cursor.execute("SELECT * FROM Inbound_Manager LIMIT 1")
    #     row = self.cursor.fetchone()
    #     self.get_logger().info(f'Inbound_Manager row: {row}')

    #     # 아두이노에 신호 전송
    #     self.arduino.send_signal("Start Inspection")
        
    #     # 3초 대기 후 검수 완료 신호 전송
    #     time.sleep(3)
    #     self.send_inspection_complete_signal()

    # def send_inspection_complete_signal(self):
    #     msg = InspectionComplete()
    #     msg.signal = "Inspection Complete"
    #     self.publisher.publish(msg)
    #     self.get_logger().info('Published inspection complete signal.')

    def destroy_node(self):
        self.arduino.close()
        super().destroy_node()


# class ArduinoCommunication:
#     def __init__(self, port='/dev/rfcomm0', baud_rate=9600):
#         self.port = port
#         self.baud_rate = baud_rate

#         try:
#             self.ser = serial.Serial(self.port, self.baud_rate)
#             print(f"Connected to {self.port} at {self.baud_rate} baud rate.")
#         except serial.SerialException as e:
#             print(f"Failed to connect to {self.port}: {e}")
#             self.ser = None

#     def send_signal(self, signal_message):
#         if self.ser is not None:
#             try:
#                 self.ser.write((signal_message + '\n').encode('utf-8'))
#                 print(f"Sent to Arduino: {signal_message}")
#             except serial.SerialException as e:
#                 print(f"Failed to send signal to Arduino: {e}")

#     def close(self):
#         if self.ser is not None:
#             self.ser.close()
#             print("Serial port closed.")


def main(args=None):
    rclpy.init(args=args)
    # arduino = ArduinoCommunication()
    MFC_network_manager = MFCNetworkManager()

    try:
        rclpy.spin(MFC_network_manager)
    except KeyboardInterrupt:
        pass

    MFC_network_manager.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
