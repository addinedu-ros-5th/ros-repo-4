import math

class DistanceCalculator:
    def calculate_distance(self, lidar_data, box, image_width, lidar_offset_forward, lidar_offset_downward):
        x_center = (box[0] + box[2]) // 2
        lidar_angle_min = -180.0
        lidar_angle_max = 180.0
        angle_range = lidar_angle_max - lidar_angle_min
        angle_per_pixel = angle_range / image_width
        lidar_angle = lidar_angle_min + (x_center * angle_per_pixel)
        min_distance = float('inf')
        for offset in range(-20, 21):
            angle_offset = lidar_angle + (offset * angle_per_pixel)
            angle_index = int((angle_offset - lidar_angle_min) / angle_range * len(lidar_data['ranges']))
            if 0 <= angle_index < len(lidar_data['ranges']):
                distance = lidar_data['ranges'][angle_index]
                if distance != float('inf') and distance > 0:
                    distance_corrected = math.sqrt(distance**2 - lidar_offset_forward**2 - lidar_offset_downward**2)
                    if distance_corrected < min_distance:
                        min_distance = distance_corrected
        return min_distance