# Docker에서 Ultralytics YOLO 모델 환경 구축하기
***
## 사전준비
### NVIDIA Docker 런타임을 설치하여 Docker 컨테이너에서 GPU 지원을 활성화
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
### Docker 명령어로 NVIDIA 확인
```
$ docker info | grep -i runtime
```
### Ultralytics Docker 이미지 설치
```
# Set image name as a variable
$ t=ultralytics/ultralytics:latest

# Pull the latest Ultralytics image from Docker Hub
$ sudo docker pull $t
```
### Docker 컨테이너에서 Ultralytics 실행 
#### [이론상] CPU 사용
```
$ t=ultralytics/ultralytics:latest
$ docker run -it --ipc=host $t
```
#### [이론상] GPU 사용
```
$ t=ultralytics/ultralytics:latest
$ docker run -it --ipc=host --gpus all $t
```
#### [우리에게 필요] 로컬 PC 내 모델 작업경로를 Docker 내 작업경로에 공유
```
$ t=ultralytics/ultralytics:latest
$ docker run -it --ipc=host --gpus all -v 로컬 PC 모델 작업경로:Docker 작업경로 $t
```
### Docker 내 작업경로에서 실행
EX)
```
$ t=ultralytics/ultralytics:latest
$ docker run -it --ipc=host --gpus all -v /home/edu/dev_ws/YOLOv5:/workspace $t

root@7178de4f531f:/workspace/yolov5# python3 detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images --name exp2 --exist-ok
```
