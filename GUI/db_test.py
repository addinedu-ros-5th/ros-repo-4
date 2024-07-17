import os 
from Connect import Connect
import cv2

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

if __name__ == "__main__":
    db_instance = Connect("team4", "0444")
    update_robot_state = UpdateRobotState(db_instance)

    # Case 1.
    query_A = "SELECT id, name, state, battery_level, last_updated FROM Robot_State WHERE name = 'Robot_A'"
    update_robot_state.loadDataFromDB(query_A)

    # Case 2.
    query_B = "SELECT id, name, state, battery_level, last_updated FROM Robot_State WHERE name = 'Robot_B'"
    update_robot_state.loadDataFromDB(query_B)
    
    db_instance.disConnection()