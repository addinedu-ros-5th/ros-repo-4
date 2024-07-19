#!/usr/bin/env python3
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, QTime, Qt

from modules.connect import *

import mysql.connector as con
import os
import yaml

from ament_index_python.packages import get_package_share_directory

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped 

global amcl_1
amcl_1 = PoseWithCovarianceStamped()

# 지도 load
map_yaml_file = os.path.join(get_package_share_directory('main_server_gui'), 'map', 'main.yaml')

def get_mysql_connection():
    try:
        db_instance = Connect("team4", "0444")
        return db_instance
    except con.Error as err:
        print(f"Error: {err}")
        return None
    
class UpdateRobotState():
    def __init__(self, db_instance):
        self.cursor = db_instance.cursor

    # 데이터베이스에서 테이블 정보를 가져오는 함수 정의
    def fetchImageDataQuery(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def loadDataFromDB(self, query):
        image_data = self.fetchImageDataQuery(query)
        print(image_data)
        print('(((((((((((((((((((())))))))))))))))))))')

class RobotStateWindow(QtWidgets.QDialog):
    def __init__(self, main_window):
        super(RobotStateWindow, self).__init__()
        ui_file = os.path.join(get_package_share_directory('main_server_gui'), 'ui', 'robot_state.ui')
        uic.loadUi(ui_file, self)

        db_instance = get_mysql_connection()
        self.main_window = main_window
        self.update_robot_state = UpdateRobotState(db_instance)
        
        self.mainButton_2.clicked.connect(self.go_to_main)
        self.Setup()
        #self.Main()
    
    # def Main(self):
    #     # Case 1.
    #     query_A = "SELECT id, name, state, battery_level, last_updated FROM Robot_State WHERE name = 'Robot_A'"
    #     self.update_robot_state.loadDataFromDB(query_A)

    #     # Case 2.
    #     query_B = "SELECT id, name, state, battery_level, last_updated FROM Robot_State WHERE name = 'Robot_B'"
    #     self.update_robot_state.loadDataFromDB(query_B)

    def Setup(self):
        # 지도 관련 함수 및 파라미터
        self.find_map_label()
        self.init_map()

        self.map_timer = QTimer(self)
        self.map_timer.timeout.connect(self.update_map)
        self.map_timer.start(200)

        # # 시계 타이머 관련 위젯
        # self.timer = QTimer(self)
        # self.timer.setInterval(1000)    # 1초 간격    
        # self.timer.timeout.connect(self.Showtime)
        # self.lcdTimer.display('')
        # self.lcdTimer.setDigitCount(8)
        # self.timer.start()
    
    def init_map(self):
        with open(map_yaml_file) as f:
            self.map_yaml_data = yaml.full_load(f)        

        print(self.map.width(), self.map.height())        # 485, 448
        print('-----------------------------')

        self.image_scale = 1
        self.pixmap = QPixmap(os.path.join(get_package_share_directory('main_server_gui'), 'map', self.map_yaml_data['image']))
        self.scaled_pixmap = self.pixmap.scaled(int(self.map.width() * self.image_scale), int(self.map.height() * self.image_scale), Qt.KeepAspectRatioByExpanding)#Qt.KeepAspectRatio)
        
        self.height = self.pixmap.size().height()
        self.width = self.pixmap.size().width()

        print(self.scaled_pixmap.size())                    # PyQt5.QtCore.QSize(485, 448) = (width, height)
        print(self.width, self.height)                      # 105 97
        print('-----------------------------')

        self.map_resolution = self.map_yaml_data['resolution']
        self.map_origin = self.map_yaml_data['origin'][:2]
        self.update_map()

    def update_map(self):
        self.scaled_pixmap = self.pixmap.scaled(int(self.map.width() * self.image_scale), int(self.map.height() * self.image_scale), Qt.KeepAspectRatioByExpanding)#Qt.KeepAspectRatio)
        painter = QPainter(self.scaled_pixmap)

        # 로봇 번호 표시
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(13)
        painter.setFont(self.font)

        # 1번 로봇 좌표
        self.draw_robot(painter, amcl_1, Qt.red, '1')

        painter.end()
        self.map.setPixmap(self.scaled_pixmap)

    def draw_robot(self, painter, amcl, color, label):
        x, y = self.calc_grid_position(amcl.pose.pose.position.x, amcl.pose.pose.position.y)
        # x, y = self.calc_grid_position(0.0, 0.0) # test용
        painter.setPen(QPen(color, 13, Qt.SolidLine))
        painter.drawPoint(int((self.width - x) * self.image_scale), int(y * self.image_scale))
        painter.drawText(int((self.width - x) * self.image_scale - 30), int(y * self.image_scale + 5), label)

    def calc_grid_position(self, x, y):
        x_offset = -85
        y_offset = 85
        x_grid = x_offset + ((x * 3.2 - self.map_origin[0]) / 0.05 )
        y_grid = y_offset + ((y * 3.0 - self.map_origin[1]) / 0.05 )

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

    def update_amcl_pose(self, amcl_pose):
        print("Received AMCL Pose in RobotStateWindow:", amcl_pose)
        #우선 합니다~