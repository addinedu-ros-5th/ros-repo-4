#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
import threading
from ament_index_python.packages import get_package_share_directory
import os
import sys

# 현재 파일의 경로를 기준으로 상대 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '../../../task_manager/lib'))

from task_manager.order_list import OrderListNode

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        # UI 파일 로드
        ui_file = os.path.join(get_package_share_directory('main_server_gui'), 'ui', 'main_window.ui')
        print(f"Loading UI file from: {ui_file}")  # 디버깅 출력
        uic.loadUi(ui_file, self)

        # UI 요소 접근
        self.label = self.findChild(QLabel, 'label')  # Qt Designer에서 설정한 객체 이름
        self.update_button = self.findChild(QPushButton, 'update_button')
        self.inventory_text = self.findChild(QTextEdit, 'inventory_text')

        # 버튼 클릭 이벤트 연결
        if self.update_button:  # update_button이 None이 아닌지 확인
            self.update_button.clicked.connect(self.update_inventory)
        else:
            print("update_button not found in the UI file")

    def update_inventory(self):
        print(current_dir)
        self.inventory_text.append("Updating inventory...")
        order_list_node = OrderListNode()
        random_order_list = order_list_node.get_random_order_list()
        print(random_order_list)
        order_list_str = "\n".join([f"Item ID: {item.item_id}, Name: {item.name}, Quantity: {item.quantity}" for item in random_order_list])
        msg = String()
        msg.data = order_list_str
        self.inventory_text.append(order_list_str)

class GUINode(Node):
    def __init__(self):
        super().__init__('gui_node')
        self.publisher_ = self.create_publisher(String, 'order_list', 10)
        
        self.app = QApplication([])
        self.window = MainWindow()
        self.window.show()

        # PyQt 애플리케이션 종료 시 rclpy도 종료
        self.app.aboutToQuit.connect(self.shutdown_ros)

    def shutdown_ros(self):
        print("Shutting down ROS...")
        rclpy.shutdown()

    def close_gui(self):
        self.window.close()

def main(args=None):
    rclpy.init(args=args)
    gui_node = GUINode()

    # rclpy 스핀을 별도의 스레드에서 실행
    def ros_spin():
        try:
            rclpy.spin(gui_node)
        except KeyboardInterrupt:
            print("Keyboard interrupt received, shutting down.")
            gui_node.destroy_node()
            rclpy.shutdown()
            # PyQt 애플리케이션 종료
            gui_node.close_gui()
            gui_node.app.quit()

    ros_spin_thread = threading.Thread(target=ros_spin)
    ros_spin_thread.start()

    gui_node.app.exec_()

    # Ensure ROS is shut down when the PyQt application exits
    if rclpy.ok():
        rclpy.shutdown()
    ros_spin_thread.join()

if __name__ == '__main__':
    main()
