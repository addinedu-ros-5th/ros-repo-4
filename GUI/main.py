from PyQt5 import QtWidgets, uic
import mysql.connector
import sys

class SigninWindow(QtWidgets.QDialog):
    def __init__(self, main_window):
        super(SigninWindow, self).__init__()
        uic.loadUi('signin.ui', self)
        
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
        try:
            conn = mysql.connector.connect(
                host="database-1.cdsoiiswk6c2.ap-northeast-2.rds.amazonaws.com",
                port=3306,
                user="root",
                password="k60746074",
                database="final_project"
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO user_manager (name, ID, password) VALUES (%s, %s, %s)", (name, user_id, password))
            conn.commit()
            conn.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def authenticate_user(self, user_id, password):
        try:
            conn = mysql.connector.connect(
                host="database-1.cdsoiiswk6c2.ap-northeast-2.rds.amazonaws.com",
                port=3306,
                user="root",
                password="k60746074",
                database="final_project"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM user_manager WHERE ID = %s AND password = %s", (user_id, password))
            user = cursor.fetchone()
            conn.close()
            return user
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def go_to_main(self):
        self.main_window.show()
        self.close()

def get_mysql_connection():
    try:
        conn = mysql.connector.connect(
            host="database-1.cdsoiiswk6c2.ap-northeast-2.rds.amazonaws.com",
            port=3306,
            user="root",
            password="k60746074",
            database="final_project"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, username=''):
        super(MainWindow, self).__init__()
        uic.loadUi('window2.ui', self)
        self.username = username
        self.treeWidget.itemClicked.connect(self.handle_tree_item_click)
        self.signinButton.clicked.connect(self.open_signin_window)
        self.logoutButton.clicked.connect(self.handle_logout)
        self.statusButton.clicked.connect(self.update_status)
        self.update_ui_for_logged_in_user()
        self.statusButton.hide()

    def handle_logout(self):
        self.username = ''
        self.update_ui_for_logged_in_user()
        self.reset_ui_to_initial_state()

    def reset_ui_to_initial_state(self):
        self.userEdit.clear()
        self.userEdit.hide()
        self.signinButton.show()
        self.logoutButton.hide()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.statusButton.hide()
        self.show()

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

    def show_inventory_management(self):
        # Load and show the inventory management screen
        pass
    
    def fetch_inbound_table_data(self):
        conn = get_mysql_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Inbound_manager")
                data = cursor.fetchall()
                conn.close()
                return data
            except mysql.connector.Error as err:
                print(f"Error: {err}")
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

    def fetch_outbound_table_data(self):
        conn = get_mysql_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Outbound_manager")
                data = cursor.fetchall()
                conn.close()
                return data
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return None

    def show_outbound_management(self):
        if not self.username:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 후에 진행해 주세요.')
            return

        data = self.fetch_outbound_table_data()
        if data:
            self.populate_table_widget(data, 'Outbound_manager')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'No data found in Outbound_manager')

    def show_warehouse_status(self):
        if not self.username:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 후에 진행해 주세요.')
            return

        data = self.fetch_all_rack_manager_data()
        if data:
            self.populate_table_widget(data, 'rack_manager')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'No data found in rack_manager table')

    def show_filtered_by_warehouse(self, warehouse, table_name):
        if not self.username:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 후에 진행해 주세요.')
            return

        data = self.fetch_filtered_by_warehouse(warehouse, table_name)
        if data:
            self.populate_table_widget(data, table_name)
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', f'No data found for warehouse: {warehouse} in {table_name} table')

    def show_filtered_by_warehouse_and_rack(self, warehouse, rack, table_name):
        if not self.username:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 후에 진행해 주세요.')
            return

        data = self.fetch_filtered_by_warehouse_and_rack(warehouse, rack, table_name)
        if data:
            self.populate_table_widget(data, table_name)
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', f'No data found for warehouse: {warehouse}, rack: {rack} in {table_name} table')

    def show_filtered_by_warehouse_rack_and_cell(self, warehouse, rack, cell, table_name):
        if not self.username:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 후에 진행해 주세요.')
            return

        data = self.fetch_filtered_by_warehouse_rack_and_cell(warehouse, rack, cell, table_name)
        if data:
            self.populate_table_widget(data, table_name)
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', f'No data found for warehouse: {warehouse}, rack: {rack}, cell: {cell} in {table_name} table')

    def fetch_all_rack_manager_data(self):
        conn = get_mysql_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM rack_manager")
                data = cursor.fetchall()
                conn.close()
                return data
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return None

    def fetch_filtered_by_warehouse(self, warehouse, table_name):
        conn = get_mysql_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {table_name} WHERE Warehouse = %s", (warehouse,))
                data = cursor.fetchall()
                conn.close()
                return data
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return None

    def fetch_filtered_by_warehouse_and_rack(self, warehouse, rack, table_name):
        conn = get_mysql_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {table_name} WHERE Warehouse = %s AND Rack = %s", (warehouse, rack))
                data = cursor.fetchall()
                conn.close()
                return data
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return None

    def fetch_filtered_by_warehouse_rack_and_cell(self, warehouse, rack, cell, table_name):
        conn = get_mysql_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {table_name} WHERE Warehouse = %s AND Rack = %s AND Cell = %s", (warehouse, rack, cell))
                data = cursor.fetchall()
                conn.close()
                return data
            except mysql.connector.Error as err:
                print(f"Error: {err}")
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
        conn = get_mysql_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SHOW COLUMNS FROM {table_name}")
                columns = cursor.fetchall()
                conn.close()
                return columns
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return []

    def update_status(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, 'Error', '행을 선택해 주세요.')
            return

        table_name = self.statusButton.property('table_name')
        status_column = None
        for col_idx in range(self.tableWidget.columnCount()):
            if self.tableWidget.horizontalHeaderItem(col_idx).text() == "Status":
                status_column = col_idx
                break

        if status_column is None:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Status 컬럼을 찾을 수 없습니다.')
            return

        if table_name == 'Inbound_manager':
            new_status = '수령완료'
        elif table_name == 'Outbound_manager':
            new_status = '배송완료'
        else:
            return

        self.tableWidget.setItem(selected_row, status_column, QtWidgets.QTableWidgetItem(new_status))

        # Update database
        item_id = self.tableWidget.item(selected_row, 0).text()  # Assuming the first column is the ID
        self.update_status_in_db(table_name, item_id, new_status)

    def update_status_in_db(self, table_name, item_id, new_status):
        conn = get_mysql_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"UPDATE {table_name} SET Status = %s WHERE idx = %s", (new_status, item_id))
                conn.commit()
                conn.close()
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                QtWidgets.QMessageBox.warning(self, 'Error', '데이터베이스 업데이트 중 오류가 발생했습니다.')

    def open_signin_window(self):
        self.hide()
        self.signin_window = SigninWindow(self)
        self.signin_window.show()
    
    def update_ui_for_logged_in_user(self):
        if self.username:
            self.userEdit.setText(self.username)
            self.userEdit.show()
            self.logoutButton.show()
            self.signinButton.hide()
        else:
            self.userEdit.hide()
            self.logoutButton.hide()
            self.signinButton.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

