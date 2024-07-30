import math
import numpy as np

import os
import yaml
from ament_index_python.packages import get_package_share_directory

class AStarPlanner:

    def __init__(self, resolution, rr, padding):
        """
        Initialize grid map for a star planning

        ox: x position list of Obstacles [m]
        oy: y position list of Obstacles [m]
        resolution: grid resolution [m]
        rr: robot radius[m]
        """

        self.resolution = resolution
        self.rr = rr
        self.padding = padding
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 0, 0
        self.obstacle_map = None
        self.x_width, self.y_width = 0, 0
        self.motion = self.get_motion_model()

        # custom parameters
        self.resolution = 1
        self.map_resolution = 1
        self.map_origin = (-0.461, -1.85)
        
        ox, oy = self.load_map()

        self.calc_obstacle_map(ox, oy)

        print("Map loading done!")

    def load_map(self):
        print("Loading map start!")
        map_yaml_file = os.path.join(get_package_share_directory('lrobot'), 'maps', 'mfl.yaml')
        map_yaml_data = yaml.full_load(open(map_yaml_file))

        self.map_resolution = map_yaml_data['resolution']    # m / pixel
        self.map_origin = map_yaml_data['origin']    # list
        

        map_pgm_file = os.path.join(get_package_share_directory('lrobot'), 'maps', map_yaml_data['image'])

        with open(map_pgm_file, 'rb') as pgmf:
            pgm_data = pgmf.readlines()
            map_width, map_height = map(int, pgm_data[1].split())
            map_data = np.array(list(map(int, pgm_data[3])))
            map_data[map_data <= 210] = 0
            map_data[map_data > 210] = 100
            map_data = map_data.reshape((map_height, map_width))
            # map_data = np.rot90(map_data, 3)
            map_data = np.flip(map_data, axis=0)    # 이상하게 불러온 맵이 플립되어있음

        # set obstacle positions
        ox, oy = [], []
        padded_map_data = map_data.copy()
        for i in range(map_height):
            for j in range(map_width):
                if map_data[i][j] == 0:
                    ox.append(j)
                    oy.append(i)
                    for dx in range(-self.padding, self.padding + 1):
                        for dy in range(-self.padding, self.padding + 1):
                            if 0 <= j + dx < map_width and 0 <= i + dy < map_height and padded_map_data[i + dy][j + dx] != 0:
                                padded_map_data[i + dy][j + dx] = 0
                                ox.append(j + dx)
                                oy.append(i + dy)

        return ox, oy

    class Node:
        def __init__(self, x, y, cost, parent_index, vector = None):
            self.x = x  # index of grid
            self.y = y  # index of grid
            self.cost = cost
            self.parent_index = parent_index
            self.vector = vector

        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(
                self.cost) + "," + str(self.parent_index)

    def planning(self, sx_real, sy_real, gx_real, gy_real):
        """
        A star path search

        input:
            s_x: start x position [m]
            s_y: start y position [m]
            gx: goal x position [m]
            gy: goal y position [m]

        output:
            rx: x position list of the final path
            ry: y position list of the final path
        """

        sx = (sx_real - self.map_origin[0]) / self.map_resolution
        sy = (sy_real - self.map_origin[1]) / self.map_resolution
        gx = (gx_real - self.map_origin[0]) / self.map_resolution
        gy = (gy_real - self.map_origin[1]) / self.map_resolution
        
        print(sx_real, sy_real, gx_real, gy_real)
        print(sx, sy, gx, gy)

        
        start_node = self.Node(self.calc_xy_index(sx, self.min_x),
                               self.calc_xy_index(sy, self.min_y), 0.0, -1)
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x),
                              self.calc_xy_index(gy, self.min_y), 0.0, -1)

        open_set, closed_set = dict(), dict()
        open_set[self.calc_grid_index(start_node)] = start_node

        is_starting = True     # navigation으로 스타팅 포인트가 padding 벗어났을 때 verifying 안하고 넘어가는 용도
        
        while True:
            if len(open_set) == 0:
                print("Open set is empty..")
                break

            c_id = min(
                open_set,
                # key=lambda o: open_set[o].cost + self.calc_heuristic(goal_node, open_set[o]))
                key=lambda o: open_set[o].cost + self.calc_manhattan(goal_node, open_set[o]))
            current = open_set[c_id]

            if current.x == goal_node.x and current.y == goal_node.y:
                print("Find goal")
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                goal_node.vector = current.vector
                break

            # Remove the item from the open set
            del open_set[c_id]

            # Add it to the closed set
            closed_set[c_id] = current

            # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion):

                is_turned = 0
                before_vector = (0, 0)
                now_vector = (self.motion[i][0], self.motion[i][1])
                if closed_set.get(current.parent_index):
                    before_node = closed_set[current.parent_index]
                    before_vector = (current.x - before_node.x, current.y - before_node.y)
                    is_turned = before_vector != now_vector
                node = self.Node(current.x + self.motion[i][0],
                                 current.y + self.motion[i][1],
                                 current.cost + self.motion[i][2] * (1 + is_turned), c_id, now_vector)
                
                n_id = self.calc_grid_index(node)

                # If the node is not safe, do nothing
                if (not is_starting) and (not self.verify_node(node)):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node  # discovered a new node
                else:
                    if open_set[n_id].cost > node.cost:
                        # This path is the best until now. record it
                        open_set[n_id] = node

                is_starting = False


        rx, ry, tpx, tpy, tvec_x, tvec_y = self.calc_final_path(goal_node, closed_set)


        # grid position to map position
        for i in range(len(tpx)):
            tpx[i] = (tpx[i] * self.map_resolution) + self.map_origin[0]
            tpy[i] = (tpy[i] * self.map_resolution) + self.map_origin[1]

        print(tpx, tpy, tvec_x, tvec_y)

        return rx, ry, tpx, tpy, tvec_x, tvec_y

    def calc_final_path(self, goal_node, closed_set):
        # generate final course
        rx, ry = [self.calc_grid_position(goal_node.x, self.min_x)], [
            self.calc_grid_position(goal_node.y, self.min_y)]
        tpx, tpy = [], []
        tvec_x, tvec_y = [], []
        
        parent_index = goal_node.parent_index
        now_node = goal_node
        before_vector = (0, 0)
        now_vector = (0, 0)
        while parent_index != -1:
            n = closed_set[parent_index]
            rx.append(self.calc_grid_position(n.x, self.min_x))
            ry.append(self.calc_grid_position(n.y, self.min_y))

            is_turned = 0
            now_vector = (n.x - now_node.x, n.y - now_node.y)
            is_turned = now_vector != before_vector
        
            if is_turned:
                tpx.append(now_node.x)
                tpy.append(now_node.y)
                tvec_x.append(now_node.vector[0])
                tvec_y.append(now_node.vector[1])

            parent_index = n.parent_index
            now_node = n
            before_vector = now_vector
        
        return rx, ry, tpx[::-1], tpy[::-1], tvec_x[::-1], tvec_y[::-1]

    @staticmethod
    def calc_heuristic(n1, n2):
        w = 1.0  # weight of heuristic
        d = w * math.hypot(n1.x - n2.x, n1.y - n2.y)
        return d
    
    @staticmethod
    def calc_manhattan(n1, n2):
        d = abs(n1.x - n2.x) + abs(n1.y - n2.y)
        return d

    def calc_grid_position(self, index, min_position):
        """
        calc grid position

        :param index:
        :param min_position:
        :return:
        """
        pos = index * self.resolution + min_position
        return pos

    # def calc_xy_index(self, position, min_pos):
    #     return round((position - min_pos) / self.resolution)

    def calc_grid_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x)

    def calc_xy_index(self, position, min_pos):
        index = round((position - min_pos) / self.resolution)
        if index < 0:
            index = 0
        return index

    def verify_node(self, node):
        if node.x < 0 or node.y < 0 or node.x >= self.x_width or node.y >= self.y_width:
            return False

        if self.obstacle_map[node.x][node.y]:
            return False

        return True

    # def verify_node(self, node):
    #     px = self.calc_grid_position(node.x, self.min_x)
    #     py = self.calc_grid_position(node.y, self.min_y)

    #     if px < self.min_x:
    #         return False
    #     elif py < self.min_y:
    #         return False
    #     elif px >= self.max_x:
    #         return False
    #     elif py >= self.max_y:
    #         return False


    #     # collision check
    #     if self.obstacle_map[node.x][node.y]:
    #         return False

    #     return True

    def calc_obstacle_map(self, ox, oy):
        print("Calc Obstacle...")

        self.min_x = round(min(ox))
        self.min_y = round(min(oy))
        self.max_x = round(max(ox))
        self.max_y = round(max(oy))
        print("min_x:", self.min_x)
        print("min_y:", self.min_y)
        print("max_x:", self.max_x)
        print("max_y:", self.max_y)

        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)
        print("x_width:", self.x_width)
        print("y_width:", self.y_width)

        # obstacle map generation
        self.obstacle_map = [[False for _ in range(self.y_width)]
                             for _ in range(self.x_width)]
        for ix in range(self.x_width):
            x = self.calc_grid_position(ix, self.min_x)
            for iy in range(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for iox, ioy in zip(ox, oy):
                    d = math.hypot(iox - x, ioy - y)
                    if d <= self.rr:
                        self.obstacle_map[ix][iy] = True
                        break

    @staticmethod
    def get_motion_model():
        # dx, dy, cost
        motion = [
            [1, 0, 1],
            [0, 1, 1],
            [-1, 0, 1],
            [0, -1, 1],
            # [-1, -1, math.sqrt(2)],
            # [-1, 1, math.sqrt(2)],
            # [1, -1, math.sqrt(2)],
            # [1, 1, math.sqrt(2)]
        ]

        return motion


# def main():
#     print(__file__ + " start!!")

#     a_star = AStarPlanner(1, 0.2, 3)
    
#     # start and goal position
#     sx = 0  # [m]
#     sy = 0  # [m]
#     gx = 0.716  # [m]
#     gy = -1.11  # [m]
#     grid_size = 0.3  # [m]
#     robot_radius = 0.2  # [m]
#     padding = 3


#     a_star = AStarPlanner(grid_size, robot_radius, padding)

#     rx, ry, tpx, tpy, tvec_x, tvec_y = a_star.planning(sx, sy, gx, gy)

#     if tpx:
#         print(f"Waypoints: {list(zip(tpx, tpy))}")
#     else:
#         print("No path found")


# if __name__ == '__main__':
#     main()


# import numpy as np
# import heapq
# import yaml
# from PIL import Image
# import os

# class AStar:
#     def __init__(self, map_pgm, map_yaml):
#         self.map_pgm = map_pgm
#         self.map_yaml = map_yaml
#         self.map = None

#     def load_map(self):
#         if not os.path.exists(self.map_pgm) or not os.path.exists(self.map_yaml):
#             print(f"Map files not found: {self.map_pgm}, {self.map_yaml}")
#             return

#         with open(self.map_yaml, 'r') as yaml_file:
#             yaml_data = yaml.safe_load(yaml_file)

#         resolution = yaml_data['resolution']
#         origin = yaml_data['origin']

#         pgm_image = Image.open(self.map_pgm)
#         map_array = np.array(pgm_image)
        
#         map_array[map_array > 0] = 1  # 1 represents free space
#         map_array[map_array == 0] = 0  # 0 represents obstacles

#         self.map = map_array
#         print("Map loaded successfully")

#     def heuristic(self, start, goal):
#         return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

#     def astar(self, start, goal):
#         if self.map is None:
#             print("Map not loaded.")
#             return []

#         start = (int(start[0]), int(start[1]))
#         goal = (int(goal[0]), int(goal[1]))

#         if not self.is_valid(start):
#             print(f"Start position {start} is invalid")
#             return []

#         if not self.is_valid(goal):
#             print(f"Goal position {goal} is invalid")
#             return []
        
#         open_list = []
#         heapq.heappush(open_list, (0, start))
#         came_from = {}
#         g_score = {start: 0}
#         f_score = {start: self.heuristic(start, goal)}

#         while open_list:
#             _, current = heapq.heappop(open_list)

#             if current == goal:
#                 path = self.reconstruct_path(came_from, current)
#                 print(f"Path found: {path}")
#                 return path

#             neighbors = self.get_neighbors(current)
#             for neighbor in neighbors:
#                 tentative_g_score = g_score[current] + 1

#                 if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
#                     came_from[neighbor] = current
#                     g_score[neighbor] = tentative_g_score
#                     f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
#                     if neighbor not in [i[1] for i in open_list]:
#                         heapq.heappush(open_list, (f_score[neighbor], neighbor))

#         print("No path found")
#         return []

#     def is_valid(self, node):
#         return 0 <= node[0] < self.map.shape[0] and 0 <= node[1] < self.map.shape[1] and self.map[node[0], node[1]] == 1

#     def get_neighbors(self, node):
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         neighbors = []
#         for direction in directions:
#             neighbor = (node[0] + direction[0], node[1] + direction[1])
#             if self.is_valid(neighbor):
#                 neighbors.append(neighbor)
#         return neighbors

#     def reconstruct_path(self, came_from, current):
#         path = [current]
#         while current in came_from:
#             current = came_from[current]
#             path.append(current)
#         path.reverse()
#         return path


# import numpy as np
# import heapq
# import yaml
# from PIL import Image

# class AStar:
#     def __init__(self, map_pgm, map_yaml):
#         self.map = self.load_map(map_pgm, map_yaml)

#     def load_map(self, map_pgm, map_yaml):
#         with open(map_yaml, 'r') as yaml_file:
#             yaml_data = yaml.safe_load(yaml_file)

#         resolution = yaml_data['resolution']
#         origin = yaml_data['origin']

#         pgm_image = Image.open(map_pgm)
#         map_array = np.array(pgm_image)
        
#         map_array[map_array > 0] = 1  # 1 represents free space
#         map_array[map_array == 0] = 0  # 0 represents obstacles

#         return map_array

#     def heuristic(self, start, goal):
#         return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

#     def astar(self, start, goal):
#         start = (int(start[0]), int(start[1]))
#         goal = (int(goal[0]), int(goal[1]))
        
#         open_list = []
#         heapq.heappush(open_list, (0, start))
#         came_from = {}
#         g_score = {start: 0}
#         f_score = {start: self.heuristic(start, goal)}

#         while open_list:
#             _, current = heapq.heappop(open_list)

#             if current == goal:
#                 return self.reconstruct_path(came_from, current)

#             neighbors = self.get_neighbors(current)
#             for neighbor in neighbors:
#                 tentative_g_score = g_score[current] + 1

#                 if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
#                     came_from[neighbor] = current
#                     g_score[neighbor] = tentative_g_score
#                     f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
#                     if neighbor not in [i[1] for i in open_list]:
#                         heapq.heappush(open_list, (f_score[neighbor], neighbor))

#         return []

#     def get_neighbors(self, node):
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         neighbors = []
#         for direction in directions:
#             neighbor = (node[0] + direction[0], node[1] + direction[1])
#             if 0 <= neighbor[0] < self.map.shape[0] and 0 <= neighbor[1] < self.map.shape[1]:
#                 if self.map[neighbor[0], neighbor[1]] == 1:
#                     neighbors.append(neighbor)
#         return neighbors

#     def reconstruct_path(self, came_from, current):
#         path = [current]
#         while current in came_from:
#             current = came_from[current]
#             path.append(current)
#         path.reverse()
#         return path

# # def main(args=None):
# #     import sys
# #     if len(sys.argv) < 3:
# #         print("Usage: astar.py <map.pgm> <map.yaml>")
# #         return

# #     map_pgm = sys.argv[1]
# #     map_yaml = sys.argv[2]

# #     astar = AStar(map_pgm, map_yaml)
# #     print("AStar initialized with map:", map_pgm, "and", map_yaml)

# # if __name__ == "__main__":
# #     main()