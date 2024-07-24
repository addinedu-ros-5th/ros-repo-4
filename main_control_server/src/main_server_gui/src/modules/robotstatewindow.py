#!/usr/bin/env python3
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, QTime, Qt

import mysql.connector as con
import os
import sys
import yaml
import threading
import queue
import rclpy
from rclpy.node import Node
from modules.connect import *
from ament_index_python.packages import get_package_share_directory

# 현재 파일의 디렉토리 경로를 기준으로 network_manager/lib/network_manager 경로를 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../network_manager/lib/network_manager')))
from communication_robot_node import AmclSubscriber 

# 현재 파일의 디렉토리 경로를 기준으로 network_manager/lib/network_manager 경로를 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../robot_state/lib/robot_state')))
from robot_state_manager_node import UpdateRobotState 

# 지도 load
map_yaml_file = os.path.join(get_package_share_directory('main_server_gui'), 'map', 'main.yaml')
#map_yaml_file = os.path.join(get_package_share_directory('main_server_gui'), 'map', 'map_hg.yaml')

def get_mysql_connection():
    try:
        db_instance = Connect("team4", "0444")
        return db_instance
    except con.Error as err:
        print(f"Error: {err}")
        return None
    
class RobotStateWindow(QtWidgets.QDialog):
    def __init__(self, main_window):
        super(RobotStateWindow, self).__init__()
        ui_file = os.path.join(get_package_share_directory('main_server_gui'), 'ui', 'robot_state.ui')
        uic.loadUi(ui_file, self)

        self.db_instance = get_mysql_connection()
        self.main_window = main_window

        self.update_robot_state = UpdateRobotState(self.db_instance)
        self.amcl_subscriber = AmclSubscriber()
        
        # 메인메뉴로 돌아가기 버튼
        self.mainButton_2.clicked.connect(self.go_to_main)
        # spin_thread 실행 상태를 나타내는 플래그
        self.spin_thread_running = False

        self.amcl_pose_queue = queue.Queue()
        
        self.Setup()
        self.start_spin_thread()
        self.Main()
    
    def Main(self):
        query2 = """
            (SELECT * FROM Robot_manager WHERE Robot_Name = 'Robo1' ORDER BY Time DESC LIMIT 1)
            UNION
            (SELECT * FROM Robot_manager WHERE Robot_Name = 'Robo2' ORDER BY Time DESC LIMIT 1);
        """
        self.robot_data = self.update_robot_state.loadDataFromDB(query2)
        self.robot_status_1 = self.robot_data[0][3]
        self.error_codes_1 = self.robot_data[0][6]
        self.robot_status_2 = self.robot_data[1][3]
        self.error_codes_2 = self.robot_data[1][6]

        self.CheckStatusAndBlink()

        self.db_instance.disConnection()

    def CheckStatusAndBlink(self):
        self.setFrameColor(self.robot_status_1, self.error_codes_1, self.frame_robot1)
        self.setFrameColor(self.robot_status_2, self.error_codes_2, self.frame_robot2)

    def setFrameColor(self, status, error_codes, frame):
        if error_codes not in ['None', 'Low Battery']:
            frame.setStyleSheet(f"background-color: {self.level_colors['Yellow']};")
        else:
            if status == '대기중':
                frame.setStyleSheet(f"background-color: {self.level_colors['Default']};")
            elif status == '충전중':
                frame.setStyleSheet(f"background-color: {self.level_colors['Blue']};")
            elif status  == '작업중':
                frame.setStyleSheet(f"background-color: {self.level_colors['Green']};")
            elif status == '충전필요':
                frame.setStyleSheet(f"background-color: {self.level_colors['Red']};")

    def Setup(self):
        # 지도 관련 함수 및 파라미터
        self.find_map_label()
        self.init_map()

        self.map_timer = QTimer(self)
        self.map_timer.timeout.connect(self.update_map)
        self.map_timer.start(200)

        # 시계 타이머 관련 위젯
        self.timer = QTimer(self)
        self.timer.setInterval(1000)    # 1초 간격    
        self.timer.timeout.connect(self.Showtime)
        self.lcdTimer.display('')
        self.lcdTimer.setDigitCount(8)
        self.timer.start()

        # Robot 상태 관련 위젯 및 색상 관련 파라미터
        self.level_colors = {
            "Default" : 'rgba(255, 255, 255, 128)',  # Status: 대기 중 -> Green Off
            "Blue": 'rgba(0, 0, 255, 128)',         # Status: 충전 중 -> Blue on
            "Green": 'rgba(0, 255, 0, 128)',        # Status: 작업 중 -> Green On
            "Red" : 'rgba(255, 0, 0, 128)',         # Status: 충전 필요 -> Red on
            "Yellow" : 'rgba(255, 255, 0, 128)'     # Error_Codes: not None or not Low Battery -> 유지보수필요 -> Yellow On
        }  

    def init_map(self):
        with open(map_yaml_file) as f:
            self.map_yaml_data = yaml.full_load(f)        

        print(self.map.width(), self.map.height())        # 485, 485  <--- from Qt
        print('-----------------------------')

        self.image_scale = 1
        self.pixmap = QPixmap(os.path.join(get_package_share_directory('main_server_gui'), 'map', self.map_yaml_data['image']))
        self.scaled_pixmap = self.pixmap.scaled(int(self.map.width() * self.image_scale), int(self.map.height() * self.image_scale), Qt.KeepAspectRatioByExpanding)#Qt.KeepAspectRatio)
        
        self.height = self.pixmap.size().height()
        self.width = self.pixmap.size().width()

        print(self.width, self.height)                      # 67 99  <--- from PGM file 
        print(self.scaled_pixmap.size())                    # PyQt5.QtCore.QSize(485, 716) = (width, height)
        print('-----------------------------')

        self.map_resolution = self.map_yaml_data['resolution']
        self.map_origin = self.map_yaml_data['origin'][:2]
        print(self.map_origin[0], self.map_origin[1])       # -0.251 -1.82
        print('--------------------------------')
        self.update_map()

    # def init_map(self):
    #     with open(map_yaml_file) as f:
    #         self.map_yaml_data = yaml.full_load(f)        

    #     print(self.map.width(), self.map.height())        # 485, 448
    #     print('-----------------------------')

    #     self.image_scale = 1
    #     self.pixmap = QPixmap(os.path.join(get_package_share_directory('main_server_gui'), 'map', self.map_yaml_data['image']))
    #     self.scaled_pixmap = self.pixmap.scaled(int(self.map.width() * self.image_scale), int(self.map.height() * self.image_scale), Qt.KeepAspectRatioByExpanding)#Qt.KeepAspectRatio)
        
    #     self.height = self.pixmap.size().height()
    #     self.width = self.pixmap.size().width()

    #     print(self.scaled_pixmap.size())                    # PyQt5.QtCore.QSize(485, 448) = (width, height)
    #     print(self.width, self.height)                      # 105 97
    #     print('-----------------------------')

    #     self.map_resolution = self.map_yaml_data['resolution']
    #     self.map_origin = self.map_yaml_data['origin'][:2]
    #     self.update_map()

    def update_map(self):
        self.scaled_pixmap = self.pixmap.scaled(int(self.map.width() * self.image_scale), int(self.map.height() * self.image_scale), Qt.KeepAspectRatioByExpanding)#Qt.KeepAspectRatio)
        painter = QPainter(self.scaled_pixmap)

        # 로봇 번호 표시
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(13)
        painter.setFont(self.font)

        # 1번 로봇 좌표
        try:
            amcl_1 = self.amcl_pose_queue.get_nowait()
            #position = amcl_1.pose.pose.position
            #orientation = amcl_1.pose.pose.orientation
            # print("It's from robotstatewindow.py")
            # print(f"Position(x: {position.x}, y: {position.y}, z: {position.z})")
            # print(f'Orientation(x: {orientation.x}, y: {orientation.y}, z: {orientation.z}, w: {orientation.w})')
            # print('RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')
        except queue.Empty:
            amcl_1 = None

        if amcl_1:
            self.draw_robot(painter, amcl_1, Qt.red, '1')

        painter.end()
        self.map.setPixmap(self.scaled_pixmap)

    def draw_robot(self, painter, amcl, color, label):
        x, y = self.calc_grid_position(amcl.pose.pose.position.x, amcl.pose.pose.position.y)
        #x, y = self.calc_grid_position(0.0, 0.0) # test용
        painter.setPen(QPen(color, 13, Qt.SolidLine))
        painter.drawPoint(int((self.width - x) * self.image_scale), int(y * self.image_scale))
        painter.drawText(int((self.width - x) * self.image_scale - 30), int(y * self.image_scale + 5), label)

    # def calc_grid_position(self, x, y):
    #     x_offset = -85
    #     y_offset = 85
    #     x_grid = x_offset + ((x * 3.2 - self.map_origin[0]) / 0.05 )
    #     y_grid = y_offset + ((y * 3.0 - self.map_origin[1]) / 0.05 )

    #     return x_grid, y_grid

    def calc_grid_position(self, x, y):
        # 맵의 해상도 (meters/pixel)
        resolution = self.map_resolution  # 예: 0.05

        # 맵의 원점 (meters)
        origin_x = self.map_origin[0]  # 예: -0.251
        origin_y = self.map_origin[1]  # 예: -1.82

        # 실제 좌표를 픽셀 좌표로 변환
        x_grid = (x - origin_x) / resolution
        y_grid = (y - origin_y) / resolution

        return x_grid, y_grid
    
    def find_map_label(self):
        self.map_label = self.findChild(QtWidgets.QLabel, 'map')
        if self.map_label:
            print('QLabel "map" found.')
        else:
            print('QLabel "map" not found.')    

    def Showtime(self):
        # 시간
        sender = self.sender()
        currentTime = QTime.currentTime().toString("hh:mm:ss")
        if id(sender) == id(self.timer):
            self.lcdTimer.display(currentTime)

    def go_to_main(self):
        self.main_window.show()
        self.close()

    def start_spin_thread(self):
        if not self.spin_thread_running:
            # 별도의 스레드에서 rclpy.spin_once 호출
            self.spin_thread_running = True
            self.spin_thread = threading.Thread(target=self.spin_loop, daemon=True)
            self.spin_thread.start()

    def spin_loop(self):
        while rclpy.ok():
            rclpy.spin_once(self.amcl_subscriber)
            amcl_1 = self.amcl_subscriber.get_amcl_pose()
            self.amcl_pose_queue.put(amcl_1)