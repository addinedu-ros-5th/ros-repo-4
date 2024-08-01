import random
from collections import Counter
import numpy as np
from itertools import permutations
import time

# 6개의 원을 3행 2열로 배치
positions = {
    'RA': (0, 1),
    'RB': (0, 2),
    'RC': (0, 3),
    'RD': (1, 1),
    'RE': (1, 2),
    'RF': (1, 3)
}

# 앞줄 렉 (로봇과 가까운 쪽)
front_racks = {'RD', 'RE', 'RF'}

# 원 선택 함수
def select_nodes():
    racks = ['RA', 'RB', 'RC', 'RD', 'RE', 'RF']
    num_items = random.randint(6, 18)
    items = []
    while len(items) < num_items:
        rack = random.choice(racks)
        if items.count(rack) < 3:
            items.append(rack)
    return items

# 거리 행렬 생성 함수
def create_distance_matrix(nodes, positions):
    unique_nodes = list(set(nodes))
    n = len(unique_nodes)
    dists = np.zeros((n, n))
    for i, u in enumerate(unique_nodes):
        for j, v in enumerate(unique_nodes):
            if i != j:
                dists[i][j] = np.linalg.norm(np.array(positions[u]) - np.array(positions[v]))
    return dists, unique_nodes

# 경로 길이 계산 함수
def calculate_path_length(path, dists, node_indices):
    length = 0
    for i in range(len(path) - 1):
        length += dists[node_indices[path[i]]][node_indices[path[i + 1]]]
    length += dists[node_indices[path[-1]]][node_indices[path[0]]]  # 마지막 위치에서 시작 위치로 돌아오는 거리 추가
    return length

# 최근접 이웃 알고리즘 함수
def nearest_neighbor_algorithm(nodes, dists, start_index=0):
    n = len(nodes)
    node_indices = {node: i for i, node in enumerate(nodes)}
    path = [nodes[start_index]]
    visited = {nodes[start_index]}
    while len(path) < n:
        last = path[-1]
        next_node = min((dists[node_indices[last]][node_indices[node]], node) for node in nodes if node not in visited)[1]
        path.append(next_node)
        visited.add(next_node)
    return path, calculate_path_length(path, dists, node_indices)

# 같은 렉을 한 번에 방문하도록 최적화 함수
def optimize_robot_path(selected_nodes, positions):
    unique_nodes = list(set(selected_nodes))
    dists, unique_nodes = create_distance_matrix(unique_nodes, positions)

    # 시작 인덱스 설정
    start_index = next((i for i, node in enumerate(unique_nodes) if node in front_racks), 0)

    # 최적 경로 계산 (근사 알고리즘 사용)
    path, length = nearest_neighbor_algorithm(unique_nodes, dists, start_index)

    return path, length

# 메인 함수
def main():
    # 랜덤으로 6개에서 18개의 원 선택, 같은 원은 최대 3개까지
    selected_items = select_nodes()
    print("Selected Items:", selected_items)
    print("Item Counts:", Counter(selected_items))

    # 물건을 로봇이 싣을 수 있는 단위로 분리
    item_counts = Counter(selected_items)
    batches = []
    for rack, count in item_counts.items():
        for _ in range(count // 3):
            batches.append([rack] * 3)
        if count % 3:
            batches.append([rack] * (count % 3))

    total_path = []
    total_length = 0

    # 각 배치에 대해 최적 경로 계산
    for batch in batches:
        path, length = optimize_robot_path(batch, positions)
        total_path.extend(path)
        total_length += length

    print(f"Total Path: {total_path}")
    print(f"Total Path Length: {total_length}")

if __name__ == "__main__":
    main()
