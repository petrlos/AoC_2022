#Advent of Code 2022: Day 22
import re
from datetime import datetime
time_start = datetime.now()

def create_maze(maze_input):
    maze = {}
    maze_text = maze_input.splitlines()
    for y, line in enumerate(maze_text, start = 1): #start with one, no off by one errors
        for x, char in enumerate(line, start = 1):
            if char in [".", "#"]:
                maze[(x, y)] = char
    row_coords = [key for key, value in maze.items() if key[1] == 1] #all row coords
    x_s = [coord[0] for coord in row_coords] #all x_s in row
    start = (min(x_s), 1) #to find top left corner of a maze
    return start, maze

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def out_of_borders(location, direction):
    x,y = location
    row_coords = [key for key, value in maze.items() if key[1] == y] #all row coords
    col_coords = [key for key, value in maze.items() if key[0] == x] #all col coords
    x_s = [coord[0] for coord in row_coords] #all x_s in row
    y_s = [coord[1] for coord in col_coords] #all y_s in column
    if direction == 0: #moving right=jump to left: x = min(x), y stays
        x = min(x_s)
    elif direction == 1: #moving down=jump up: x stays, y = min(y)
        y = min(y_s)
    elif direction == 2: #moving left=jump to right: x = max(x), y stays
        x = max(x_s)
    elif direction == 3: #moving up=jump down: x = stays, y=max(y)
        y = max(y_s)
    if maze[(x,y)] == "#":
        return location
    else:
        return (x,y)

def run_through_2D_maze(location, maze, instructions):
    turn = {"L": -1, "R": + 1, "0":0}
    direction = 0 #basic direction right
    for instruction in instructions:
        moves = int(instruction[:-1])
        for move in range(moves):
            new_location = tuple_sum(location, directions[direction])
            if new_location not in maze.keys(): #out of maze
                new_location = out_of_borders(new_location, direction)
            if new_location in maze.keys():
                if maze[new_location] == ".":
                    location = new_location
        direction = (direction + turn[instruction[-1]]) % 4
    x,y = location
    return y * 1000 + x * 4 + direction

#MAIN
with open("data.txt") as file:
    maze_input, instructions = file.read().split("\n\n")
re_inst = re.compile(r"(?:\d+\w?)")
instructions = re_inst.findall(instructions)

start, maze= create_maze(maze_input)


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] #RDLU

#Task 1:
task1 = run_through_2D_maze(start, maze, instructions)
print("Task 1:", task1)
print("Runtime:", datetime.now() - time_start)