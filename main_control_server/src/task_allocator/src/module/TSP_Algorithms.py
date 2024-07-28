import random
from collections import Counter
import numpy as np
from itertools import combinations
import time

# 6개의 원을 3행 2열로 배치
positions = {
    'RD': (0, 0),
    'RA': (0, 1),
    'RE': (1, 0),
    'RB': (1, 1),
    'RC': (2, 0),
    'RF': (2, 1)
}

# 원 선택 함수
def select_nodes(min_n, max_n, max_copies):
    selected_nodes = []
    num_nodes = random.randint(min_n, max_n)
    while len(selected_nodes) < num_nodes:
        node = random.choice(list(positions.keys()))
        if selected_nodes.count(node) < max_copies:
            selected_nodes.append(node)
    return selected_nodes

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
def calculate_path_length(path, dists):
    length = 0
    for i in range(len(path) - 1):
        length += dists[path[i]][path[i + 1]]
    length += dists[path[-1]][path[0]]  # 마지막 위치에서 시작 위치로 돌아오는 거리 추가
    return length

# 최근접 이웃 알고리즘 함수
def nearest_neighbor_algorithm(nodes, dists, start_index=0):
    path = [start_index]
    visited = {start_index}
    while len(path) < len(nodes):
        last = path[-1]
        next_node = min((dists[last][i], i) for i in range(len(nodes)) if i not in visited)[1]
        path.append(next_node)
        visited.add(next_node)
    return path, calculate_path_length(path, dists)

# 두 로봇의 경로 최적화 함수
def optimize_two_robots_prioritize(selected_nodes, positions):
    n = len(selected_nodes)
    best_total_length = float('inf')
    best_paths = None

    # 노드 인덱스 리스트 생성
    indices = list(range(n))
    start_nodes = {'RD', 'RE', 'RF'}

    # 가능한 모든 조합을 나누어 두 그룹으로 나누기
    for comb in combinations(indices, n // 2):
        set1 = list(comb)
        set2 = [i for i in indices if i not in set1]

        # 거리 행렬 생성
        nodes1 = [selected_nodes[i] for i in set1]
        nodes2 = [selected_nodes[i] for i in set2]
        dists1, unique_nodes1 = create_distance_matrix(nodes1, positions)
        dists2, unique_nodes2 = create_distance_matrix(nodes2, positions)

        # 시작 인덱스 설정
        start_index1 = next((i for i, node in enumerate(unique_nodes1) if node in start_nodes), 0)
        start_index2 = next((i for i, node in enumerate(unique_nodes2) if node in start_nodes), 0)

        # 최적 경로 계산 (근사 알고리즘 사용)
        path1, length1 = nearest_neighbor_algorithm(unique_nodes1, dists1, start_index1)
        path2, length2 = nearest_neighbor_algorithm(unique_nodes2, dists2, start_index2)

        total_length = length1 + length2

        if total_length < best_total_length:
            best_total_length = total_length
            best_paths = (unique_nodes1, path1, length1), (unique_nodes2, path2, length2)

    # 같은 노드를 한 번에 방문하도록 수정
    def expand_path(path, nodes):
        expanded_path = []
        for i in path:
            node = nodes[i]
            expanded_path.extend([node] * selected_nodes.count(node))
        return expanded_path

    expanded_best_paths = [(expand_path(best_paths[0][1], best_paths[0][0]), best_paths[0][2]),
                           (expand_path(best_paths[1][1], best_paths[1][0]), best_paths[1][2])]

    return expanded_best_paths, best_total_length

# 메인 함수
def main_prioritize():
    # 랜덤으로 최소 6개에서 최대 18개의 원 선택, 같은 원은 최대 3개까지
    selected_items = select_nodes(6, 18, 3)
    print("Selected Items:", selected_items)
    print("Item Counts:", Counter(selected_items))

    # 두 로봇의 동선 최적화
    start_time = time.time()
    optimal_paths, best_total_length = optimize_two_robots_prioritize(selected_items, positions)
    end_time = time.time()

    print(f"Best Total Length: {best_total_length}")
    for i, (path, length) in enumerate(optimal_paths):
        print(f"Robot {i+1} Path: {path}")
        print(f"Path Length: {length}")

    print(f"Calculation Time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main_prioritize()
