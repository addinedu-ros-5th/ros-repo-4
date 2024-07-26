import sys
import threading
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import time

pose_dict = {
    "R_A1": [-0.034, 1.56, 0.99, 1.0], "R_A2": [-0.034, 1.56, 0.99, 1.0], "R_A3": [-0.034, 1.56, 0.99, 1.0],
    "R_B1": [0.566, 1.56, 0.99, 1.0], "R_B2": [0.566, 1.56, 0.99, 1.0], "R_B3": [0.566, 1.56, 0.99, 1.0],
    "R_C1": [1.166, 1.56, 0.99, 1.0], "R_C2": [1.166, 1.56, 0.99, 1.0], "R_C3": [1.166, 1.56, 0.99, 1.0],
    "R_D1": [-0.334, 0.96, 0.99, 1.0], "R_D2": [-0.334, 0.96, 0.99, 1.0], "R_D3": [-0.334, 0.96, 0.99, 1.0],
    "R_E1": [0.566, 0.96, 0.99, 1.0], "R_E2": [0.566, 0.96, 0.99, 1.0], "R_E3": [0.566, 0.96, 0.99, 1.0],
    "R_F1": [1.166, 0.96, 0.99, 1.0], "R_F2": [1.166, 0.96, 0.99, 1.0], "R_F3": [1.166, 0.96, 0.99, 1.0],
    "I1": [0.116, -1.11, 0.0, 1.0], "I2": [0.416, -1.11, 1.0, 0.0],
    "O1": [0.716, -1.11, 0.0, 1.0], "O2": [0.716, -1.11, 1.0, 0.0],
    "RH1": [0.0, 0.0, 0.0, 1.0], "RH2": [0.0, 0.0, 0.0, 1.0],
    "test": [0.84, -0.5, -0.00, 0.00]
}

class TargetPosePublisher(Node):
    def __init__(self):
        super().__init__('target_pose_publisher')
        self.publisher_ = self.create_publisher(PoseStamped, 'target_pose', 10)

    def publish_poses(self, poses):
        for key in poses:
            pose = pose_dict[key]
            msg = PoseStamped()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = 'map'
            msg.pose.position.x = pose[0]
            msg.pose.position.y = pose[1]
            msg.pose.orientation.z = pose[2]
            msg.pose.orientation.w = pose[3]
            self.publisher_.publish(msg)
            self.get_logger().info(f'Published target_pose: {key}')
            time.sleep(1)  # wait for 1 second between publishes

class MainWindow(QMainWindow):
    def __init__(self, publisher):
        super().__init__()
        self.publisher = publisher
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Target Pose Publisher')

        self.button = QPushButton('Publish Target Poses', self)
        self.button.setGeometry(50, 50, 200, 50)
        self.button.clicked.connect(self.publish_poses)

    def publish_poses(self):
        poses = ["R_A1", "R_B1", "R_D1", "O1"]  # 여기 코드에 상품이 검수 완료되고 로봇 호출/바코드 찍으면 자동으로 어펜드 되게
        self.publisher.publish_poses(poses)

def main(args=None):
    rclpy.init(args=args)
    publisher = TargetPosePublisher()

    app = QApplication(sys.argv)
    main_window = MainWindow(publisher)
    main_window.show()

    rclpy_thread = threading.Thread(target=rclpy.spin, args=(publisher,))
    rclpy_thread.start()

    sys.exit(app.exec_())

    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
