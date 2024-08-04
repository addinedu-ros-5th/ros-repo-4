import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
from sensor_msgs.msg import Image, LaserScan
from cv_bridge import CvBridge
import socket
import cv2
import json
import time
import threading

class SensorSender(Node):
    def __init__(self):
        super().__init__('sensor_sender')

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            depth=10
        )

        self.image_subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10)
        
        self.lidar_subscription = self.create_subscription(
            LaserScan,
            '/scan',  # 라이다 토픽 이름을 적절히 변경하세요
            self.lidar_callback,
            qos_profile
            )
        
        self.bridge = CvBridge()
        self.image_buffer = []
        self.lidar_buffer = []
        
        # PC 서버 설정 (PC의 IP 주소를 사용)
        self.pc_ip = '192.168.2.17'  # 예: PC의 IP 주소
        self.pc_port = 8080
        self.connect_to_server()
    
    def connect_to_server(self):
        while True:
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((self.pc_ip, self.pc_port))
                print(f"Connected to PC server at {self.pc_ip}:{self.pc_port}")
                break
            except socket.error as e:
                print(f"Failed to connect to server: {e}, retrying in 1 second...")
                time.sleep(1)
    
    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        # 이미지를 JPEG 형식으로 인코딩
        _, buffer = cv2.imencode('.jpg', cv_image)
        image_data = buffer.tobytes()
        image_timestamp = msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9
        
        # 이미지 버퍼에 추가
        self.image_buffer.append((image_data, image_timestamp))
        
        # 오래된 데이터를 제거 (0.5초보다 오래된 데이터 제거)
        current_time = time.time()
        self.image_buffer = [(data, ts) for data, ts in self.image_buffer if current_time - ts < 0.5]
        
        self.send_data()

    def lidar_callback(self, msg):
        # 라이다 데이터를 JSON 형식으로 변환
        lidar_data = {
            'angle_min': msg.angle_min,
            'angle_max': msg.angle_max,
            'ranges': list(msg.ranges),
            'intensities': list(msg.intensities)
        }
        lidar_timestamp = msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9
        
        # 라이다 버퍼에 추가
        self.lidar_buffer.append((lidar_data, lidar_timestamp))
        
        # 오래된 데이터를 제거 (0.5초보다 오래된 데이터 제거)
        current_time = time.time()
        self.lidar_buffer = [(data, ts) for data, ts in self.lidar_buffer if current_time - ts < 0.5]
        
        self.send_data()

    def send_data(self):
        if not self.image_buffer or not self.lidar_buffer:
            return
        
        # 타임스탬프를 기준으로 가장 최근의 이미지와 라이다 데이터 찾기
        image_data, image_timestamp = self.image_buffer[-1]
        lidar_data, lidar_timestamp = min(self.lidar_buffer, key=lambda x: abs(x[1] - image_timestamp))
        
        # 이미지와 라이다 데이터의 타임스탬프가 일치하는지 확인
        if abs(image_timestamp - lidar_timestamp) > 0.1:  # 100ms 이내로 동기화
            return

        lidar_json = json.dumps(lidar_data).encode('utf-8')
        image_length = len(image_data)
        lidar_length = len(lidar_json)
        total_length = 8 + image_length + lidar_length

        print(f"Sending total data of length: {total_length}")

        try:
            # 데이터 길이 전송
            self.client_socket.sendall(total_length.to_bytes(4, 'big'))

            # 이미지 데이터 길이 전송
            self.client_socket.sendall(image_length.to_bytes(4, 'big'))

            # 이미지 데이터 전송
            self.client_socket.sendall(image_data)

            # 라이다 데이터 길이 전송
            self.client_socket.sendall(lidar_length.to_bytes(4, 'big'))

            # 라이다 데이터 전송
            self.client_socket.sendall(lidar_json)

            print("Data sent")
        except socket.error as e:
            print(f"Socket error: {e}, reconnecting...")
            self.connect_to_server()
            self.send_data()  # 재연결 후 다시 데이터 전송 시도

def main(args=None):
    rclpy.init(args=args)
    sensor_sender = SensorSender()
    rclpy.spin(sensor_sender)
    sensor_sender.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()