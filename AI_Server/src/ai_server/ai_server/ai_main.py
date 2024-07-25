import socket
import cv2
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
from .yolo_loads import YoloDetector
from .distance_calculator import DistanceCalculator
from .data_handle import DataHandler

# 서버 설정
server_ip = '0.0.0.0'
server_port = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"Server listening on {server_ip}:{server_port}")

class DetectionClient(Node):
    def __init__(self):
        super().__init__('detection_client')
        self.publisher = self.create_publisher(String, 'detection_result', 10)

    def send_detection_data(self, labels, distances):
        detection_data = {
            'labels': labels,
            'distances': distances
        }
        msg = String()
        msg.data = json.dumps(detection_data)
        self.publisher.publish(msg)
        self.get_logger().info("Detection data sent")

def main():
    rclpy.init()
    detection_client = DetectionClient()
    
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            data_handler = DataHandler(client_socket)
            yolo_detector = YoloDetector()
            distance_calculator = DistanceCalculator()

            try:
                while True:
                    image, lidar_data = data_handler.receive_data()
                    if image is None or lidar_data is None:
                        print("Failed to receive data")
                        break

                    results = yolo_detector.detect_objects(image)

                    labels = []
                    distances = []
                    detected_people = False
                    annotated_image = image.copy()
                    for result in results:
                        for box in result.boxes:
                            if box.cls == 0 and box.conf > 0.7:
                                detected_people = True
                                x1, y1, x2, y2 = map(int, box.xyxy[0])
                                distance = distance_calculator.calculate_distance(
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
                                print(label)

                    if labels and distances:
                        detection_client.send_detection_data(labels, distances)

                    if not detected_people:
                        print("No person detected")

                    cv2.imshow('YOLO Output', annotated_image)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            except Exception as e:
                print(f"Error during processing: {e}")
            finally:
                client_socket.close()
                print("Client disconnected")
                cv2.destroyAllWindows()

        except Exception as e:
            print(f"Server error: {e}")

if __name__ == '__main__':
    try:
        main()
    finally:
        server_socket.close()
        print("Server socket closed")
        rclpy.shutdown()
