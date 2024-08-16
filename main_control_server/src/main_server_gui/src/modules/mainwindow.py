from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer, QTime, pyqtSignal
from ament_index_python.packages import get_package_share_directory
import os
import yaml
import mysql.connector as con

from modules.connect import Connect
from modules.robotstatewindow import *
from modules.signinwindow import *

def get_mysql_connection():
    try:
        db_id, db_pw = load_db_params(yaml_file_path)
        db_instance = Connect(db_id, db_pw)
        return db_instance
    except con.Error as err:
        print(f"Error: {err}")
        return None    
        
class MainWindow(QtWidgets.QMainWindow):
    #----------------------------------- Inbound 관련 Signal(출처: Class InboundNode(Node) ) -----------------------------------
    # Signal 정의 로스노드로부터 데이터를 받아야해요~
    inbound_list_signal = pyqtSignal(list)                  # self.get_logger().info(f'Parsed outbound_list list: {outbound_list}')
    #8시 알려라~ node에~
    schedule_signal = pyqtSignal()  # 8시가 되었음을 알리는 신호
    
    # DB 업데이트 완료요~(task_manager한테 알려줄 용도)
    db_update_signal = pyqtSignal(str) 
    inbound_status_db_update_signal = pyqtSignal()

    def __init__(self, username=''):
        super(MainWindow, self).__init__()
        self.inbound_management_active = False
        self.outbound_management_active = False

        ui_file = os.path.join(get_package_share_directory('main_server_gui'), 'ui', 'window2.ui')
        uic.loadUi(ui_file, self)

        self.username = username
        self.treeWidget.itemClicked.connect(self.handle_tree_item_click)
        self.signinButton.clicked.connect(self.open_signin_window)
        self.logoutButton.clicked.connect(self.handle_logout)
        self.update_ui_for_logged_in_user()
    
        self.startButton.clicked.connect(self.toggleClock)
        self.startButton.setEnabled(False)  
        self.timeEdit.setTime(QTime(7, 55))
        self.timeEdit.setEnabled(False)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateClock)
        self.schedule_timer = QTimer(self)
        self.schedule_timer.timeout.connect(self.check_schedule)
        self.schedule_timer.start(1000)

        # 관제 및 로봇 상태 관리창 인스턴스
        self.robot_state_window = None

        # Signal 연결
        #----------------------------------- Inbound 관련 Signal -----------------------------------
        self.inbound_list_signal.connect(self.display_inbound_list)
        self.inbound_status_db_update_signal.connect(self.show_inbound_management)

    def toggleClock(self):
        if self.startButton.text() == 'Start':
            self.startClock()
        else:
            self.stopClock()

    def startClock(self):
        self.time = self.timeEdit.time()
        self.timer.start(100)
        self.updateClock()
        self.startButton.setText('Close')

    def stopClock(self):
        self.timer.stop()
        self.startButton.setText('Start')
        self.timeEdit.setTime(QTime(7, 55))

    def updateClock(self):
        self.time = self.time.addSecs(10)
        self.timeEdit.setTime(self.time)

    def check_schedule(self):
        current_time = self.timeEdit.time()
        if current_time.hour() == 8 and current_time.minute() == 0:
            self.schedule_signal.emit()  # 8시가 되었음!! 로스에 전달!!

    #----------------------------------- Inbound 관련 매써드 -----------------------------------
    def display_inbound_list(self, inbound_list):
        self.update_inbound_list(inbound_list)
        if self.inbound_management_active:
            self.show_inbound_management()

    def update_inbound_list(self, inbound_list):#초기 리스트 update
        db_instance = get_mysql_connection()
        if db_instance:
            try:
                db_instance.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
                db_instance.cursor.execute("DELETE FROM Inbound_Manager")    # 여기서 DB 테이블 삭제
                db_instance.cursor.execute("SET FOREIGN_KEY_CHECKS=1")
                for idx, item in enumerate(inbound_list, start=1):
                    insert_query = ("INSERT INTO Inbound_Manager (No, Product_Code, Product_Name, Warehouse, Rack, Cell, Receiving_Quantity, Status) "
                                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
                    data = (idx, item['item_id'], item['name'], item['warehouse'], item['rack'], item['cell'], item['quantity'], item['status'])
                    db_instance.cursor.execute(insert_query, data)
                db_instance.conn.commit()
                db_instance.disConnection()

                self.db_update_signal.emit("DB Update Completed")
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

    def populate_table_widget(self, data, table_name):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        if not data:
            return
        num_rows = len(data)
        num_columns = len(data[0])
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_columns)
        column_names = [desc[0] for desc in self.fetch_column_names(table_name)]
        self.tableWidget.setHorizontalHeaderLabels(column_names)
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
        pass

    def show_warehouse_status(self):
        if not self.username:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 후에 진행해 주세요.')
            return
        
    #----------------------------------- Inbound 관련 매써드 -----------------------------------
    def show_inbound_management(self):
        if not self.username:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 후에 진행해 주세요.')
            return
        data = self.fetch_inbound_table_data()
        if data:
            self.populate_table_widget(data, 'Inbound_Manager')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'No data found in Inbound_Manager')

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
            
    def show_robotstate_management(self):
        if self.robot_state_window is None:
            self.robot_state_window = RobotStateWindow(self)
        self.robot_state_window.show()
        self.close()
