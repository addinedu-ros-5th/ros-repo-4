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
import signal

# SIGPIPE 시그널을 무시하도록 설정
signal.signal(signal.SIGPIPE, signal.SIG_IGN)

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
            '/scan',
            self.lidar_callback,
            qos_profile
            )
        
        self.bridge = CvBridge()
        self.image_buffer = []
        self.lidar_buffer = []
        self.buffer_lock = threading.Lock()
        self.max_buffer_size = 100  # 버퍼의 최대 크기 설정
        
        self.pc_ip = '192.168.1.17'
        self.pc_port = 8080
        self.robot_id = 'robot_1'

        self.image_send_interval = 1/15 # 이미지 전송 주기 (초)
        self.last_image_send_time = 0

        self.connected = False
        self.connect_to_server()
    
    def connect_to_server(self):
        while not self.connected:
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((self.pc_ip, self.pc_port))
                self.connected = True
                print(f"Connected to PC server at {self.pc_ip}:{self.pc_port}")
            except socket.error as e:
                print(f"Failed to connect to server: {e}, retrying in 1 second...")
                time.sleep(1)
    
    def close_connection(self):
        if self.client_socket:
            try:
                self.client_socket.shutdown(socket.SHUT_RDWR)
            except:
                pass
            self.client_socket.close()
            self.connected = False
            print("Connection closed")

    def image_callback(self, msg):
        current_time = time.time()
        if current_time - self.last_image_send_time < self.image_send_interval:
            return
        self.last_image_send_time = current_time

        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # 이미지를 320x240으로 리사이즈
        cv_image = cv2.resize(cv_image, (320, 240))

        _, buffer = cv2.imencode('.jpg', cv_image)
        image_data = buffer.tobytes()
        image_timestamp = msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9
        
        with self.buffer_lock:
            if len(self.image_buffer) >= self.max_buffer_size:
                self.image_buffer.pop(0)
            self.image_buffer.append((image_data, image_timestamp))
        
        self.send_data()

    def lidar_callback(self, msg):
        lidar_data = {
            'angle_min': msg.angle_min,
            'angle_max': msg.angle_max,
            'ranges': list(msg.ranges),
            'intensities': list(msg.intensities)
        }
        lidar_timestamp = msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9
        
        with self.buffer_lock:
            if len(self.lidar_buffer) >= self.max_buffer_size:
                self.lidar_buffer.pop(0)
            self.lidar_buffer.append((lidar_data, lidar_timestamp))
        
        self.send_data()

    def send_data(self):
        if not self.connected:
            return

        with self.buffer_lock:
            if not self.image_buffer or not self.lidar_buffer:
                return
        
            image_data, image_timestamp = self.image_buffer[-1]
            lidar_data, lidar_timestamp = min(self.lidar_buffer, key=lambda x: abs(x[1] - image_timestamp))
            
            if abs(image_timestamp - lidar_timestamp) > 0.1:
                return

            lidar_json = json.dumps(lidar_data).encode('utf-8')
            image_length = len(image_data)
            lidar_length = len(lidar_json)
            robot_id_encoded = self.robot_id.encode('utf-8')
            robot_id_length = len(robot_id_encoded)
            total_length = 4 + robot_id_length + 4 + image_length + 4 + lidar_length

            print(f"Sending total data of length: {total_length}")

            try:
                self.client_socket.sendall(total_length.to_bytes(4, 'big'))
                self.client_socket.sendall(robot_id_length.to_bytes(4, 'big'))
                self.client_socket.sendall(robot_id_encoded)
                self.client_socket.sendall(image_length.to_bytes(4, 'big'))
                self.client_socket.sendall(image_data)
                self.client_socket.sendall(lidar_length.to_bytes(4, 'big'))
                self.client_socket.sendall(lidar_json)

                print("Data sent")
            except (socket.error, BrokenPipeError) as e:
                print(f"Socket error: {e}, reconnecting...")
                self.close_connection()
                self.connect_to_server()

def main(args=None):
    rclpy.init(args=args)
    sensor_sender = SensorSender()
    rclpy.spin(sensor_sender)
    sensor_sender.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
