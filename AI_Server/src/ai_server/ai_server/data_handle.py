import numpy as np
import cv2
import json

class DataHandler:
    def __init__(self, client_socket):
        self.client_socket = client_socket

    def receive_data(self):
        try:
            total_length = self._receive_length()
            if total_length is None:
                return None, None

            image_length = self._receive_length()
            if image_length is None:
                return None, None

            image_data = self._receive_data(image_length)
            if image_data is None:
                return None, None

            lidar_length = self._receive_length()
            if lidar_length is None:
                return None, None

            lidar_data = self._receive_data(lidar_length)
            if lidar_data is None:
                return None, None

            # 이미지 데이터 디코딩
            np_array = np.frombuffer(image_data, np.uint8)
            cv_image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
            if cv_image is None:
                print("Failed to decode image data")
                return None, None

            # 라이다 데이터 디코딩
            lidar_json = json.loads(lidar_data.decode('utf-8'))

            return cv_image, lidar_json
        except Exception as e:
            print(f"Exception in receive_data: {e}")
            return None, None

    def _receive_length(self):
        try:
            length_data = self.client_socket.recv(4)
            if len(length_data) < 4:
                print("Failed to receive length data")
                return None
            return int.from_bytes(length_data, 'big')
        except Exception as e:
            print(f"Exception in _receive_length: {e}")
            return None

    def _receive_data(self, data_length):
        try:
            data = bytearray()
            while len(data) < data_length:
                packet = self.client_socket.recv(min(data_length - len(data), 4096))
                if not packet:
                    print("Failed to receive data packet")
                    return None
                data.extend(packet)
            return data
        except Exception as e:
            print(f"Exception in _receive_data: {e}")
            return None
