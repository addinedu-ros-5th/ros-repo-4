#!/usr/bin/env python3
import os
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, QTime, Qt


import mysql.connector as con
import yaml
from threading import Thread
from rclpy.executors import MultiThreadedExecutor

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from modules.signinwindow import *
from modules.mainwindow import *
from modules.node import *

def main(args=None):
    rclpy.init(args=args)
    executor = MultiThreadedExecutor()

    # QApplication 초기화
    app = QApplication(sys.argv)

    # GUI 초기화 및 실행
    main_window = MainWindow()
    main_window.show()

    # InboundNode 초기화
    inbound_node = InboundNode(main_window)
    executor.add_node(inbound_node)

    thread = Thread(target=executor.spin)
    thread.start()

    # Qt 이벤트 루프를 시작
    #sys.exit(app.exec_())
    app.exec_()

    # ROS 종료
    if rclpy.ok():
        rclpy.shutdown()


if __name__ == '__main__':
    main()

