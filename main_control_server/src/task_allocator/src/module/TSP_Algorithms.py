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

# 물품의 위치
product_to_location = {
    "P01": "RA", "P02": "RA", "P03": "RA",
    "P04": "RB", "P05": "RB", "P06": "RB",
    "P07": "RC", "P08": "RC", "P09": "RC",
    "P10": "RD", "P11": "RD", "P12": "RD",
    "P13": "RE", "P14": "RE", "P15": "RE",
    "P16": "RF", "P17": "RF", "P18": "RF"
}


# 비용 계산 함수
def calculate_cost(robot):
    battery_factor = (100 - robot['battery_level']) / 100
    workload_factor = robot['total_workload']
    return battery_factor + workload_factor

# 경매 기반 작업 할당 함수
def auction_based_task_allocation(tasks, robots):
    task_allocations = []

    for task_id, (task_code, task_products) in enumerate(tasks.items()):
        task_racks = [product_to_location[product] for product in task_products]
        min_cost = float('inf')
        selected_robot = None

        for robot_name, robot in robots.items():
            if robot['status'] not in ['오류 발생', '유지보수 중']:
                cost = calculate_cost(robot)
                if cost < min_cost:
                    min_cost = cost
                    selected_robot = robot_name # 제일 값싼 친구가 누구야!!!


        if selected_robot is not None:
            task_allocations.append({
                'task_code': task_code,
                'robot_name': selected_robot,
                'rack_list': task_racks
            })
        else:
            task_allocations.append({
                'task_code': task_code,
                'robot_name': 'None',
                'rack_list': [],
                'message': 'No suitable robot found'
            })

    return task_allocations