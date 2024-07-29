import math
from collections import defaultdict

# 렉의 좌표 (3열 2행 배치)
rack_coordinates = {
    "A": (0, 0), "B": (1, 0), "C": (2, 0),
    "D": (0, 1), "E": (1, 1), "F": (2, 1),
}

# 제품 코드를 렉 위치로 매핑
product_to_location = {
    "P01": "A", "P02": "A", "P03": "A",
    "P04": "B", "P05": "B", "P06": "B",
    "P07": "C", "P08": "C", "P09": "C",
    "P10": "D", "P11": "D", "P12": "D",
    "P13": "E", "P14": "E", "P15": "E",
    "P16": "F", "P17": "F", "P18": "F",
}

def calculate_distance(rack1, rack2):
    x1, y1 = rack_coordinates[rack1]
    x2, y2 = rack_coordinates[rack2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def group_items(order_list):
    # 렉 별로 아이템을 그룹화
    rack_to_items = defaultdict(list)
    for item in order_list:
        rack_to_items[product_to_location[item]].append(item)
    
    tasks = []
    used_items = set()
    
    # 같은 렉에 있는 아이템을 우선으로 그룹화
    for rack, items in rack_to_items.items():
        if len(items) >= 3:
            for i in range(0, len(items), 3):
                task_items = items[i:i+3]
                if len(task_items) == 3:
                    tasks.append(task_items)
                    used_items.update(task_items)
    
    # 사용되지 않은 아이템들을 인접한 렉의 아이템들과 그룹화
    remaining_items = [item for item in order_list if item not in used_items]
    remaining_items_by_rack = defaultdict(list)
    for item in remaining_items:
        remaining_items_by_rack[product_to_location[item]].append(item)
    
    for rack, items in remaining_items_by_rack.items():
        if len(items) == 2:
            closest_racks = sorted(rack_coordinates.keys(), key=lambda x: calculate_distance(rack, x))
            for closest_rack in closest_racks:
                if closest_rack != rack and closest_rack in remaining_items_by_rack and len(remaining_items_by_rack[closest_rack]) > 0:
                    task_items = items + [remaining_items_by_rack[closest_rack][0]]
                    tasks.append(task_items)
                    used_items.update(task_items)
                    remaining_items_by_rack[closest_rack] = remaining_items_by_rack[closest_rack][1:]
                    break
    
    # 남은 아이템 그룹화
    remaining_items = [item for item in order_list if item not in used_items]
    for i in range(0, len(remaining_items), 3):
        task_items = remaining_items[i:i+3]
        if task_items:
            tasks.append(task_items)
    
    return tasks

# 입고 리스트 예시
order_list = ["P02", "P08", "P15", "P10", "P04", "P01", "P03", "P06", "P07"]

# 물품 짝짓기
tasks = group_items(order_list)
for i, task in enumerate(tasks):
    print(f"Task {i+1}: {task}")