#Advent of Code 2022: Day 12
import string
from collections import deque
from datetime import datetime
time_start = datetime.now()

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def parse_data(lines):
    values = dict(zip(string.ascii_lowercase, range(1,27)))
    grid = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                start = (x,y)
                grid[(x,y)] = values["a"]
            elif char == "E":
                exit = (x,y)
                grid[(x,y)] = values["z"]
            else:
                grid[(x,y)] = values[char]
    return start, exit, grid

def start_to_exit(start, exit, maze):
    distances = dict()
    distances[start] = 0
    queue = deque([start])
    while queue:
        current_point = queue[0]
        for direction in directions:
            new_point = tuple_sum(current_point, direction)
            if new_point in maze:
                if new_point not in distances.keys():  # not yet visited
                    if (maze[new_point] - 1) <= maze[current_point]:
                        distances[new_point] = distances[current_point] + 1
                        queue.append(new_point)
        queue.popleft()
    if exit not in distances.keys(): # there might be "a" that will not reach exit
        distances[exit] = 99999
    return distances[exit]

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # UDLR
start, exit, maze = parse_data(lines)

#Task1:
task1 = start_to_exit(start, exit, maze)
print("Task 1:", task1)

#Task2:
starts = []
for key, value in maze.items():
    if value == 1:
        starts.append(key)
task2_distances = []
for start in starts:
    new_distance = start_to_exit(start, exit, maze)
    task2_distances.append(new_distance)
print("Task 2", min(task2_distances))