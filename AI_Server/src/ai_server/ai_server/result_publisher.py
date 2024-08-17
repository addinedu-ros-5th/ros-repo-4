import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import time

class DetectionClient(Node):
    def __init__(self):
        super().__init__('detection_client')
        self.publisher = self.create_publisher(String, 'detection_result', 10)
        self.timer = self.create_timer(1.0, self.publish_detection_data)  # Set the timer to call the function periodically

    def publish_detection_data(self):
        try:
            with open('./detection_data.json', 'r') as f:
                detection_data = json.load(f)
                msg = String()
                msg.data = json.dumps(detection_data)
                self.publisher.publish(msg)
                self.get_logger().info("Detection data sent")
        except FileNotFoundError:
            self.get_logger().info("Detection data file not found")
        except json.JSONDecodeError:
            self.get_logger().info("Error decoding JSON data")

def main():
    rclpy.init()
    detection_client = DetectionClient()

    try:
        rclpy.spin(detection_client)
    except KeyboardInterrupt:
        pass

    detection_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
