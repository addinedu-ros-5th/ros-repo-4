import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from std_msgs.msg import String  # String 메시지 타입을 임포트
from cv_bridge import CvBridge
import cv2 as cv
import numpy as np
import os
from ament_index_python.packages import get_package_share_directory
import time  # 시간 모듈 임포트

class ArucoCmdVelPublisher(Node):
    def __init__(self):
        super().__init__('aruco_cmd_vel_publisher')
        self.get_logger().info('ArucoCmdVelPublisher 노드가 시작되었습니다.')

        self.bridge = CvBridge()
        self.marker_size = 3.1  # 센티미터 단위
        self.angle_aligned = False  # 각도 조정 완료 여부
        self.result_state = "STOPPED"  # 초기 상태
        self.last_stationary_time = None  # 마지막으로 정지한 시간 초기화

        try:
            package_share_directory = get_package_share_directory('aruco_detector_pkg')
            calib_data_path = os.path.join(package_share_directory, 'calib_data', 'MultiMatrix_ys.npz')

            # 캘리브레이션 데이터 로드
            calib_data = np.load(calib_data_path)
            self.cam_mat = calib_data["camMatrix"]
            self.dist_coef = calib_data["distCoef"]

            # 아루코 마커 사전 및 감지 파라미터 설정
            self.dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_50)
            self.parameters = cv.aruco.DetectorParameters()

            # 이미지를 subscribe
            self.image_subscription = self.create_subscription(
                Image,
                '/camera/image_raw',
                self.image_callback,
                10
            )

            # cmd_vel 퍼블리셔
            self.cmd_vel_publisher = self.create_publisher(Twist, 'base_controller/cmd_vel_unstamped', 10)

            # result_topic을 subscribe
            self.result_subscription = self.create_subscription(
                String,
                'result_topic',
                self.result_callback,
                10
            )

            # 조정완료 토픽 퍼블리셔
            self.adjustment_complete_publisher = self.create_publisher(String, 'arrive_topic', 10)

            self.get_logger().info('초기화 완료.')

        except Exception as e:
            self.get_logger().error(f'초기화 중 오류: {e}')

    def result_callback(self, msg):
        self.result_state = msg.data
        self.get_logger().info(f'결과 상태가 업데이트됨: {self.result_state}')

    def image_callback(self, msg):
        if self.result_state != "ADJUSTING":
            self.get_logger().info('현재 아루코 마커 감지가 허용되지 않습니다.')
            return

        try:
            # 이미지 메시지를 OpenCV 이미지로 변환
            frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
            gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            # 아루코 마커 검출 및 코너 좌표 추출
            marker_corners, marker_IDs, _ = cv.aruco.detectMarkers(gray_frame, self.dictionary, parameters=self.parameters)

            if marker_corners:
                for marker_corner, marker_id in zip(marker_corners, marker_IDs):
                    # 각 마커의 2D 코너를 1D 배열로 변환
                    marker_corner_2d = marker_corner.reshape(-1, 2).astype(np.float32)

                    # PnP 알고리즘을 사용한 포즈 추정
                    ret, rVec, tVec = cv.solvePnP(
                        self.get_marker_corners_3d(), marker_corner_2d, self.cam_mat, self.dist_coef
                    )

                    if ret:
                        twist = Twist()
                        if not self.angle_aligned:
                            # 마커의 중심 좌표 계산
                            center_x = (marker_corner_2d[0][0] + marker_corner_2d[2][0]) / 2.0
                            frame_center_x = frame.shape[1] / 2.0
                            error_x = center_x - frame_center_x

                            self.get_logger().info(f'오차 x: {error_x}')

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
                                self.last_stationary_time = time.time()  # 로봇이 정지한 시간을 기록

                            self.cmd_vel_publisher.publish(twist)

                    else:
                        self.get_logger().error('포즈 추정 실패.')

            else:
                self.get_logger().info('마커가 검출되지 않음.')

        except Exception as e:
            self.get_logger().error(f'이미지 처리 오류: {e}')

        # 로봇이 3초 동안 정지 상태인지 확인
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
        self.last_stationary_time = None  # 정지 시간을 초기화

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
