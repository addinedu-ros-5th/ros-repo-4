import numpy as np
# import cv2
# import yaml

class JPS:
    def __init__(self, map_data):
        self.map_data = map_data
        self.height, self.width = map_data.shape

    def is_walkable(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and self.map_data[y, x] == 0

    def get_neighbors(self, x, y):
        neighbors = []
        if self.is_walkable(x - 1, y): neighbors.append((x - 1, y))
        if self.is_walkable(x + 1, y): neighbors.append((x + 1, y))
        if self.is_walkable(x, y - 1): neighbors.append((x, y - 1))
        if self.is_walkable(x, y + 1): neighbors.append((x, y + 1))
        return neighbors

    def jump(self, x, y, px, py):
        if not self.is_walkable(x, y):
            return None

        if (x, y) == self.goal:
            return (x, y)

        dx, dy = x - px, y - py

        if dx != 0 and dy != 0:
            if (self.is_walkable(x - dx, y + dy) and not self.is_walkable(x - dx, y)) or \
               (self.is_walkable(x + dx, y - dy) and not self.is_walkable(x, y - dy)):
                return (x, y)
        elif dx != 0:
            if (self.is_walkable(x + dx, y + 1) and not self.is_walkable(x, y + 1)) or \
               (self.is_walkable(x + dx, y - 1) and not self.is_walkable(x, y - 1)):
                return (x, y)
        elif dy != 0:
            if (self.is_walkable(x + 1, y + dy) and not self.is_walkable(x + 1, y)) or \
               (self.is_walkable(x - 1, y + dy) and not self.is_walkable(x - 1, y)):
                return (x, y)

        if dx != 0 and dy != 0:
            jx = self.jump(x + dx, y, x, y)
            jy = self.jump(x, y + dy, x, y)
            if jx or jy:
                return (x, y)
        if dx != 0:
            return self.jump(x + dx, y, x, y)
        if dy != 0:
            return self.jump(x, y + dy, x, y)

        return None

    def find_path(self, start, goal):
        self.start, self.goal = start, goal
        open_list = []
        open_list.append((start, None))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while open_list:
            open_list.sort(key=lambda x: f_score[x[0]])
            current, parent = open_list.pop(0)
            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(*current):
                jump_point = self.jump(*neighbor, *current)
                if jump_point:
                    tentative_g_score = g_score[current] + self.distance(current, jump_point)
                    if jump_point not in g_score or tentative_g_score < g_score[jump_point]:
                        came_from[jump_point] = current
                        g_score[jump_point] = tentative_g_score
                        f_score[jump_point] = tentative_g_score + self.heuristic(jump_point, goal)
                        open_list.append((jump_point, current))
        return []

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def distance(self, a, b):
        return np.linalg.norm(np.array(a) - np.array(b))

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path
