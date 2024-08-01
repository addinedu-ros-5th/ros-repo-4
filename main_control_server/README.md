
### 입고 시나리오 진행 순서
#### 1. esp32_master.ino 및 arduino_slave_1.ino 빌드하기
```
# esp32_mater.ino
const char* ssid = "와이파이 이름";
const char* password = "비밀번호";

String MFCNetworkManagerIP = "PC IP 주소"; // network_manager IP 주소. ifconfig로 확인하기

# Serial Monitor
...
11:16:43.140 -> IP address: 'ESP32 IP 주소'
...
```

#### 2. communication_MFC_arduino.py 수정
```
# ros-repo-4/main_control_server/src/network_manager/src/communication_MFC_arduino.py
...
self.esp32_master = ESP32Master('ESP32 IP 주소', 80) # 시리얼 통신 클래스 인스턴스 생성
...

def receive_inspection_server(self):
        self.check_and_close_existing_socket('PC IP 주소', 12345)
        ...
        receive_inspection_server_socket.bind(('PC IP 주소', 12345))  # 서버 IP와 포트 설정 ifconfig로 확인하기
        ...
```
#### 3. 메인서버 내 노드 순차적 실행
```
# 빌드 및 ros 환경 불러온 후
## 터미널 1
ros2 run task_manager task_manager_node.py 

## 터미널 2
ros2 run task_allocator task_allocator_node.py

## 터미널 3
ros2 run robot_state robot_state_manager_node.py 

## 터미널 4
ros2 run robot_state robot_task_server.py 

## 터미널 5
ros2 run network_manager communication_MFC_arduino.py

## 터미널 6
ros2 run main_server_gui main_server_gui.py 
```
#### 4. GUI 상에서 START 8:00 AM 여러번 실행
##### 아래 결과 나와야 액션 통신 준비 완료
```
## 터미널 3
~$ ros2 run robot_state robot_state_manager_node.py 
Update 전 초기값
Debugging ['Debugging', 'Debugging', 'Debugging'] Debugging
################################################################
[INFO] [1722479547.594396443] [mfc_robot_manager]: Received task assignment for robot: Robo1
[INFO] [1722479547.594757637] [mfc_robot_manager]: Task Code: Task_1
[INFO] [1722479547.594980065] [mfc_robot_manager]: Rack List: ['R_F3']
[INFO] [1722479547.595161416] [mfc_robot_manager]: Task Assignment: 입고
It is in MFCRobotManager
Robo1 Task_1 ['R_F3'] 입고
################################################################
Update 후
Robo1 Task_1 ['R_F3'] 입고
################################################################
[INFO] [1722479547.690252849] [robot_task_client]: Goal accepted: )
```
```
## 터미널 4
~$ ros2 run robot_state robot_task_server.py 
[INFO] [1722479547.702819031] [robot_task_server]: Executing goal...
[INFO] [1722479547.703119457] [robot_task_server]: Client sent: robot_name=Robo1, goal_location=R_F3
[INFO] [1722479607.759886072] [robot_task_server]: Current_pose: pos_x = -10.0, pos_y = -10.0
```

