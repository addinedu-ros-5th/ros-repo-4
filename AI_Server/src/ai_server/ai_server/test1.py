import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from sensor_msgs.msg import Image, LaserScan
from std_msgs.msg import String
import cv2
import numpy as np
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
from cv_bridge import CvBridge
import threading
import math
import json
from ultralytics import YOLO
import time
from concurrent.futures import ThreadPoolExecutor
import logging

class DistanceCalculator:
    def calculate_distance(self, lidar_data, box, image_width, lidar_offset_forward, lidar_offset_downward):
        x_center = (box[0] + box[2]) // 2
        lidar_angle_min = -180.0
        lidar_angle_max = 180.0
        angle_range = lidar_angle_max - lidar_angle_min
        angle_per_pixel = angle_range / image_width
        lidar_angle = lidar_angle_min + (x_center * angle_per_pixel)
        min_distance = float('inf')
        for offset in range(-20, 21):
            angle_offset = lidar_angle + (offset * angle_per_pixel)
            angle_index = int((angle_offset - lidar_angle_min) / angle_range * len(lidar_data.ranges))
            if 0 <= angle_index < len(lidar_data.ranges):
                distance = lidar_data.ranges[angle_index]
                if distance != float('inf') and distance > 0:
                    distance_corrected = math.sqrt(distance**2 - lidar_offset_forward**2 - lidar_offset_downward**2)
                    if distance_corrected < min_distance:
                        min_distance = distance_corrected
        return min_distance

class YoloDetector:
    def __init__(self, model_path='yolov5s.pt'):
        logging.getLogger("ultralytics").setLevel(logging.WARNING)

        self.model = YOLO(model_path)

    def detect_objects(self, image):
        results = self.model(image)
        return results

class ImageDisplayNode(Node):
    def __init__(self):
        super().__init__('image_display_node')

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            depth=10
        )

        self.image_sub_1 = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback_1,
            10)

        self.image_sub_2 = self.create_subscription(
            Image,
            '/camera/image_raw_2',
            self.image_callback_2,
            10)
        
        self.lidar_sub_1 = self.create_subscription(
            LaserScan,
            'scan',
            self.lidar_callback_1,
            qos_profile
            )
        
        self.lidar_sub_2 = self.create_subscription(
            LaserScan,
            'scan_2',
            self.lidar_callback_2,
            qos_profile
            )

        self.publisher = self.create_publisher(String, 'detection_result', 10)

        self.bridge = CvBridge()
        self.distance_calculator = DistanceCalculator()
        self.yolo_detector = YoloDetector()
        self.lidar_data_1 = None
        self.lidar_data_2 = None

        self.lock = threading.Lock()
        self.image_1 = None
        self.image_2 = None
        self.thread = threading.Thread(target=self.display_images)
        self.thread.start()
        self.last_detection_time_1 = 0
        self.last_detection_time_2 = 0
        self.detection_interval = 0.5  # 0.5초마다 객체 탐지 수행

    def image_callback_1(self, msg):
        try:
            image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            resized_image = cv2.resize(image, (640, 480))
            with self.lock:
                self.image_1 = resized_image
        except Exception as e:
            pass

    def image_callback_2(self, msg):
        try:
            image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            resized_image = cv2.resize(image, (320, 240))
            with self.lock:
                self.image_2 = resized_image
        except Exception as e:
            pass

    def lidar_callback_1(self, msg):
        self.lidar_data_1 = msg
        
    def lidar_callback_2(self, msg):
        self.lidar_data_2 = msg

    def send_detection_data(self, robot_id, labels, distances):
        detection_data = {
            'robot_id': robot_id,
            'labels': labels,
            'distances': distances
        }
        msg = String()
        msg.data = json.dumps(detection_data)
        self.publisher.publish(msg)

    def detect_and_annotate(self, image, lidar_data, robot_id):
        try:
            results = self.yolo_detector.detect_objects(image)

            img_center_x = image.shape[1] // 2

            labels = []
            distances = []
            detected_people = False
            annotated_image = image.copy()
            for result in results:
                for box in result.boxes:
                    if box.cls == 0 and box.conf > 0.7:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        box_center_x = (x1 + x2) // 2

                        if abs(box_center_x - img_center_x) <= 100:
                            detected_people = True
                            distance = self.distance_calculator.calculate_distance(
                                lidar_data,
                                (x1, y1, x2, y2),
                                image.shape[1],
                                0.07,
                                0.02
                            )
                            labels.append('person')
                            distances.append(distance)
                            label = f"person {distance:.2f}m"
                            cv2.rectangle(annotated_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                            cv2.putText(annotated_image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                            x_center = (x1 + x2) // 2
                            y_center = (y1 + y2) // 2
                            cv2.circle(annotated_image, (x_center, y_center), 5, (0, 0, 255), -1)

            if labels and distances:
                self.send_detection_data(robot_id, labels, distances)

            return annotated_image
        except Exception as e:
            return image

    def display_images(self):
        with ThreadPoolExecutor(max_workers=2) as executor:
            while rclpy.ok():
                try:
                    current_time = time.time()
                    if self.image_1 is not None and self.lidar_data_1 is not None:
                        if current_time - self.last_detection_time_1 >= self.detection_interval:
                            self.last_detection_time_1 = current_time
                            executor.submit(self.process_image, self.image_1, self.lidar_data_1, 'robot_1')
                    if self.image_2 is not None and self.lidar_data_2 is not None:
                        if current_time - self.last_detection_time_2 >= self.detection_interval:
                            self.last_detection_time_2 = current_time
                            executor.submit(self.process_image, self.image_2, self.lidar_data_2, 'robot_2')
                    cv2.waitKey(1)
                except Exception as e:
                    pass

    def process_image(self, image, lidar_data, robot_id):
        try:
            annotated_image = self.detect_and_annotate(image, lidar_data, robot_id)
            if annotated_image.shape[0] > 0 and annotated_image.shape[1] > 0:
                cv2.imshow(f"Image from {robot_id}", annotated_image)
        except Exception as e:
            pass

def main(args=None):
    try:
        rclpy.init(args=args)
        node = ImageDisplayNode()
        executor = MultiThreadedExecutor()  # ROS 2 콜백을 위한 MultiThreadedExecutor
        executor.add_node(node)
        try:
            executor.spin()
        finally:
            node.destroy_node()
            rclpy.shutdown()
            cv2.destroyAllWindows()
    except Exception as e:
        pass

if __name__ == '__main__':
    main()
