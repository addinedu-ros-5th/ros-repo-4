# import pandas as pd

# # 비용 계산 함수
# def calculate_cost(robot, task_load):
#     battery_level = robot['battery_level']
#     workload_factor = robot['total_workload']
    
#     # 배터리 수준에 따른 비용 설정
#     if battery_level <= 20:
#         battery_factor = float('inf')  # 배터리 수준이 20 이하인 경우, 작업 할당 불가
#     elif battery_level <= 50:
#         battery_factor = 2.0  # 배터리 수준이 20~50 사이인 경우 비용 높음
#     elif battery_level <= 80:
#         battery_factor = 1.0  # 배터리 수준이 50~80 사이인 경우 비용 중간,
#     else:
#         battery_factor = 0.5  # 배터리 수준이 80 이상인 경우 비용 낮음

#     # 상태에 따른 추가 비용 설정
#     if robot['status'] == '작업중':
#         status_factor = 0.5
#     elif robot['status'] == '충전중':
#         if battery_level <= 20:
#             status_factor = float('inf')  # 충전 중이며 배터리 수준이 20 이하인 경우, 작업 할당 불가
#         elif battery_level <= 50:
#             status_factor = 0.5  # 충전 중이며 배터리 수준이 20~50 사이인 경우
#         elif battery_level <= 80:
#             status_factor = 0.2  # 충전 중이며 배터리 수준이 50~80 사이인 경우
#         else:
#             status_factor = 0.1  # 충전 중이며 배터리 수준이 80 이상인 경우
#     elif robot['status'] == '대기중':
#         status_factor = 0
#     elif robot['status'] == '오류' or robot['status'] == '유지보수 중':
#         status_factor = float('inf')  # 오류 또는 유지보수 중인 경우, 작업 할당 불가
#     else:
#         status_factor = 0  # 기본 상태 비용

#     total_cost = battery_factor + workload_factor + status_factor + task_load

#     return total_cost

# # 가능한 모든 경우의 수에 대해 비용 계산 및 결과 저장
# def evaluate_all_cases():
#     states = ["충전중", "오류", "유지보수 중", "대기중", "작업중"]
#     battery_levels = [0, 20, 40, 60, 80, 100]
#     task_loads = [1, 2, 3]
#     results = []

#     for state in states:
#         for battery_level in battery_levels:
#             for task_load in task_loads:
#                 # 작업중이 아닌 경우 task_load를 1로 고정
#                 if state != "작업중":
#                     task_load = 1

#                 robot = {
#                     'name': 'TestRobot',
#                     'battery_level': battery_level,
#                     'total_workload': 1,  # 가정: 현재 작업량은 1
#                     'status': state
#                 }

#                 cost = calculate_cost(robot, task_load)
#                 results.append({
#                     'State': state,
#                     'Battery': battery_level,
#                     'Task Load': task_load,
#                     'Cost': cost
#                 })

#     return pd.DataFrame(results)

# # 모든 경우의 수 평가
# df = evaluate_all_cases()

# # 비용을 기준으로 정렬
# df_sorted = df.sort_values(by='Cost').reset_index(drop=True)

# # 결과 출력
# print(df_sorted.to_string(index=False))
#----------------------------------------------------------- 모든 경우의 수 계산
import random
import pandas as pd

class Robot:
    def __init__(self, name, battery_level, status, task_load=0):
        self.name = name
        self.battery_level = battery_level
        self.status = status
        self.task_load = task_load
        self.total_cost = 0

    def can_perform_task(self, task_count):
        if self.status in ["유지보수", "오류"]:
            return False
        if self.battery_level < 20:
            return False
        if self.battery_level - task_count * 10 < 10:  # 작업 후에도 10% 이상 남아야 함
            return False
        return True

    def assign_task(self, task_count):
        if self.can_perform_task(task_count):
            self.task_load += task_count
            self.battery_level -= task_count * 10
            self.total_cost += task_count * 5  # 작업 비용
            self.status = "작업중" if self.task_load > 0 else self.status
        else:
            self.status = "충전중"
            self.charge()

    def perform_task(self):
        if self.status == "작업중" and self.task_load > 0:
            self.battery_level -= 10
            self.task_load -= 1
            self.total_cost += 5  # 작업 비용
            if self.battery_level <= 20:
                self.status = "충전중"
        elif self.status == "충전중":
            self.charge()

    def charge(self):
        if self.status == "충전중":
            self.battery_level = min(100, self.battery_level + 20)
            self.total_cost += 10  # 충전 비용
            if self.battery_level >= 50:
                self.status = "대기중"

def get_best_robot(robots, task_count, charge_threshold):
    eligible_robots = [robot for robot in robots if robot.can_perform_task(task_count)]
    if not eligible_robots:
        return None

    # 작업 개수와 task_load에 따른 우선순위 설정
    if task_count == 1:
        eligible_robots.sort(key=lambda r: (
            r.status == "충전중" and r.battery_level >= charge_threshold[0],
            r.status == "작업중" and r.task_load <= 3 and r.battery_level >= charge_threshold[0]
        ), reverse=True)
    elif task_count == 2:
        eligible_robots.sort(key=lambda r: (
            r.status == "충전중" and r.battery_level >= charge_threshold[1],
            r.status == "작업중" and r.task_load == 1 and r.battery_level >= charge_threshold[1] + 10,
            r.status == "작업중" and r.task_load == 2 and r.battery_level >= charge_threshold[1] + 10,
            r.status == "작업중" and r.task_load == 3 and r.battery_level >= charge_threshold[1] + 20
        ), reverse=True)
    elif task_count == 3:
        eligible_robots.sort(key=lambda r: (
            r.status == "충전중" and r.battery_level >= charge_threshold[2],
            r.status == "작업중" and r.task_load == 1 and r.battery_level >= charge_threshold[2] + 30,
            r.status == "작업중" and r.task_load == 2 and r.battery_level >= charge_threshold[2] + 20,
            r.status == "작업중" and r.task_load == 3 and r.battery_level >= charge_threshold[2] + 10
        ), reverse=True)

    return eligible_robots[0] if eligible_robots else None

def simulate_operations(robots, task_assignments, charge_threshold):
    for task_count in task_assignments:
        best_robot = get_best_robot(robots, task_count, charge_threshold)
        if best_robot:
            best_robot.assign_task(task_count)
        else:
            print(f"No available robot for task count: {task_count}")

    total_cost = sum(robot.total_cost for robot in robots)
    return total_cost

def find_optimal_strategy():
    best_costs = {1: float('inf'), 2: float('inf'), 3: float('inf')}
    best_strategies = {1: None, 2: None, 3: None}

    results = []
    
    charge_thresholds = [
        (40, 50, 60),  # 테스트할 다양한 배터리 임계값
        (50, 60, 70),
        (60, 70, 80),
        (70, 80, 90)
    ]

    for charge_threshold in charge_thresholds:
        for task_count in [1, 2, 3]:
            for task_load in [1, 2, 3]:
                robots = [Robot(f"Robo{i}", random.choice([0, 10, 20, 30, 40, 50, 60, 70]), 
                                random.choice(["충전중", "작업중"]), task_load if random.choice(["충전중", "작업중"]) == "작업중" else 0) for i in range(10)]
                total_cost = simulate_operations(robots, [task_count]*10, charge_threshold)
                results.append((task_count, task_load, charge_threshold, total_cost))
                print(f"Task Count: {task_count}, Task Load: {task_load}, Charge Threshold: {charge_threshold}, Total Cost: {total_cost}")
                
                if total_cost < best_costs[task_count]:
                    best_costs[task_count] = total_cost
                    best_strategies[task_count] = (task_load, charge_threshold)

    return best_strategies, best_costs, results

# 최적 전략 찾기
best_strategies, best_costs, results = find_optimal_strategy()

for task_count in best_strategies:
    print(f"Optimal Strategy for Task Count: {task_count} with Task Load: {best_strategies[task_count][0]} and Charge Threshold: {best_strategies[task_count][1]}, Best Cost: {best_costs[task_count]}")

# 결과 데이터를 pandas DataFrame으로 변환
df_results = pd.DataFrame(results, columns=["Task Count", "Task Load", "Charge Threshold", "Total Cost"])
print(df_results)

# 결과 데이터 저장 (원하는 경우 CSV로 저장)
# df_results.to_csv("simulation_results.csv", index=False)

