import os
import yaml
import mysql.connector as con
from connect import *


# YAML 파일 절대 경로
yaml_file_path = os.path.join('/home/edu/dev_ws/git_ws2/ros-repo-4/main_control_server/params/db_user_info.yaml')
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
    
class UpdateRobotState():
    def __init__(self, db_instance):
        self.cursor = db_instance.cursor

    # 데이터베이스에서 테이블 정보를 가져오는 함수 정의
    def loadDataFromDB(self, query):
        self.cursor.execute(query)
        robot_data = self.cursor.fetchall()
        return robot_data


db_instance = get_mysql_connection()
update_robot_state = UpdateRobotState(db_instance)
query = "SELECT Robot_Name, Rack_List, Status, Estimated_Completion_Time, Battery_Status, Task_Assignment, Error_Codes FROM Robot_manager;"
robot_data = update_robot_state.loadDataFromDB(query)

print(robot_data)