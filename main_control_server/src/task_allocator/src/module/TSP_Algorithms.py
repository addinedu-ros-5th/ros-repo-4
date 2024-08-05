import numpy as np

# 최적 배터리 임계값 (작업 개수에 따라)
optimal_charge_thresholds = {
    1: 40,
    2: 50,
    3: 60
}

# 비용 계산 함수
def calculate_cost(robot, task_count):
    battery_factor = (100 - robot['battery_level']) / 100
    workload_factor = robot['total_workload'] / 3
    return battery_factor + workload_factor

# 경매 기반 작업 할당 함수
def auction_based_task_allocation(tasks, robots):
    task_allocations = []

    for task_id, (task_code, task_products) in enumerate(tasks.items()):
        task_count = len(task_products)  # 작업 개수
        charge_threshold = optimal_charge_thresholds[task_count]
        min_cost = float('inf')
        selected_robot = None

        for robot_name, robot in robots.items():
            if robot['status'] in ['오류 발생', '유지보수 중']:
                continue

            cost = calculate_cost(robot, task_count)
            if robot['status'] == '대기중' and robot['battery_level'] == 100:
                selected_robot = robot_name
                break
            elif robot['status'] == '충전중' and robot['battery_level'] >= charge_threshold:
                if cost < min_cost:
                    min_cost = cost
                    selected_robot = robot_name
            elif robot['status'] == '작업중':
                if (task_count == 1 and robot['battery_level'] >= 40) or \
                   (task_count == 2 and ((robot['total_workload'] == 1 and robot['battery_level'] >= 60) or 
                                         (robot['total_workload'] == 2 and robot['battery_level'] >= 60) or 
                                         (robot['total_workload'] == 3 and robot['battery_level'] >= 70))) or \
                   (task_count == 3 and ((robot['total_workload'] == 1 and robot['battery_level'] >= 90) or 
                                         (robot['total_workload'] == 2 and robot['battery_level'] >= 80) or 
                                         (robot['total_workload'] == 3 and robot['battery_level'] >= 70))):
                    if cost < min_cost:
                        min_cost = cost
                        selected_robot = robot_name

        # 적합한 로봇이 없으면 가장 낮은 비용을 제시한 로봇 선택
        if selected_robot is None:
            for robot_name, robot in robots.items():
                if robot['status'] not in ['오류 발생', '유지보수 중']:
                    cost = calculate_cost(robot, task_count)
                    if cost < min_cost:
                        min_cost = cost
                        selected_robot = robot_name

        if selected_robot is not None:
            # 선택된 로봇에 작업 할당 및 상태 업데이트
            robots[selected_robot]['status'] = '작업중'
            robots[selected_robot]['total_workload'] += task_count
            robots[selected_robot]['battery_level'] -= task_count * 10  # 작업 수행 시 배터리 소모
            task_allocations.append({
                'task_code': task_code,
                'robot_name': selected_robot,
                'task_products': task_products
            })
        else:
            task_allocations.append({
                'task_code': task_code,
                'robot_name': 'None',
                'task_products': [],
                'message': 'No suitable robot found'
            })

    return task_allocations


# # 예제 작업 리스트와 로봇 상태
# tasks = {
#     'T1': ['P01', 'P04', 'P07'],
#     'T2': ['P10', 'P13'],
#     'T3': ['P16']
# }

# robots = {
#     'Robo1': {'battery_level': 80, 'status': '대기중', 'total_workload': 0},
#     'Robo2': {'battery_level': 50, 'status': '충전중', 'total_workload': 0},
#     'Robo3': {'battery_level': 60, 'status': '작업중', 'total_workload': 1},
#     'Robo4': {'battery_level': 40, 'status': '충전중', 'total_workload': 0},
#     'Robo5': {'battery_level': 90, 'status': '대기중', 'total_workload': 0}
# }

# # 작업 할당 실행
# allocations = auction_based_task_allocation(tasks, robots)

# # 할당 결과 출력
# for allocation in allocations:
#     print(allocation)
