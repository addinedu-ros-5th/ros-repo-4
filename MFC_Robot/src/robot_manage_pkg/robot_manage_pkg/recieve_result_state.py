import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import json

class DetectionServer(Node):
    def __init__(self):
        super().__init__('detection_server')
        self.cmd_vel_publisher = self.create_publisher(Twist, 'base_controller/cmd_vel_unstamped', 10)
        self.obstacle_publisher = self.create_publisher(String, 'obstacle_topic', 10)

        self.detection_subscription = self.create_subscription(
            String,
            'detection_result',
            self.listener_callback,
            10
        )
        self.cmd_vel_subscription = self.create_subscription(
            Twist,
            'base_controller/cmd_vel_unstamped',
            self.cmd_vel_callback,
            10
        )
        self.obstacle_detected = False  # 장애물이 감지되었는지 추적

    def listener_callback(self, msg):
        detection_data = json.loads(msg.data)
        labels = detection_data['labels']
        distances = detection_data['distances']
        for label, distance in zip(labels, distances):
            self.get_logger().info(f"Detected {label}, {distance:.2f}m")
            if label == "person" and distance <= 0.2:
                if not self.obstacle_detected:
                    self.obstacle_detected = True
                    stop_command = Twist()
                    stop_command.linear.x = 0.0
                    stop_command.angular.z = 0.0
                    self.cmd_vel_publisher.publish(stop_command)
                    obstacle_msg = String()
                    obstacle_msg.data = "obstacle"
                    self.obstacle_publisher.publish(obstacle_msg)
                    self.get_logger().info("STOP command sent to the robot due to obstacle detection")
                return  # 장애물 감지 시 추가 명령 처리 중단
        if self.obstacle_detected:
            self.obstacle_detected = False
            free_msg = String()
            free_msg.data = "clear"
            self.obstacle_publisher.publish(free_msg)
            self.get_logger().info("Obstacle cleared, free command sent to the robot")

    def cmd_vel_callback(self, msg):
        if self.obstacle_detected:
            self.get_logger().info("Obstacle detected, ignoring cmd_vel message")
            return
        self.cmd_vel_publisher.publish(msg)
        self.get_logger().info("cmd_vel message forwarded to the robot")

def main(args=None):
    rclpy.init(args=args)
    detection_server = DetectionServer()
    rclpy.spin(detection_server)
    detection_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
