import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import json

class DetectionServer(Node):
    def __init__(self):
        super().__init__('detection_server')
        self.publisher_ = self.create_publisher(String, 'robot_command_topic', 10)
        self.subscription = self.create_subscription(
            String,
            'detection_topic',
            self.listener_callback,
            10
        )
        self.velocity_subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.velocity_callback,
            10
        )
        self.subscription
        self.is_robot_stopped = False  # 로봇이 정지 상태인지 추적

    def velocity_callback(self, msg):
        if msg.linear.x == 0.0 and msg.angular.z == 0.0:
            self.is_robot_stopped = True
        else:
            self.is_robot_stopped = False

    def listener_callback(self, msg):
        detection_data = json.loads(msg.data)
        labels = detection_data['labels']
        distances = detection_data['distances']
        for label, distance in zip(labels, distances):
            self.get_logger().info(f"Detected {label}, {distance:.2f}m")
            if label == "person" and distance <= 0.3:
                if not self.is_robot_stopped:  # 로봇이 정지 상태가 아니면
                    stop_command = String()
                    stop_command.data = "STOP"
                    self.publisher_.publish(stop_command)
                    self.get_logger().info("STOP command sent to the robot")
            else:
                if self.is_robot_stopped:  # 로봇이 정지 상태이면
                    self.is_robot_stopped = False  # 로봇이 움직이는 상태로 변경

def main(args=None):
    rclpy.init(args=args)
    detection_server = DetectionServer()
    rclpy.spin(detection_server)
    detection_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
