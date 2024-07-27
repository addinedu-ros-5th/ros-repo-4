import sys
import threading
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, PoseArray, Pose
from PyQt5.QtWidgets import *
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
        self.publisher_ = self.create_publisher(PoseArray, 'target_poses', 10)

    def publish_poses(self, poses):
        pose_array_msg = PoseArray()
        pose_array_msg.header.stamp = self.get_clock().now().to_msg()
        pose_array_msg.header.frame_id = 'map'

        for key in poses:
            pose = pose_dict[key]
            pose_msg = Pose()
            pose_msg.position.x = pose[0]
            pose_msg.position.y = pose[1]
            pose_msg.orientation.z = pose[2]
            pose_msg.orientation.w = pose[3]
            pose_array_msg.poses.append(pose_msg)

        self.publisher_.publish(pose_array_msg)
        self.get_logger().info(f'Published target_poses: {poses}')

class MainWindow(QMainWindow):
    def __init__(self, publisher):
        super().__init__()
        self.publisher = publisher
        self.selected_poses = []
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Target Pose Publisher')

        layout = QVBoxLayout()

        self.pose_list = QListWidget()
        for key in pose_dict.keys():
            self.pose_list.addItem(key)
        layout.addWidget(self.pose_list)

        self.selected_pose_list = QListWidget()
        layout.addWidget(self.selected_pose_list)

        self.add_button = QPushButton('Add Pose', self)
        self.add_button.clicked.connect(self.add_pose)
        layout.addWidget(self.add_button)

        self.remove_button = QPushButton('Remove Selected Pose', self)
        self.remove_button.clicked.connect(self.remove_pose)
        layout.addWidget(self.remove_button)

        self.publish_button = QPushButton('Publish Poses', self)
        self.publish_button.clicked.connect(self.publish_poses)
        layout.addWidget(self.publish_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_pose(self):
        selected_items = self.pose_list.selectedItems()
        for item in selected_items:
            self.selected_poses.append(item.text())
            self.selected_pose_list.addItem(item.text())
            self.pose_list.takeItem(self.pose_list.row(item))

    def remove_pose(self):
        selected_items = self.selected_pose_list.selectedItems()
        for item in selected_items:
            self.selected_poses.remove(item.text())
            self.pose_list.addItem(item.text())
            self.selected_pose_list.takeItem(self.selected_pose_list.row(item))

    def publish_poses(self):
        if self.selected_poses:
            self.publisher.publish_poses(self.selected_poses)
            self.selected_poses = []  # Clear the list after publishing
            self.selected_pose_list.clear()

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


# 이름도 같이 발행되게 하는 코드
# import sys
# import threading
# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import PoseStamped, Pose
# from std_msgs.msg import String, Header
# from PyQt5.QtWidgets import *
# import time

# pose_dict = {
#     "R_A1": [-0.034, 1.56, 0.99, 1.0], "R_A2": [-0.034, 1.56, 0.99, 1.0], "R_A3": [-0.034, 1.56, 0.99, 1.0],
#     "R_B1": [0.566, 1.56, 0.99, 1.0], "R_B2": [0.566, 1.56, 0.99, 1.0], "R_B3": [0.566, 1.56, 0.99, 1.0],
#     "R_C1": [1.166, 1.56, 0.99, 1.0], "R_C2": [1.166, 1.56, 0.99, 1.0], "R_C3": [1.166, 1.56, 0.99, 1.0],
#     "R_D1": [-0.334, 0.96, 0.99, 1.0], "R_D2": [-0.334, 0.96, 0.99, 1.0], "R_D3": [-0.334, 0.96, 0.99, 1.0],
#     "R_E1": [0.566, 0.96, 0.99, 1.0], "R_E2": [0.566, 0.96, 0.99, 1.0], "R_E3": [0.566, 0.96, 0.99, 1.0],
#     "R_F1": [1.166, 0.96, 0.99, 1.0], "R_F2": [1.166, 0.96, 0.99, 1.0], "R_F3": [1.166, 0.96, 0.99, 1.0],
#     "I1": [0.116, -1.11, 0.0, 1.0], "I2": [0.416, -1.11, 1.0, 0.0],
#     "O1": [0.716, -1.11, 0.0, 1.0], "O2": [0.716, -1.11, 1.0, 0.0],
#     "RH1": [0.0, 0.0, 0.0, 1.0], "RH2": [0.0, 0.0, 0.0, 1.0],
#     "test": [0.84, -0.5, -0.00, 0.00]
# }

# class TargetPosePublisher(Node):
#     def __init__(self):
#         super().__init__('target_pose_publisher')
#         self.publisher_ = self.create_publisher(PoseArray, 'target_poses', 10)
#         self.name_publisher_ = self.create_publisher(String, 'target_pose_names', 10)

#     def publish_poses(self, poses):
#         pose_array_msg = PoseArray()
#         pose_array_msg.header.stamp = self.get_clock().now().to_msg()
#         pose_array_msg.header.frame_id = 'map'
        
#         names = []

#         for key in poses:
#             pose = pose_dict[key]
#             pose_msg = Pose()
#             pose_msg.position.x = pose[0]
#             pose_msg.position.y = pose[1]
#             pose_msg.orientation.z = pose[2]
#             pose_msg.orientation.w = pose[3]
#             pose_array_msg.poses.append(pose_msg)
#             names.append(key)

#         self.publisher_.publish(pose_array_msg)
#         names_msg = String()
#         names_msg.data = ','.join(names)
#         self.name_publisher_.publish(names_msg)
#         self.get_logger().info(f'Published target_poses: {names}')

# class MainWindow(QMainWindow):
#     def __init__(self, publisher):
#         super().__init__()
#         self.publisher = publisher
#         self.selected_poses = []
#         self.initUI()

#     def initUI(self):
#         self.setGeometry(100, 100, 300, 400)
#         self.setWindowTitle('Target Pose Publisher')

#         layout = QVBoxLayout()

#         self.pose_list = QListWidget()
#         for key in pose_dict.keys():
#             self.pose_list.addItem(key)
#         layout.addWidget(self.pose_list)

#         self.selected_pose_list = QListWidget()
#         layout.addWidget(self.selected_pose_list)

#         self.add_button = QPushButton('Add Pose', self)
#         self.add_button.clicked.connect(self.add_pose)
#         layout.addWidget(self.add_button)

#         self.remove_button = QPushButton('Remove Selected Pose', self)
#         self.remove_button.clicked.connect(self.remove_pose)
#         layout.addWidget(self.remove_button)

#         self.publish_button = QPushButton('Publish Poses', self)
#         self.publish_button.clicked.connect(self.publish_poses)
#         layout.addWidget(self.publish_button)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#     def add_pose(self):
#         selected_items = self.pose_list.selectedItems()
#         for item in selected_items:
#             self.selected_poses.append(item.text())
#             self.selected_pose_list.addItem(item.text())
#             self.pose_list.takeItem(self.pose_list.row(item))

#     def remove_pose(self):
#         selected_items = self.selected_pose_list.selectedItems()
#         for item in selected_items:
#             self.selected_poses.remove(item.text())
#             self.pose_list.addItem(item.text())
#             self.selected_pose_list.takeItem(self.selected_pose_list.row(item))

#     def publish_poses(self):
#         if self.selected_poses:
#             self.publisher.publish_poses(self.selected_poses)
#             self.selected_poses = []  # Clear the list after publishing
#             self.selected_pose_list.clear()

# def main(args=None):
#     rclpy.init(args=args)
#     publisher = TargetPosePublisher()

#     app = QApplication(sys.argv)
#     main_window = MainWindow(publisher)
#     main_window.show()

#     rclpy_thread = threading.Thread(target=rclpy.spin, args=(publisher,))
#     rclpy_thread.start()

#     sys.exit(app.exec_())

#     publisher.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()
