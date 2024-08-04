import numpy as np

# 6개의 원을 3행 2열로 배치
positions = {
    'RA': (0, 1),
    'RB': (0, 2),
    'RC': (0, 3),
    'RD': (1, 1),
    'RE': (1, 2),
    'RF': (1, 3)
}

# 로봇 정보
robots = {
    'Robo1': {'battery_level': 80, 'position': 'RD', 'total_workload': 2},
    'Robo2': {'battery_level': 60, 'position': 'RE', 'total_workload': 1},
    'Robo3': {'battery_level': 50, 'position': 'RF', 'total_workload': 3}
}

# 물품의 위치
product_to_location = {
    "P01": "RA", "P02": "RA", "P03": "RA",
    "P04": "RB", "P05": "RB", "P06": "RB",
    "P07": "RC", "P08": "RC", "P09": "RC",
    "P10": "RD", "P11": "RD", "P12": "RD",
    "P13": "RE", "P14": "RE", "P15": "RE",
    "P16": "RF", "P17": "RF", "P18": "RF"
}

# # 거리 계산 함수
# def calculate_distance(pos1, pos2):
#     return np.linalg.norm(np.array(pos1) - np.array(pos2))

# 비용 계산 함수
def calculate_cost(robot, task_racks, positions, max_distance):
    battery_factor = (100 - robot['battery_level']) / 100
    distance_factor = sum(calculate_distance(positions[robot['position']], positions[rack]) for rack in task_racks) / max_distance
    workload_factor = robot['total_workload'] / 3
    return battery_factor + distance_factor + workload_factor

# 경매 기반 작업 할당 함수
def auction_based_task_allocation(tasks, robots, positions):
    max_distance = max(calculate_distance(positions[r1], positions[r2]) for r1 in positions for r2 in positions)
    task_allocations = []

    for task_id, (task_code, task_products) in enumerate(tasks.items()):
        task_racks = [product_to_location[product] for product in task_products]
        print(f"\nStarting auction for {task_code} with racks {task_racks}")
        min_cost = float('inf')
        selected_robot = None
        for robot_name, robot in robots.items():
            cost = calculate_cost(robot, task_racks, positions, max_distance)
            print(f"  Robot {robot_name} cost calculation: {cost:.4f} (Battery: {(100 - robot['battery_level']) / 100:.2f}, Distance: {sum(calculate_distance(positions[robot['position']], positions[rack]) for rack in task_racks) / max_distance:.2f}, Workload: {robot['total_workload'] / 3:.2f})")
            if cost < min_cost:
                min_cost = cost
                selected_robot = robot_name
        robots[selected_robot]['total_workload'] += len(task_racks)
        robots[selected_robot]['position'] = task_racks[-1]  # 마지막 위치로 로봇의 위치 업데이트
        task_allocations.append({
            'task_code': task_code,
            'robot_name': selected_robot,
            'rack_list': task_racks
        })
        print(f"  {task_code} assigned to {selected_robot} with cost {min_cost:.4f}")

    return task_allocations

# 메인 함수
def main():
    # 예제 작업 리스트
    tasks = {
        'Task_1': ['P16', 'P17', 'P18'],
        'Task_2': ['P10', 'P11'],
        'Task_3': ['P01', 'P02', 'P03']
    }

    # 경매 기반 작업 할당
    task_allocations = auction_based_task_allocation(tasks, robots, positions)

    for allocation in task_allocations:
        print(f"\nTask Code: {allocation['task_code']}")
        print(f"Assigned Robot: {allocation['robot_name']}")
        print(f"Rack List: {allocation['rack_list']}")
        print(f"Task Assignment: 입고")

if __name__ == "__main__":
    main()
