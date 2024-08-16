# 도심형 풀필먼트 물류 서비스
(기간: 2024년 07월 09일 ~ 2024년 08월 09일)
## 1. 👨‍🏫Project Introduction👨‍🏫
### 1-1. Background
  <div align=center> 
      <br/>
      <img src="https://github.com/user-attachments/assets/643fe683-dd63-47d9-a31e-8eb710a71f28" width ="800">
  </div>
  
### 1-2. Project Purpose
  <div align=center> 
      <br/>
      <img src="https://github.com/user-attachments/assets/588414cf-cd6e-493a-8922-550cee1ed006" width ="800">
  </div>

### 1-3. Technology Stack
  <div align=center>
      
   |**Category**|**Details**|
  |:----------:|:----------:|
  |**DEV**|<img src="https://img.shields.io/badge/Ubuntu22.04-E95420?style=for-the-badge&logo=Ubuntu22.04&logoColor=white"> <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=Linux&logoColor=white"> |
  |**TECH**|<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white"> <img src="https://img.shields.io/badge/ROS2-22314E?style=for-the-badge&logo=ros&logoColor=white"> <img src="https://img.shields.io/badge/YOLO-512BD4?style=for-the-badge&logoColor=white"> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logoColor=white"> <img src="https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=Qt&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">|
  |**HW**|<img src="https://img.shields.io/badge/Rasberrypi4-A22846?style=for-the-badge&logo=raspberrypi&logoColor=white">  <img src="https://img.shields.io/badge/Arduino-00878F?style=for-the-badge&logo=Arduino&logoColor=white"> <img src="https://img.shields.io/badge/ESP32-4285F4?style=for-the-badge&logoColor=white">|
  |**TOOL**|<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"> <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"> <img src="https://img.shields.io/badge/Confluence-172B4D?style=for-the-badge&logo=Confluence&logoColor=white"> <br> <img src="https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=Jira&logoColor=white"> <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=Slack&logoColor=white"> <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=Figma&logoColor=white"> |
</div> 

### 1-4. Member Role

## 2. Project Design
### 2-1. Process Flow Chart
* Inbound Flow
  <div align=center> 
      <br/>
      <img src="https://github.com/user-attachments/assets/51fe083a-c311-44fb-98dc-525938d2381b" width ="800">
  </div>
* Outbound Flow
  <div align=center> 
      <br/>
      <img src="https://github.com/user-attachments/assets/84abaf8a-6374-41bb-98e3-3bb80e60608e" width ="800">
  </div>

### 2-2. HW Architecture
### 2-3. System Architecture
### 2-4. State Display
* Robot State
* Items State in Rack 

## 3. Main Technology
### 3-1. Multi-Robot Task Scheduling Algorithm
#### 3-1-1. Order List Grouping
#### 3-1-2. LOW-Coast Auction

### 3-2. Path Planning
#### 3-2-1. SLAM & Navigation
#### 3-2-2. A* Algorithm

### 3-3. DeepLearning
#### 3-3-1. Human Detection

### 3-4. Order Information and Robot Control Management System

## 4.  Prerequisite & Installation
### :warning:빌드시 주의사항:warning:
0. humble (ROS 환경 불러오기)
1. Local로 clone or pull했을 때, log, install, build 삭제 src파일만 남기기
2. workspace에서 의존성 자동 설치
    ```
    rosdep install --from-paths src --ignore-src -r -y
    ```
3. colcon build
### :warning:Docker에서 Ultralytics YOLO 모델 환경 구축하기:warning:
1. NVIDIA Docker 런타임을 설치하여 Docker 컨테이너에서 GPU 지원을 활성화
   ```
    # Add NVIDIA package repositories
    $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
       && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
       && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

    # Install NVIDIA Docker runtime
    $ sudo apt-get update
    $ sudo apt-get install -y nvidia-docker2

    # Restart Docker service to apply changes
    $ sudo systemctl restart docker
    ```
2. Docker 명령어로 NVIDIA 확인
    ```
    $ docker info | grep -i runtime
    ```
3. Ultralytics Docker 이미지 설치
    ```
    # Set image name as a variable
    $ t=ultralytics/ultralytics:latest

    # Pull the latest Ultralytics image from Docker Hub
    $ sudo docker pull $t
    ```
4. Docker 컨테이너에서 Ultralytics 실행
    ```
    # 로컬 PC 내 모델 작업경로를 Docker 내 작업경로에 공유
    $ t=ultralytics/ultralytics:latest
    $ docker run -it --ipc=host --gpus all -v '로컬 PC 모델 작업경로':'Docker 작업경로' $t

    # 예시) Docker 내 작업경로에서 실행
    $ t=ultralytics/ultralytics:latest
    $ docker run -it --ipc=host --gpus all -v /home/edu/dev_ws/YOLOv5:/workspace $t
    root@7178de4f531f:/workspace/yolov5# python3 detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images --name exp2 --exist-ok
    ```
### :warning:AWS RDS 상 DB 정보 로컬에 저장:warning:
0. AWS RDS 상 데이터베이스 백업
    ```
    ~/dev_ws/git_ws$ mysqldump -h database-1.cdigc6umyoh0.ap-northeast-2.rds.amazonaws.com -P 3306 -u root -p DFC_system_db > DFC_system_db.sql
    Enter password: AWS RDS PW
    ```
1. 로컬 디렉토리에 해당하는 sql 파일 로컬 MYSQL에 import
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

## 5. Usage




