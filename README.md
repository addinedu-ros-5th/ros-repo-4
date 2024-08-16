# 도심형 풀필먼트 물류 서비스

## 1. Project Introduction
### 1-1. Project Purpose
### 1-2. Background
### 1-3. Technology Stack
### 1-4. Member Role

## 2. Project Design
### 2-1. Process Flow Chart
* Inbound Flow
* Outbound Flow
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




