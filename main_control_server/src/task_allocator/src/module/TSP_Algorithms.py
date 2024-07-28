import random
from collections import Counter
import numpy as np
from itertools import permutations
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation

# 6개의 원을 3행 2열로 배치
positions = {
    0: (0, 0),
    1: (0, 1),
    2: (1, 0),
    3: (1, 1),
    4: (2, 0),
    5: (2, 1)
}



# 원 선택 함수
def select_nodes(max_n, max_copies):
    selected_nodes = []
    while len(selected_nodes) < max_n:
        node = random.choice(list(positions.keys()))
        if selected_nodes.count(node) < max_copies:
            selected_nodes.append(node)
    return selected_nodes

# 두 대의 로봇에게 품목을 나누어 주기
def distribute_items_among_robots(selected_items):
    item_counts = Counter(selected_items)
    robot1, robot2 = [], []

    for item, count in item_counts.items():
        while count > 0:
            if len(robot1) < 3:
                robot1.append(item)
            elif len(robot2) < 3:
                robot2.append(item)
            else:
                break
            count -= 1

    return robot1, robot2

# 로봇 동선을 위한 전체 계획 세우기
def plan_robot_routes(selected_items):
    tasks = []
    while selected_items:
        robot1, robot2 = distribute_items_among_robots(selected_items[:6])
        tasks.append((robot1, robot2))
        selected_items = selected_items[6:]
    return tasks

# 거리 행렬 생성 함수
def create_distance_matrix(nodes, positions):
    n = len(nodes)
    dists = np.zeros((n, n))
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if i != j:
                dists[i][j] = np.linalg.norm(np.array(positions[u]) - np.array(positions[v]))
    return dists

# 최적 경로를 계산하는 함수 (Brute Force)
def find_optimal_path(dists):
    n = len(dists)
    best_path = None
    min_length = float('inf')

    for perm in permutations(range(n)):
        length = sum(dists[perm[i]][perm[i + 1]] for i in range(n - 1))
        length += dists[perm[-1]][perm[0]]  # 돌아오는 길
        if length < min_length:
            min_length = length
            best_path = perm

    return best_path, min_length

# 각 로봇의 품목에 대한 최적 경로 계산
def get_optimal_paths_for_tasks(tasks, positions):
    results = []
    for task in tasks:
        task_results = []
        for robot_items in task:
            if robot_items:
                unique_items = list(set(robot_items))
                dists = create_distance_matrix(unique_items, positions)
                best_path, min_length = find_optimal_path(dists)
                task_results.append((robot_items, [unique_items[i] for i in best_path], min_length))
        results.append(task_results)
    return results

# 경로 애니메이션 함수
def animate_paths(optimal_paths, positions):
    G = nx.Graph()
    pos = positions

    for node in positions.keys():
        G.add_node(node, pos=positions[node])

    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=500, ax=ax)
    lines = [ax.plot([], [], color=color, lw=2)[0] for color in ['red', 'blue']]
    points = [ax.plot([], [], 'o', color=color)[0] for color in ['red', 'blue']]

    def init():
        for line in lines:
            line.set_data([], [])
        for point in points:
            point.set_data([], [])
        return lines + points

    def update(num):
        for line, point, task_results in zip(lines, points, optimal_paths):
            if task_results:
                robot_items, optimal_path, _ = task_results
                if optimal_path:
                    path = []
                    for i in range(len(optimal_path) - 1):
                        path.append((optimal_path[i], optimal_path[i + 1]))
                    path.append((optimal_path[-1], optimal_path[0]))

                    segment_length = 10  # number of frames per segment
                    segment_index = num // segment_length
                    segment_progress = (num % segment_length) / segment_length

                    if segment_index < len(path):
                        u, v = path[segment_index]
                        x0, y0 = positions[u]
                        x1, y1 = positions[v]
                        x = x0 + segment_progress * (x1 - x0)
                        y = y0 + segment_progress * (y1 - y0)
                        point.set_data([x], [y])
                        line.set_data([positions[optimal_path[i]][0] for i in range(segment_index + 1)] + [x],
                                      [positions[optimal_path[i]][1] for i in range(segment_index + 1)] + [y])
        return lines + points

    ani = FuncAnimation(fig, update, init_func=init, frames=len(positions) * 10, interval=100, repeat=False)
    plt.show()

# 메인 함수
def main():
    # 랜덤으로 최대 18개의 원 선택, 같은 원은 최대 3개까지
    selected_items = select_nodes(18, 3)
    print("Selected Items:", selected_items)
    print("Item Counts:", Counter(selected_items))

    # 두 로봇의 동선 계획
    tasks = plan_robot_routes(selected_items)
    for i, (robot1, robot2) in enumerate(tasks):
        print(f"Task {i+1} - Robot 1 Items: {robot1}, Robot 2 Items: {robot2}")

    # 최적 경로 출력
    optimal_paths = get_optimal_paths_for_tasks(tasks, positions)
    for i, task_results in enumerate(optimal_paths):
        for j, (robot_items, optimal_path, min_length) in enumerate(task_results):
            print(f"Task {i+1} - Robot {j+1} Items: {robot_items}")
            print(f"  Optimal Path: {optimal_path}")
            print(f"  Minimum Length: {min_length}")

    # 경로 애니메이션
    animate_paths(optimal_paths[0], positions)  # 첫 번째 작업의 경로를 애니메이션으로 표시

if __name__ == "__main__":
    main()
