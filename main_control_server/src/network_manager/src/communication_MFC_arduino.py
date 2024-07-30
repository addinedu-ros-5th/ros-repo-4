#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from task_manager.msg import StartInspection, InspectionComplete, SendAllocationResults
from modules.esp32_master import ESP32Master
import sqlite3
import socket
import threading
import os
import signal

class MFCNetworkManager(Node):
    def __init__(self):
        super().__init__('mfc_network_manager')
        
        self.subscription = self.create_subscription(
            StartInspection,
            'mfc_start_inspection',
            self.start_inspection_callback,
            10)
        #192.168.0.9 쬰지네
        #172.30.1.77 탐탐
        #192.168.2.56 학원
            #192.168.0.21 학원2
        #192.168.1.44 건대 카공
        #172.30.1.87 건대 카공

        self.esp32_master = ESP32Master('172.20.10.5', 80) # 시리얼 통신 클래스 인스턴스 생성
        self.receive_inspection_server_thread = threading.Thread(target=self.receive_inspection_server)
        self.receive_inspection_server_thread.start()

        self.inspection_complete_publisher = self.create_publisher(InspectionComplete, 'inspection_complete', 10)

        self.allocation_results_subscription = self.create_subscription(
            SendAllocationResults,
            'send_allocation_results',
            self.task_assignment_callback,
            10)


    def start_inspection_callback(self, msg):
        self.get_logger().info(f'Received start inspection signal for {msg.product_code}:{msg.product_name}')
        self.esp32_master.send_signal(f'START_INSPECTION:{msg.product_code}')

    def receive_inspection_server(self):
        self.check_and_close_existing_socket('172.20.10.4', 12345)
        #192.168.0.15 쬰지네
        #172.30.1.28 탐탐
        #192.168.2.28 학원1
            #192.168.0.89 학원2
        #192.168.1.40 건대카공
        #커피랑도서관
        receive_inspection_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        receive_inspection_server_socket.bind(('172.20.10.4', 12345))  # 서버 IP와 포트 설정 ifconfig러 확인하기
        receive_inspection_server_socket.listen(5)
        self.get_logger().info('Server listening on port 12345')

        while True:
            client_socket, addr = receive_inspection_server_socket.accept()
            self.get_logger().info(f'Connected by {addr}')
            data = client_socket.recv(1024).decode()
            self.get_logger().info(f'Received: {data}')
            if data.startswith("result-"):
                product_code = data.split(':')[1]
                self.handle_task_complete(product_code)
            client_socket.close()
    
    def handle_task_complete(self, product_code):
        self.get_logger().info(f'Task complete for product: {product_code}')
        msg = InspectionComplete()
        msg.product_code = product_code
        self.inspection_complete_publisher.publish(msg)


    def check_and_close_existing_socket(self, host, port):
        # netstat 명령어를 사용하여 포트 사용 여부 확인
        cmd = f"lsof -i tcp:{port} -sTCP:LISTEN"
        result = os.popen(cmd).read()
        if result:
            # 포트를 사용하는 프로세스가 있으면 해당 프로세스 종료
            for line in result.splitlines():
                if 'python' in line:
                    pid = int(line.split()[1])
                    os.kill(pid, signal.SIGKILL)
                    self.get_logger().info(f'Killed process {pid} using port {port}')

    def task_assignment_callback(self, msg):
        rack_list = msg.rack_list  # 예: RA-1,RA-2,RA-3
        task_assignment = msg.task_assignment  # 예: 입고
        # ESP32 마스터 보드에 명령 보내기
        # command = f'START-{task_assignment}:{rack_list[0]}'
        # self.esp32_master.send_signal(command)
        # self.get_logger().info(f'Sent command to ESP32: {command}')



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
