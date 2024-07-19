import cv2
from ultralytics import YOLO
import logging

class YoloDetector:
    def __init__(self, model_path='yolov5s.pt'):
        logging.getLogger("ultralytics").setLevel(logging.WARNING)
        self.model = YOLO(model_path)

    def detect_objects(self, image):
        results = self.model(image)
        return results
