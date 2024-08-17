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
import time
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from modules.connect import *
from ament_index_python.packages import get_package_share_directory

# 현재 파일의 디렉토리 경로를 기준으로 network_manager/lib/network_manager 경로를 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../network_manager/lib/network_manager')))
from communication_robot_node import AmclSubscriber1, AmclSubscriber2 

# 지도 파일 경로
map_yaml_file = os.path.join(get_package_share_directory('main_server_gui'), 'map', 'mfc_map.yaml')

# 전역 변수 설정
init_pos_x = 0
init_pos_y = 0
robot_position1 = [init_pos_x,init_pos_y]  # 로봇의 초기 위치(position_x, position_y)
# robot_position2 = [init_pos_x,init_pos_y]  # 로봇의 초기 위치(position_x, position_y)

def get_mysql_connection():
    try:
        db_instance = Connect("root", "0")                                 # new 0807
        return db_instance
    except con.Error as err:
        print(f"Error: {err}")
        return None    

class UpdateRobotState():
    def __init__(self, db_instance):
        self.cursor = db_instance.cursor
        self.conn = db_instance.conn

        if not self.conn or not self.cursor:
            self.get_logger().error("Failed to connect to the database")
            return
    
    # 데이터베이스에서 테이블 정보를 가져오는 함수 정의
    def fetchDataQuery(self, query):
        self.cursor.execute(query)

        return self.cursor.fetchall()

    def loadDataFromDB(self, query):
        robot_data = self.fetchDataQuery(query)
        return robot_data
    
    def updateData(self, query):
        self.cursor.execute(query)
        self.conn.commit()
    
class RobotStateWindow(QtWidgets.QDialog):
    def __init__(self, main_window):
        super(RobotStateWindow, self).__init__()
        ui_file = os.path.join(get_package_share_directory('main_server_gui'), 'ui', 'robot_state.ui')
        uic.loadUi(ui_file, self)

        self.db_instance = get_mysql_connection()
        self.main_window = main_window

        self.update_robot_state = UpdateRobotState(self.db_instance)
        self.amcl_subscriber1 = AmclSubscriber()
        #self.amcl_subscriber2 = AmclSubscriber()
        
        # 메인메뉴로 돌아가기 버튼
        self.mainButton_2.clicked.connect(self.go_to_main)
        # spin_thread 실행 상태를 나타내는 플래그
        self.spin_thread_running = False

        self.amcl_pose_queue = queue.Queue()
        self.Setup()
        self.start_spin_thread()
        # 새로 고침 버튼
        self.i = 0
        self.resetButton.clicked.connect(self.get_data_from_table)
    
    def get_data_from_table(self):
        # 'Robot_manager' 테이블 데이터 업로드
        self.ShowRobotTable()
        # 로봇 상태 버튼 창
        self.ShowRobotBtn()
        ## 'Inbound_Manager' 테이블 데이터 업로드
        #self.ShowInboundTable()                                                     # new 0807

    def ShowRobotTable(self):        
        # 'Robot_manager' 테이블 데이터 업로드
        query = "SELECT Robot_Name, Rack_List, Status, Estimated_Completion_Time, Battery_Status, Task_Assignment FROM Robot_manager;"
        robot_data = self.update_robot_state.loadDataFromDB(query)
        
        # Robot_Name을 키로 사용하여 로봇 정보를 저장할 딕셔너리 생성
        robot_dict = {}
        for row in robot_data:
            robot_dict[row[0]] = row

        # TableWidget 초기화
        self.tableWidget.setRowCount(0)

        # 딕셔너리의 로봇 정보로 테이블 업데이트
        for Robot_Name, robotInfo in robot_dict.items():
            Rack_List = robotInfo[1]
            Status = robotInfo[2] 
            Estimated_Completion_Time = robotInfo[3]
            Battery_Status = robotInfo[4]
            Task_Assignment = robotInfo[5]

            # 로그인에서 입력 받은 데이터 home.ui TableWidget에 보이기
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(Robot_Name))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(Rack_List))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(Status))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(Estimated_Completion_Time)))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(Battery_Status))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(Task_Assignment))

    def ShowRobotBtn(self):
        #  로봇 상태 버튼 창
        query = "SELECT Status, Call_Num FROM Robot_manager;"
        robot_data = self.update_robot_state.loadDataFromDB(query)
        print(f'robot_data: {robot_data}')
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        self.robot_status_1 = robot_data[0][0]
        self.call_num_1 = robot_data[0][1]
        # self.robot_status_2 = robot_data[1][0]
        # self.call_num_2 = robot_data[1][1]

        self.CheckStatusAndBlink()

    def CheckStatusAndBlink(self):
        self.setFrameColor(self.robot_status_1, self.error_codes_1, self.frame_robot1)
        # self.setFrameColor(self.robot_status_2, self.error_codes_2, self.frame_robot2)

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

        # 이미지 불러오기
        with open(map_yaml_file) as f:
            self.map_yaml_data = yaml.full_load(f)   
        self.pixmap = QPixmap(os.path.join(get_package_share_directory('main_server_gui'), 'map', self.map_yaml_data['image']))

        # UI로부터 맵 크기 불러오기
        print(self.map.width(), self.map.height())        # 380, 190  <--- from Qt
        print('-----------------------------')

        # 이미지 크기 가져오기
        self.height = self.pixmap.size().height()
        self.width = self.pixmap.size().width()
        print(self.width, self.height)                      # 38 76  <--- from PGM file 
        print('-----------------------------')

        # map resolution 및 origin 설정
        self.map_resolution = self.map_yaml_data['resolution']
        self.map_origin = self.map_yaml_data['origin'][:2]

        print(self.map_origin[0], self.map_origin[1])       # -0.461 -1.85
        print('--------------------------------')

        # 이미지 스케일 설정
        self.image_scale = 12
        
        # 이미지 변환 (-90도 회전)
        transform = QTransform().rotate(-90)
        rotated_pixmap = self.pixmap.transformed(transform)
        
        # 이미지 이동 설정 
        translated_pixmap = QPixmap(rotated_pixmap.size())         # 동일한 크기의 빈 'translated_pixmap'
        self.painter = QPainter(translated_pixmap)
        move_x = 0      
        move_y = 0      
        self.painter.drawPixmap(move_x, -move_y, rotated_pixmap)    # x 좌표를 -로 설정하여 왼쪽으로 이동
        self.painter.end()
        
        # QLabel 크기에 맞게 이미지 조정 및 설정
        scaled_pixmap = translated_pixmap.scaled(self.width * self.image_scale, self.height * self.image_scale, Qt.KeepAspectRatio)
        self.map_label.setPixmap(scaled_pixmap)

        self.update_map()

    def update_map(self):
        global robot_position1

        # 기존 pixmap을 기반으로 QPixmap 생성
        updated_pixmap = QPixmap(self.map_label.pixmap())
        self.painter = QPainter(updated_pixmap)

        # 로봇 번호 표시
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(13)
        self.painter.setFont(self.font)

        # 1번 로봇 좌표
        try:
            amcl_1 = self.amcl_pose_queue.get_nowait()

            position = amcl_1.pose.pose.position
            orientation = amcl_1.pose.pose.orientation

            robot_position1[0] = position.x
            robot_position1[1] = position.y

            print("It's from robotstatewindow.py")
            print(f"Position(x: {robot_position1[0]}, y: {robot_position1[1]}, z: {position.z})")
            print(f'Orientation(x: {orientation.x}, y: {orientation.y}, z: {orientation.z}, w: {orientation.w})')
            print('RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')

        except queue.Empty:
            amcl_1 = None

        # amcl_pose subscribe 후
        if amcl_1:
            self.draw_robot(Qt.red, '1')
        # amcl_pose subscribe 전
        else:
            self.draw_robot(Qt.green, '1', initial=True)

        # QPainter 종료
        self.painter.end()
        # QLabel에 업데이트된 pixmap 설정
        self.map_label.setPixmap(updated_pixmap)

    def draw_robot(self, color, label):
        global robot_position1
        x, y = self.calc_grid_position(robot_position1[0], robot_position1[1])

        # 로봇 번호 표시
        self.painter.setPen(QPen(color, 13, Qt.SolidLine))
        # x와 y를 스왑하고 y 좌표를 반전시켜서 올바른 방향으로 그리기
        self.painter.drawPoint(self.map_label.pixmap().height() - y + 190, self.map_label.pixmap().height() - x)
        self.painter.drawText(self.map_label.pixmap().height() - y +180, self.map_label.pixmap().height() - x - 10, label)

    def calc_grid_position(self, x, y):
        # print("변환 전\n")
        # print(x, y)
        # print('**************************')

        pos_x = ((x - self.map_origin[0]) / self.map_resolution) * 5
        pos_y = ((y - self.map_origin[1]) / self.map_resolution) * 5

        # print("변환 후\n")
        # print(pos_x, pos_y)

        return int(pos_x), int(pos_y)
    
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
            rclpy.spin_once(self.amcl_subscriber1)
            amcl_1 = self.amcl_subscriber1.get_amcl_pose()
            self.amcl_pose_queue1.put(amcl_1)
