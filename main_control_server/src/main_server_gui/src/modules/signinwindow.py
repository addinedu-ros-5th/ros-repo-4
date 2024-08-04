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

# YAML 파일 경로
# yaml_file_path = '/home/edu/dev_ws/git_ws2/ros-repo-4/main_control_server/params/db_user_info.yaml'

current_dir = os.path.dirname(os.path.abspath(__file__))
db_user_info_path = os.path.join(current_dir, "../../../../../params/db_user_info.yaml")
yaml_file_path = os.path.abspath(db_user_info_path)

# YAML 파일을 읽어 파라미터를 가져옴
def load_db_params(file_path):
    with open(file_path, 'r') as file:
        params = yaml.safe_load(file)
    return params['local_db']['id'], params['local_db']['pw']

def get_mysql_connection():
    try:
        db_id, db_pw = load_db_params(yaml_file_path)
        db_instance = Connect(db_id, db_pw)
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