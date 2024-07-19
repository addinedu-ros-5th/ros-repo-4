import cv2 as cv
import numpy as np

# 캘리브레이션 데이터 경로 설정
calib_data_path = "../calib_data/MultiMatrix.npz"

# 캘리브레이션 데이터 로드
calib_data = np.load(calib_data_path)
print(calib_data.files)

# 캘리브레이션 데이터 추출
cam_mat = calib_data["camMatrix"]
dist_coef = calib_data["distCoef"]
r_vectors = calib_data["rVector"]
t_vectors = calib_data["tVector"]

MARKER_SIZE = 7.5  # 센티미터 단위 #5.3, 3.2

# 아루코 마커 사전 및 감지 파라미터 설정
dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_50)
parameters = cv.aruco.DetectorParameters()
detector = cv.aruco.ArucoDetector(dictionary, parameters)

# 카메라 캡처 시작
cap = cv.VideoCapture(0)

# 3D 아루코 마커의 각 코너의 실제 좌표 (마커가 평면에 놓여 있다고 가정)
marker_corners_3d = np.array([
    [-MARKER_SIZE / 2, MARKER_SIZE / 2, 0],
    [MARKER_SIZE / 2, MARKER_SIZE / 2, 0],
    [MARKER_SIZE / 2, -MARKER_SIZE / 2, 0],
    [-MARKER_SIZE / 2, -MARKER_SIZE / 2, 0]
], dtype=np.float32)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, reject = detector.detectMarkers(gray_frame)
    
    if marker_corners:
        for marker_corner, marker_id in zip(marker_corners, marker_IDs):
            # 각 마커의 2D 코너를 1D 배열로 변환
            marker_corner_2d = marker_corner.reshape(-1, 2).astype(np.float32)

            # cv.solvePnP를 사용하여 포즈 추정
            ret, rVec, tVec = cv.solvePnP(
                marker_corners_3d, marker_corner_2d, cam_mat, dist_coef
            )

            # 마커의 포즈 그리기
            cv.polylines(
                frame, [marker_corner.astype(np.int32)], True, (0, 255, 255), 4, cv.LINE_AA
            )
            corners = marker_corner.reshape(4, 2)
            corners = corners.astype(int)
            top_right = corners[0].ravel()
            top_left = corners[1].ravel()
            bottom_right = corners[2].ravel()
            bottom_left = corners[3].ravel()

            # 거리 계산
            distance = np.sqrt(
                tVec[0][0] ** 2 + tVec[1][0] ** 2 + tVec[2][0] ** 2
            )
            # 마커의 포즈 그리기
            point = cv.drawFrameAxes(frame, cam_mat, dist_coef, rVec, tVec, 4, 4)
            cv.putText(
                frame,
                f"id: {marker_id[0]} Dist: {round(distance, 2)}",
                top_right,
                cv.FONT_HERSHEY_PLAIN,
                1.3,
                (0, 0, 255),
                2,
                cv.LINE_AA,
            )
            cv.putText(
                frame,
                f"x:{round(tVec[0][0],1)} y: {round(tVec[1][0],1)} z: {round(tVec[2][0],1)}",
                bottom_right,
                cv.FONT_HERSHEY_PLAIN,
                1.0,
                (0, 0, 255),
                2,
                cv.LINE_AA,
            )
            # print(marker_id, "  ", corners)
    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key == ord("q"):
        break
cap.release()
cv.destroyAllWindows()
