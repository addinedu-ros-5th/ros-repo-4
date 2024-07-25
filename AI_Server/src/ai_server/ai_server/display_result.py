import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
import json

print('start display')

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.image_subscription = self.create_subscription(
            Image,
            'detection_image',
            self.image_callback,
            10)
        self.result_subscription = self.create_subscription(
            String,
            'detection_result',
            self.result_callback,
            10)
        self.bridge = CvBridge()
        self.detection_data = None
        self.cv_image = None
        self.get_logger().info("ImageSubscriber node initialized")

    def image_callback(self, msg):
        self.cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        self.get_logger().info("Image received")
        if self.detection_data:
            self.draw_bounding_boxes()
        cv2.imshow("Detection Image", self.cv_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.destroy_node()
            rclpy.shutdown()

    def result_callback(self, msg):
        self.get_logger().info("Detection result received")
        self.detection_data = json.loads(msg.data)
        if self.cv_image is not None:
            self.draw_bounding_boxes()
            cv2.imshow("Detection Image", self.cv_image)

    def draw_bounding_boxes(self):
        if 'labels' in self.detection_data and 'distances' in self.detection_data and 'boxes' in self.detection_data:
            for label, distance, bbox in zip(self.detection_data['labels'], self.detection_data['distances'], self.detection_data['boxes']):
                x1, y1, x2, y2 = map(int, bbox)
                cv2.rectangle(self.cv_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label_text = f"{label} {distance:.2f}m"
                cv2.putText(self.cv_image, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                x_center = (x1 + x2) // 2
                y_center = (y1 + y2) // 2
                cv2.circle(self.cv_image, (x_center, y_center), 5, (0, 0, 255), -1)
            self.get_logger().info("Bounding boxes drawn")
        else:
            self.get_logger().error("Missing keys in detection data")

def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    image_subscriber.get_logger().info("Starting spin")
    rclpy.spin(image_subscriber)

    cv2.destroyAllWindows()
    image_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
