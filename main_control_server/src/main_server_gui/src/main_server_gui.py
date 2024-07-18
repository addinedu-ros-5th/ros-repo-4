#!/usr/bin/env python3

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, QTime, Qt

from connect import Connect
import mysql.connector as con

import threading
import rclpy
import os
import sys

from rclpy.node import Node
from std_msgs.msg import String
from ament_index_python.packages import get_package_share_directory

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '../../../task_manager/share'))
from task_manager.srv import GenerateOrder


def get_mysql_connection():
    try:
        db_instance = Connect("team4", "0444")
        return db_instance
    except con.Error as err:
        print(f"Error: {err}")
        return None

class SigninWindow(QtWidgets.QDialog):
    def __init__(self, main_window):
        super(SigninWindow, self).__init__()
        ui_file = os.path.join(get_package_share_directory('main_server_gui'), 'ui', 'signin.ui')
        print(f"Loading UI file from: {ui_file}")  # 디버깅 출력
        uic.loadUi(ui_file, self)
        
        self.main_window = main_window
        
        self.loginButton.clicked.connect(self.handle_login)
        self.signupButton.clicked.connect(self.handle_signup)
        self.mainButton_l.clicked.connect(self.go_to_main)
        
        self.radioButton_1.toggled.connect(self.toggle_radio_buttons)
        self.radioButton_2.toggled.connect(self.toggle_radio_buttons)
        
        self.radioButton_1.setChecked(True)
        self.groupBox.setVisible(True)
        self.groupBox_2.setVisible(False)


    def toggle_radio_buttons(self):
        if self.radioButton_1.isChecked():
            self.groupBox.setVisible(True)
            self.groupBox_2.setVisible(False)
        else:
            self.groupBox.setVisible(False)
            self.groupBox_2.setVisible(True)

    def handle_signup(self):
        name = self.usernameEdit_2.text()
        user_id = self.passwordEdit_2.text()
        password = self.passwordEdit_3.text()
        
        if not name or not user_id or not password:
            QtWidgets.QMessageBox.warning(self, 'Error', 'All fields are required')
            return
        
        if self.save_user(name, user_id, password):
            QtWidgets.QMessageBox.information(self, 'Success', 'User created successfully')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'User creation failed')
    
    def handle_login(self):
        user_id = self.usernameEdit.text()
        password = self.passwordEdit.text()
        
        user = self.authenticate_user(user_id, password)
        if user:
            self.main_window.username = user[0]  # Assuming user[0] is the name
            self.main_window.update_ui_for_logged_in_user()
            self.main_window.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Invalid username or password')

    def save_user(self, name, user_id, password):
        db_instance = get_mysql_connection()
        if db_instance:
            try:
                db_instance.cursor.execute("INSERT INTO user_manager (name, ID, password) VALUES (%s, %s, %s)", (name, user_id, password))
                db_instance.conn.commit()
                db_instance.disConnection()
                return True
            except con.Error as err:
                print(f"Error: {err}")
                db_instance.disConnection()
                return False
        else:
            return False

    def authenticate_user(self, user_id, password):
        db_instance = get_mysql_connection()
        if db_instance:
            try:
                db_instance.cursor.execute("SELECT name FROM user_manager WHERE ID = %s AND password = %s", (user_id, password))
                user = db_instance.cursor.fetchone()
                db_instance.disConnection()
                return user
            except con.Error as err:
                print(f"Error: {err}")
                db_instance.disConnection()
                return None
        else:
            return None

    def go_to_main(self):
        self.main_window.show()
        self.close()
    
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, username=''):
        super(MainWindow, self).__init__()
        # UI 파일 로드

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
        # self.robot_state_window = None      # RobotStateWindow 인스턴스 저장용 변수

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
       
    
        self.node = rclpy.create_node('gui_client_node')
        self.client = self.node.create_client(GenerateOrder, 'generate_order')


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
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.node.get_logger().info('service not available, waiting again...')
        
        request = GenerateOrder.Request()
        self.node.get_logger().info(f'Sending request: {request}')  # 요청 데이터 출력
        future = self.client.call_async(request)
        future.add_done_callback(self.inbound_list_callback)

    def inbound_list_callback(self, future):
        try:
            response = future.result()
            self.node.get_logger().info(f'Received response: {response}')  # 응답 데이터 출력
            inbound_list = [{
                "item_id": response.item_ids[i],
                "name": response.names[i],
                "quantity": response.quantities[i],
                "warehouse": response.warehouses[i],
                "rack": response.racks[i],
                "cell": response.cells[i],
                "status": response.statuses[i]
            } for i in range(len(response.item_ids))]
            self.node.get_logger().info(f'Parsed inbound list: {inbound_list}')  # 파싱된 데이터 출력
            # self.update_inbound_list(inbound_list)
        except Exception as e:
            self.node.get_logger().error(f'Service call failed: {e}')


    # def update_inbound_list(self, inbound_list):

    #     db_instance = get_mysql_connection()
    #     if db_instance:
    #         try:
    #             # 기존 데이터 삭제
    #             delete_query = "DELETE FROM Inbound_manager"
    #             db_instance.cursor.execute(delete_query)
                
    #             # 새로운 데이터 삽입
    #             for idx, item in enumerate(inbound_list, start=1):
    #                 insert_query = ("INSERT INTO Inbound_manager (Purchase_Number, Product_Code, Product_Name, Warehouse, Rack, Cell, Receiving_Quantity, Status) "
    #                                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    #                 data = (idx, item['item_id'], item['name'], item['warehouse'], item['rack'], item['cell'], item['quantity'], item['status'])
    #                 db_instance.cursor.execute(insert_query, data)
                
    #             db_instance.conn.commit()
    #             db_instance.disConnection()
    #         except con.Error as err:
    #             print(f"Error: {err}")
    #             db_instance.disConnection()


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
            elif item.text(0) == '창고별 재고현황':
                self.show_warehouse_status()
            elif item.text(0) == '입고처리관리':
                self.show_inbound_management()
                self.statusButton.show()
            elif item.text(0) == '출고처리관리':
                self.show_outbound_management()
                self.statusButton.show()
            elif item.text(0) == "관제 및 로봇 상태 관리":
                self.open_robot_state_window() 
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
            return 'Inbound_manager'
        elif root.text(0) == '출고처리관리':
            return 'Outbound_manager'
        return None
    
    def fetch_inbound_table_data(self):
        db_instance = get_mysql_connection()
        if db_instance:
            try:
                db_instance.cursor.execute("SELECT * FROM Inbound_manager")
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

    def show_inbound_management(self):
        if not self.username:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 후에 진행해 주세요.')
            return

        data = self.fetch_inbound_table_data()
        if data:
            self.populate_table_widget(data, 'Inbound_manager')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'No data found in Inbound_manager')


class GUINode(Node):
    def __init__(self):
        super().__init__('gui_node')
        # self.publisher_ = self.create_publisher(String, 'order_list', 10)
        
        self.app = QApplication([])
        self.window = MainWindow()
        self.window.show()

        # PyQt 애플리케이션 종료 시 rclpy도 종료
        self.app.aboutToQuit.connect(self.shutdown_ros)
    
    def run(self):
        self.app.exec_()
    
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
