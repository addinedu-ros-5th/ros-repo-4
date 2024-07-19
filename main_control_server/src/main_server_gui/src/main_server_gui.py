#!/usr/bin/env python3
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, QTime, Qt

import mysql.connector as con
import yaml
import threading
import os
import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from task_manager.srv import GenerateOrder

from ament_index_python.packages import get_package_share_directory

from modules.connect import *
from modules.robotstatewindow import *
from modules.signinwindow import *
from modules.mainwindow import *
from modules.node import *


def main(args=None):
    rclpy.init(args=args)

    # QApplication 초기화
    app = QApplication(sys.argv)

    # GUI 초기화 및 실행
    main_window = MainWindow()
    main_window.show()

    robot_state_window = RobotStateWindow(main_window)
    # InboundNode 초기화
    inbound_node = InboundNode(main_window)
    
    # AmclSubscriber 초기화
    amcl_node = AmclSubscriber(robot_state_window)

    # ROS 노드를 별도의 스레드에서 스핀
    def spin_node(node):
        try:
            rclpy.spin(node)
        except KeyboardInterrupt:
            print(f"Keyboard interrupt received, shutting down {node.get_name()}.")
            node.destroy_node()
        except Exception as e:
            print(f"Exception in node {node.get_name()}: {e}")

    inbound_thread = threading.Thread(target=spin_node, args=(inbound_node,))
    amcl_thread = threading.Thread(target=spin_node, args=(amcl_node,))

    inbound_thread.start()
    amcl_thread.start()

    # Qt 이벤트 루프를 시작
    sys.exit(app.exec_())

    # ROS 종료
    if rclpy.ok():
        rclpy.shutdown()

    # 스레드 종료 대기
    inbound_thread.join()
    amcl_thread.join()

if __name__ == '__main__':
    main()
