# 도심형 풀필먼트 물류 서비스
(기간: 2024년 07월 09일 ~ 2024년 08월 09일)
## 1. 👨‍🏫Project Introduction👨‍🏫
### 1-1. Background
  <div align=center> 
      <img src="https://github.com/user-attachments/assets/643fe683-dd63-47d9-a31e-8eb710a71f28" width ="800">
  </div>
  
### 1-2. Project Purpose
  <div align=center> 
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

## 2. 👨🏻‍💻Project Design👨🏻‍💻
### 2-1. Main Process Flow Chart
* Inbound Flow
  <div align=center> 
      <img src="https://github.com/user-attachments/assets/51fe083a-c311-44fb-98dc-525938d2381b" width ="800">
  </div>
  
* Outbound Flow
  <div align=center> 
      <img src="https://github.com/user-attachments/assets/84abaf8a-6374-41bb-98e3-3bb80e60608e" width ="800">
  </div>

### 2-2. HW Architecture
  <div align=center> 
      <img src="https://github.com/user-attachments/assets/bbe210e2-0043-4bbd-bae2-b25e9fa923a0" width ="800">
  </div>

### 2-3. System Architecture
  <div align=center> 
      <img src="https://github.com/user-attachments/assets/f295b644-96dd-48dc-933a-1d3606856e08" height ="600">
  </div>

### 2-4. State Display
* Robot State
  <div align=center> 
      <img src="https://github.com/user-attachments/assets/d6ae5b7c-06d1-4d36-a3c0-c716f89f2995" height ="400">
  </div>
* Items State in Rack 
  <div align=center> 
      <img src="https://github.com/user-attachments/assets/e9c21807-a186-403f-b0ff-69f3bae9a9f4" height ="400">
  </div>
  
## 3. :star:Main Technology:star:
### 3-1. Multi-Robot Task Scheduling Algorithm ℹ️
#### 3-1-1. Order List Grouping
* **동일한 or 인접한** 렉에 물품들 Rack List로 그룹핑
* **Task Code(ex.Task1,2)** 로 Rack List를 관리하며 작업 할당 경매
    <div align=center> 
      <img src="https://github.com/user-attachments/assets/c86076f8-c001-46dc-8233-65be5feb02a0" width ="600">
  </div>

#### 3-1-2. Low-Cost Based Auction
* Task Code에 대한 **할당 비용이 가장 낮은 로봇 순**으로 작업 할당
* **3가지 변수**에 대한 모든 경우의 수 고려한 최적 비용값 설정
  * 1) **로봇 초기 상태**
  * 2) **충전 상태**
  * 3) **잔여 작업수**
       
  <div align=center> 
      <img src="https://github.com/user-attachments/assets/2153a576-e220-46d2-91f8-42c6dbec5270" width ="600">
  </div>
  
### 3-2. Path Planning ℹ️
#### A* Algorithm
* 1개 경로 당 **2개의 waypoint**들 생성
* 예측 가능한 waypoint 위주로 구성된 경로를 통해 돌발 상황 감소
  <div align=center>
  </br>
      <img src="https://github.com/user-attachments/assets/76bbd056-3494-42ba-aac9-706558c72fd1" width ="800">
      <img src="https://github.com/user-attachments/assets/d7e35464-f613-49b8-bd1d-34fecd68f8d7" width ="1000">
  </div>

### 3-3. DeepLearning ℹ️
#### Human Detection
* YOLOv5 Classification 모델 사용
* 주행 중 작업자 인식 시 우선 멈춤 동작
    <div align=center>
  </br>
      <img src="https://github.com/user-attachments/assets/96a3942c-b31e-4632-b888-fdefb94ccbba" width ="600">
      <img src="https://github.com/user-attachments/assets/3125f762-b074-413f-a7e1-384310f50d5c" width ="900">
  </div>

### 3-4. Order Information and Robot Control Management System ℹ️
* GUI 구현 화면
  <div align=center> 
      <br/>
      <img src="https://github.com/user-attachments/assets/6319ac9c-76ae-4877-9a7f-19c5a789b968" width ="800">
  </div>
* 입고 시나리오 _ 적재 시연 영상
  <div align=center> 
      <br/>
      <img src="https://github.com/user-attachments/assets/eec29ead-03fe-4bef-ac66-9cf52b09d7df" width ="600">
  </div>

## 4.  :exclamation:Prerequisite & Installation:exclamation:
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




