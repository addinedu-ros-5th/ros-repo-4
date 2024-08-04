# final_project
***
### 빌드시 주의사항
#### 0. humble (로스환경불러오기)
#### 1. Local로 clone or pull했을 때, log, install, build 삭제 src파일만 남겨둠

#### 2. workspace에서 의존성 자동 설치
rosdep install --from-paths src --ignore-src -r -y

#### 3. colcon build
***

### AWS RDS 상 DB 정보 로컬에 저장
```
~/dev_ws/git_ws$ mysqldump -h database-1.cdigc6umyoh0.ap-northeast-2.rds.amazonaws.com -P 3306 -u root -p DFC_system_db > DFC_system_db.sql
Enter password: 슬랙에 있는 AWS RDS PW: xxxxxx
```
### 로컬 디렉토리에 해당하는 sql 파일 로컬 MYSQL에 import
```
~/dev_ws/git_ws$ mysql -u root -p
Enter password: 본인 로컬 MYSQL PW
```
 
```
mysql > create database DFC_system_db;
mysql > use DFC_system_db;
mysql > SOURCE 'DFC_system_db.sql 위치한 절대 경로';
mysql > show tables;
```


***
### 로봇 기동 순서 
#### (로봇에 원격 접속 후)
```
cd ~/final_project/ros-repo-4/scripts
chmod +x launch_robot.sh launch_map.sh robot_drive.sh
```

#### 0. 로봇 기동
```
cd ~/final_project/ros-repo-4/scripts
./launch_robot.sh
```
#### 1. (다른 터미널 열고) robot_drive 노드 실행
```
cd ~/final_project/ros-repo-4/scripts
./robot_drive.sh
```

#### 2. (다른 터미널 열고) nav2 맵 실행
```
cd ~/final_project/ros-repo-4/scripts
./launch_map.sh
```
#### 내 pc에서 실행 

#### 3. (다른 터미널 열고) PC에 있는 레파지토리에서 경로 생성 코드 실행
```
humble
export ROS_DOMAIN_ID=48
cd `/final_project/ros-repo-4/MFC_Robot/
source install/local_setup.bash
ros2 launch lrobot path_server_launch.py
```

#### 4. (다른 터미널 열고) [임시] 목표 좌표 발행
```
humble
export ROS_DOMAIN_ID=48
ros2 topic pub /target_pose minibot_interfaces/GoalPose "{position_x: 1.04, position_y: 1.45, orientation_z: 0.7, orientation_w: 0.7}" --once
```
