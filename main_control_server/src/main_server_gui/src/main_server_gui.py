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

from modules.connect import Connect
from modules.robotstatewindow import *
from modules.signinwindow import *


# 지도 load
map_yaml_file = os.path.join(get_package_share_directory('main_server_gui'), 'map', 'main.yaml')

def get_mysql_connection():
    try:
        db_instance = Connect("team4", "0444")
        return db_instance
    except con.Error as err:
        print(f"Error: {err}")
        return None

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, node, username=''):
        super(MainWindow, self).__init__()

        self.node = node
        self.inbound_management_active = False  # 입고처리관리 플래그

        ui_file = os.path.join(get_package_share_directory('main_server_gui'), 'ui', 'window2.ui')
        print(f"Loading UI file from: {ui_file}")  # 디버깅 출력
        uic.loadUi(ui_file, self)

        self.username = username
        self.treeWidget.itemClicked.connect(self.handle_tree_item_click)
        self.signinButton.clicked.connect(self.open_signin_window)
        self.logoutButton.clicked.connect(self.handle_logout)
        # self.statusButton.clicked.connect(self.update_status)
        self.update_ui_for_logged_in_user()
        # self.statusButton.hide()

        # 각종 창 인스턴스 변수
        self.robot_state_window = None      

        # Start 버튼 및 QTimeEdit 초기화
        self.startButton.clicked.connect(self.toggleClock)
        self.startButton.setEnabled(False)  
        self.timeEdit.setTime(QTime(7, 55))
        self.timeEdit.setEnabled(False)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateClock)

        self.schedule_timer = QTimer(self)
        self.schedule_timer.timeout.connect(self.check_schedule)
        self.schedule_timer.start(1000)  # 1초마다 스케줄 체크(바꿔야하나?)
       
    def toggleClock(self):
        if self.startButton.text() == 'Start':
            self.startClock()
        else:
            self.stopClock()

    def startClock(self):
        self.time = self.timeEdit.time()
        self.timer.start(100)  # 100ms마다 updateClock 호출
        self.updateClock()
        self.startButton.setText('Close')

    def stopClock(self):
        self.timer.stop()
        self.startButton.setText('Start')
        self.timeEdit.setTime(QTime(7, 55))

    def updateClock(self):
        self.time = self.time.addSecs(10) # 10초씩 증가 현실보다 100배 빠르게 증가
        self.timeEdit.setTime(self.time)

    def check_schedule(self):
        current_time = self.timeEdit.time()
        if current_time.hour() == 8 and current_time.minute() == 0:
            self.request_inbound_list()

    def request_inbound_list(self):
        self.node.get_logger().info('Requesting inbound list')
        self.node.request_inbound_list()

    def display_inbound_list(self, inbound_list):
        self.update_inbound_list(inbound_list)
        if self.inbound_management_active:
            self.show_inbound_management()

    def update_inbound_list(self, inbound_list):

        db_instance = get_mysql_connection()
        if db_instance:
            try:
                # 외래 키 제약 조건 비활성화
                db_instance.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
                
                # 기존 데이터 삭제
                delete_query = "DELETE FROM Inbound_Manager"
                db_instance.cursor.execute(delete_query)
                
                # 외래 키 제약 조건 다시 활성화
                db_instance.cursor.execute("SET FOREIGN_KEY_CHECKS=1")

                # 새로운 데이터 삽입
                for idx, item in enumerate(inbound_list, start=1):
                    insert_query = ("INSERT INTO Inbound_Manager (No, Product_Code, Product_Name, Warehouse, Rack, Cell, Receiving_Quantity, Status) "
                                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
                    data = (idx, item['item_id'], item['name'], item['warehouse'], item['rack'], item['cell'], item['quantity'], item['status'])
                    db_instance.cursor.execute(insert_query, data)
                
                db_instance.conn.commit()
                db_instance.disConnection()
            except con.Error as err:
                print(f"Error: {err}")
                db_instance.disConnection()

    def handle_tree_item_click(self, item, column):
        if not self.username:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 후에 진행해 주세요.')
            return
        
        table_name = self.get_table_name(item)
        self.statusButton.setProperty('table_name', table_name)
        parent = item.parent()
        if parent is None:
            self.statusButton.hide()
            if item.text(0) == '재고 관리':
                self.show_inventory_management()
                self.inbound_management_active = False

            elif item.text(0) == '창고별 재고현황':
                self.show_warehouse_status()
                self.inbound_management_active = False

            elif item.text(0) == '입고처리관리':
                self.show_inbound_management()
                self.statusButton.show()
                self.inbound_management_active = True

            elif item.text(0) == '출고처리관리':
                self.show_outbound_management()
                self.statusButton.show()
                self.inbound_management_active = False

            elif item.text(0) == "관제 및 로봇 상태 관리":
                self.show_robotstate_management() 
        else:
            self.statusButton.hide()
            grandparent = parent.parent()
            if grandparent is None:
                self.show_filtered_by_warehouse(item.text(0), table_name)
            else:
                great_grandparent = grandparent.parent()
                if great_grandparent is None:
                    self.show_filtered_by_warehouse_and_rack(parent.text(0), item.text(0), table_name)
                else:
                    self.show_filtered_by_warehouse_rack_and_cell(grandparent.text(0), parent.text(0), item.text(0), table_name)

    def open_signin_window(self):
        self.hide()
        self.signin_window = SigninWindow(self)
        self.signin_window.show()

    def handle_logout(self):
        self.username = ''
        self.update_ui_for_logged_in_user()
        self.reset_ui_to_initial_state()

    def update_ui_for_logged_in_user(self):
        if self.username:
            self.userEdit.setText(self.username)
            self.userEdit.show()
            self.logoutButton.show()
            self.signinButton.hide()
            self.startButton.setEnabled(True)
            self.timeEdit.setEnabled(True)

        else:
            self.userEdit.hide()
            self.logoutButton.hide()
            self.signinButton.show()
            self.startButton.setEnabled(False)
            self.timeEdit.setEnabled(False)

    def reset_ui_to_initial_state(self):
        self.userEdit.clear()
        self.userEdit.hide()
        self.signinButton.show()
        self.logoutButton.hide()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.statusButton.hide()
        self.show()

    def get_table_name(self, item):
        root = item
        while root.parent():
            root = root.parent()
        if root.text(0) == '창고별 재고현황':
            return 'rack_manager'
        elif root.text(0) == '입고처리관리':
            return 'Inbound_Manager'
        elif root.text(0) == '출고처리관리':
            return 'Outbound_manager'
        return None
    
    def fetch_inbound_table_data(self):
        db_instance = get_mysql_connection()
        if db_instance:
            try:
                db_instance.cursor.execute("SELECT * FROM Inbound_Manager")
                data = db_instance.cursor.fetchall()
                db_instance.disConnection()
                return data
            except con.Error as err:
                print(f"Error: {err}")
                db_instance.disConnection()
                return None
            
    def populate_table_widget(self, data, table_name):
        # Clear the tableWidget
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

        if not data:
            return

        # Set the number of rows and columns
        num_rows = len(data)
        num_columns = len(data[0])
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_columns)

        # Set the table headers
        column_names = [desc[0] for desc in self.fetch_column_names(table_name)]
        self.tableWidget.setHorizontalHeaderLabels(column_names)


        # Populate the table with data
        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

    def fetch_column_names(self, table_name):
        db_instance = get_mysql_connection()
        if db_instance:
            try:
                db_instance.cursor.execute(f"SHOW COLUMNS FROM {table_name}")
                columns = db_instance.cursor.fetchall()
                db_instance.disConnection()
                return columns
            except con.Error as err:
                print(f"Error: {err}")
                db_instance.disConnection()
                return None

    def show_inventory_management(self):
        # Load and show the inventory management screen
        pass

    def show_warehouse_status(self):
        if not self.username:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 후에 진행해 주세요.')
            return
        
    def show_inbound_management(self):
        if not self.username:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 후에 진행해 주세요.')
            return

        data = self.fetch_inbound_table_data()
        if data:
            self.populate_table_widget(data, 'Inbound_Manager')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'No data found in Inbound_Manager')

    def show_outbound_management(self):
        if not self.username:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 후에 진행해 주세요.')
            return

        data = self.fetch_outbound_table_data()
        if data:
            self.populate_table_widget(data, 'Outbound_manager')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'No data found in Outbound_manager')

    def show_robotstate_management(self):
        if self.robot_state_window is None:
            self.robot_state_window = RobotStateWindow(self)
        self.robot_state_window.show()
        self.close()

class InboundNode(Node):
    def __init__(self,app):
        super().__init__('inbound_node')
        self.client = self.create_client(GenerateOrder, 'generate_order')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

        self.get_logger().info('Service available, ready to send request.')

        self.app = app
        self.window = MainWindow(self)
        self.window.show()

        self.app.aboutToQuit.connect(self.shutdown_ros)

    def run(self):
        self.app.exec_()

    def shutdown_ros(self):
        print("Shutting down ROS...")
        rclpy.shutdown()

    def close_gui(self):
        self.window.close()

    def request_inbound_list(self):
        if not self.client:
            self.get_logger().error('Client not initialized')
            return

        request = GenerateOrder.Request()
        # request 필드를 설정

        try:
            future = self.client.call_async(request)
            future.add_done_callback(self.inbound_list_callback)
            self.get_logger().info('Async request sent')
        except Exception as e:
            self.get_logger().error(f'Failed to send async request: {e}')

    def inbound_list_callback(self, future):
        self.get_logger().info('inbound_list_callback called')
        try:
            response = future.result()
            self.get_logger().info(f'Received response: {response}')
            inbound_list = [{
                "item_id": response.item_ids[i],
                "name": response.names[i],
                "quantity": response.quantities[i],
                "warehouse": response.warehouses[i],
                "rack": response.racks[i],
                "cell": response.cells[i],
                "status": response.statuses[i]
            } for i in range(len(response.item_ids))]
            self.get_logger().info(f'Parsed inbound list: {inbound_list}')
            self.window.display_inbound_list(inbound_list)
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

class AmclSubscriber(Node):
    def __init__(self):
        super().__init__('amcl_subscriber')

        self.pose1_sub = self.create_subscription(PoseWithCovarianceStamped, 'amcl_pose', self.amcl_callback1, 10)

    def amcl_callback1(self, amcl):
        global amcl_1
        amcl_1 = amcl
        print(amcl_1)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

def main(args=None):
    rclpy.init(args=args)
    
    app = QApplication([])
    inbound_node = InboundNode(app)
    amcl_node = AmclSubscriber()

    # rclpy 스핀을 별도의 스레드에서 실행하는 함수 정의
    def spin_node(node):
        try:
            rclpy.spin(node)
        except KeyboardInterrupt:
            print(f"Keyboard interrupt received, shutting down {node.get_name()}.")
            node.destroy_node()

    inbound_thread = threading.Thread(target=spin_node, args=(inbound_node,))
    amcl_thread = threading.Thread(target=spin_node, args=(amcl_node,))

    inbound_thread.start()
    amcl_thread.start()

    app.exec_()# Qt 이벤트 루프를 시작

    if rclpy.ok():
        rclpy.shutdown()

    inbound_thread.join()
    amcl_thread.join()

if __name__ == '__main__':
    main()
