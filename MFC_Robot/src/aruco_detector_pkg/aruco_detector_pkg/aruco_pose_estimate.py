import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2 as cv
import numpy as np
import os
from ament_index_python.packages import get_package_share_directory
import time

class ArucoCmdVelPublisher(Node):
    def __init__(self, robot_id, image_topic, calib_file, cmd_vel_topic, arrive_topic, result_topic):
        super().__init__(f'aruco_cmd_vel_publisher_{robot_id}')
        self.robot_id = robot_id
        self.bridge = CvBridge()
        self.marker_size = 3.1
        self.angle_aligned = False
        self.result_state = "STOPPED"
        self.last_stationary_time = None

        # 캘리브레이션 파일 경로
        package_share_directory = get_package_share_directory('aruco_detector_pkg')
        calib_data_path = os.path.join(package_share_directory, 'calib_data', calib_file)

        # 캘리브레이션 데이터 로드
        calib_data = np.load(calib_data_path)
        self.cam_mat = calib_data["camMatrix"]
        self.dist_coef = calib_data["distCoef"]

        # 아루코 마커 사전 및 감지 파라미터 설정
        self.dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_50)
        self.parameters = cv.aruco.DetectorParameters()
        self.detector = cv.aruco.ArucoDetector(self.dictionary, self.parameters)

        # 이미지 토픽 구독 설정
        self.image_subscription = self.create_subscription(
            Image,
            image_topic,
            self.image_callback,
            10
        )

        # cmd_vel 퍼블리셔
        self.cmd_vel_publisher = self.create_publisher(Twist, cmd_vel_topic, 10)
        self.result_subscription = self.create_subscription(
            String,
            result_topic,
            self.result_callback,
            10
        )
        self.adjustment_complete_publisher = self.create_publisher(String, arrive_topic, 10)

        self.get_logger().info(f'Robot {robot_id} ArucoCmdVelPublisher initialized.')

    def result_callback(self, msg):
        self.result_state = msg.data
        self.get_logger().info(f'결과 상태가 업데이트됨: {self.result_state}')

    def image_callback(self, msg):
        if self.result_state != "ADJUSTING":
            self.get_logger().info('현재 아루코 마커 감지가 허용되지 않습니다.')
            return

        try:
            frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
            gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            marker_corners, marker_IDs, _ = self.detector.detectMarkers(gray_frame)

            if marker_corners:
                for marker_corner, marker_id in zip(marker_corners, marker_IDs):
                    marker_corner_2d = marker_corner.reshape(-1, 2).astype(np.float32)
                    ret, rVec, tVec = cv.solvePnP(self.get_marker_corners_3d(), marker_corner_2d, self.cam_mat, self.dist_coef)

                    if ret:
                        twist = Twist()
                        if not self.angle_aligned:
                            center_x = (marker_corner_2d[0][0] + marker_corner_2d[2][0]) / 2.0
                            frame_center_x = frame.shape[1] / 2.0
                            error_x = center_x - frame_center_x
                            self.get_logger().info(f'오차 x: {error_x}')

                            if abs(error_x) > 10:
                                twist.angular.z = -0.002 * error_x
                                twist.linear.x = 0.0
                            else:
                                self.angle_aligned = True
                                twist.angular.z = 0.0
                                twist.linear.x = 0.0
                            self.cmd_vel_publisher.publish(twist)
                        else:
                            distance = np.sqrt(tVec[0][0]**2 + tVec[1][0]**2 + tVec[2][0]**2)
                            if distance > 20:
                                twist.linear.x = 0.1
                                twist.angular.z = 0.0
                            elif distance < 15:
                                twist.linear.x = -0.1
                                twist.angular.z = 0.0
                            else:
                                twist.linear.x = 0.0
                                twist.angular.z = 0.0
                                self.angle_aligned = False
                                self.last_stationary_time = time.time()
                            self.cmd_vel_publisher.publish(twist)
                    else:
                        self.get_logger().error('포즈 추정 실패.')
            else:
                self.get_logger().info('마커가 검출되지 않음.')

        except Exception as e:
            self.get_logger().error(f'이미지 처리 오류: {e}')

        if self.last_stationary_time and (time.time() - self.last_stationary_time) >= 2:
            self.publish_adjustment_complete()
            self.result_state = "STOPPED"

    def get_marker_corners_3d(self):
        return np.array([
            [-self.marker_size / 2, self.marker_size / 2, 0],
            [self.marker_size / 2, self.marker_size / 2, 0],
            [self.marker_size / 2, -self.marker_size / 2, 0],
            [-self.marker_size / 2, -self.marker_size / 2, 0]
        ], dtype=np.float32)

    def publish_adjustment_complete(self):
        self.get_logger().info('조정 완료 메시지 발행 중.')
        msg = String()
        msg.data = "complete"
        self.adjustment_complete_publisher.publish(msg)
        self.last_stationary_time = None

def main(args=None):
    rclpy.init(args=args)
    executor = MultiThreadedExecutor()

    robot_1_node = ArucoCmdVelPublisher(robot_id=1, 
                                        image_topic='/camera/image_raw_1', 
                                        calib_file='MultiMatrix.npz', 
                                        cmd_vel_topic='/base_controller/cmd_vel_unstamped_1', 
                                        arrive_topic='/arrive_topic_1', 
                                        result_topic='/result_topic_1')

    robot_2_node = ArucoCmdVelPublisher(robot_id=2, 
                                        image_topic='/camera/image_raw_2', 
                                        calib_file='MultiMatrix.npz', 
                                        cmd_vel_topic='/base_controller/cmd_vel_unstamped_2', 
                                        arrive_topic='/arrive_topic_2', 
                                        result_topic='/result_topic_2')

    executor.add_node(robot_1_node)
    executor.add_node(robot_2_node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        robot_1_node.destroy_node()
        robot_2_node.destroy_node()
        rclpy.shutdown()
        cv.destroyAllWindows()

if __name__ == '__main__':
    main()
