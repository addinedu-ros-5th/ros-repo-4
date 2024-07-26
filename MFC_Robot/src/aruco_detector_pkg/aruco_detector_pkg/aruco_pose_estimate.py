import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2 as cv
import numpy as np
import os
from ament_index_python.packages import get_package_share_directory

class ArucoCmdVelPublisher(Node):
    def __init__(self):
        super().__init__('aruco_cmd_vel_publisher')
        self.get_logger().info('ArucoCmdVelPublisher node has been started.')

        self.bridge = CvBridge()
        self.marker_size = 3.1  # 센티미터 단위
        self.angle_aligned = False  # 각도 조정 완료 여부

        try:
            package_share_directory = get_package_share_directory('aruco_detector_pkg')
            calib_data_path = os.path.join(package_share_directory, 'calib_data', 'MultiMatrix.npz')

            # 캘리브레이션 데이터 로드
            calib_data = np.load(calib_data_path)
            self.cam_mat = calib_data["camMatrix"]
            self.dist_coef = calib_data["distCoef"]

            # 아루코 마커 사전 및 감지 파라미터 설정
            self.dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_50)
            self.parameters = cv.aruco.DetectorParameters()
            self.detector = cv.aruco.ArucoDetector(self.dictionary, self.parameters)

            # 이미지를 subscribe
            self.image_subscription = self.create_subscription(
                Image,
                '/camera/image_raw',
                self.image_callback,
                10
            )

            # cmd_vel 퍼블리셔
            self.cmd_vel_publisher = self.create_publisher(Twist, 'base_controller/cmd_vel_unstamped', 10)

            self.get_logger().info('Initialization complete.')
        
        except Exception as e:
            self.get_logger().error(f'Error during initialization: {e}')

    def image_callback(self, msg):
        try:
            # 이미지 메시지를 OpenCV 이미지로 변환
            frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
            gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            # 아루코 마커 검출 및 코너 좌표 추출
            marker_corners, marker_IDs, _ = self.detector.detectMarkers(gray_frame)

            if marker_corners:
                for marker_corner, marker_id in zip(marker_corners, marker_IDs):
                    # 각 마커의 2D 코너를 1D 배열로 변환
                    marker_corner_2d = marker_corner.reshape(-1, 2).astype(np.float32)

                    # PnP 알고리즘을 사용한 포즈 추정
                    ret, rVec, tVec = cv.solvePnP(
                        self.get_marker_corners_3d(), marker_corner_2d, self.cam_mat, self.dist_coef
                    )

                    if ret:
                        if not self.angle_aligned:
                            # 마커의 중심 좌표 계산
                            center_x = (marker_corner_2d[0][0] + marker_corner_2d[2][0]) / 2.0
                            frame_center_x = frame.shape[1] / 2.0
                            error_x = center_x - frame_center_x

                            self.get_logger().info(f'Error x: {error_x}')

                            twist = Twist()
                            if abs(error_x) > 10:  # 임계값 설정
                                # 마커의 중심이 프레임의 중심과 일치하지 않는 경우 회전
                                twist.angular.z = -0.002 * error_x
                                twist.linear.x = 0.0
                            else:
                                self.angle_aligned = True
                                twist.angular.z = 0.0
                                twist.linear.x = 0.0

                            self.cmd_vel_publisher.publish(twist)
                        else:
                            # 마커와의 거리가 20cm보다 크면 전진, 작으면 후진
                            distance = np.sqrt(tVec[0][0]**2 + tVec[1][0]**2 + tVec[2][0]**2)
                            twist = Twist()
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

                            self.cmd_vel_publisher.publish(twist)

                    else:
                        self.get_logger().error('Pose estimation failed.')

            else:
                self.get_logger().info('No markers detected.')
            
            # OpenCV를 사용하여 화면에 이미지 표시
            # cv.imshow('Aruco Detection', frame)
            # cv.waitKey(1)
        
        except Exception as e:
            self.get_logger().error(f'Error in process_image: {e}')


    def get_marker_corners_3d(self):
        return np.array([
            [-self.marker_size / 2, self.marker_size / 2, 0],
            [self.marker_size / 2, self.marker_size / 2, 0],
            [self.marker_size / 2, -self.marker_size / 2, 0],
            [-self.marker_size / 2, -self.marker_size / 2, 0]
        ], dtype=np.float32)

def main(args=None):
    rclpy.init(args=args)
    node = ArucoCmdVelPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

    # OpenCV 창 닫기
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
