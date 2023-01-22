#Advent of Code 2022: Day 24
from copy import deepcopy
from collections import defaultdict
from datetime import datetime
time_start = datetime.now()

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def create_maze(lines):
    maze = defaultdict(lambda: -1)
    blizzard_ID = 0
    blizzards_location = {}  #blizzard_ID: (x,y)
    blizzards_direction = {} #blizzard_ID: direction ( < ^ > v )
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in [".", "#"]:
                maze[(x,y)] = char
            else:
                blizzards_direction[blizzard_ID] = char
                blizzards_location[blizzard_ID] = (x,y)
                blizzard_ID += 1
                maze[(x,y)] = "." #everywhere is a dot, because everywhere might be no blizzard
    return maze, x,y, blizzards_location, blizzards_direction, (x-1,y)

def move_blizzard(max_x, max_y, blizzards_locations):
    for blizzard, location in blizzards_locations.items():
        new_location = tuple_sum(location, directions[blizzards_directions[blizzard]])
        x, y = new_location
        if maze[new_location] == "#": #blizzard hits a wall
            if blizzards_directions[blizzard] == ">": #roll over to left border: x = 1
                x = 1
            elif blizzards_directions[blizzard] == "<": #roll over right: x = max_x - 1
                x = max_x - 1
            elif blizzards_directions[blizzard] == "v": #roll over up: y = 1
                y = 1
            elif blizzards_directions[blizzard] == "^": #roll over down: y = max_x - 1
                y = max_y - 1
        blizzards_locations[blizzard] = (x,y)
    return blizzards_locations

def print_maze():
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x,y) in blizzards_locations.values():
                blizzard_chars = []
                for blizzard, location in blizzards_locations.items():
                    if location == (x,y):
                        blizzard_chars.append(blizzards_directions[blizzard])
                if len(blizzard_chars) == 1:
                    print(blizzard_chars[0], end= "")
                else:
                    print(len(blizzard_chars), end="")
            else:
                print(maze[(x,y)], end = "")
        print(" ")

def run_through_maze(maze, start, end_of_maze, blizzards_locations):
    locations = set(list([start]))
    counter = 0
    while end_of_maze not in locations:
        for location in deepcopy(locations):
            for direction in move_directions: #move in all possible directions incl. stay on place
                new_location = tuple_sum(location, direction)
                if maze[new_location] != -1 and maze[new_location] != "#":  # coord not in maze or wall
                    locations.add(new_location)
        blizzards_locations = move_blizzard(max_x, max_y, blizzards_locations)
        locations = locations - set(blizzards_locations.values()) #kill all, that stay on blizzard
        counter += 1
    return counter, blizzards_locations

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()
directions = dict(zip("^v<>",[(0, -1), (0, 1), (-1, 0), (1, 0)]))  # UDLR
move_directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (0,0)] #UDLR + dont move

start = (1,0)
results = []
maze, max_x, max_y, blizzards_locations, blizzards_directions, end_of_maze = create_maze(lines)

#Task1: from start to end
result, blizzards_locations = run_through_maze(maze, start, end_of_maze, blizzards_locations)
results.append(result)

#Task2 from end to start and then back
result, blizzards_locations = run_through_maze(maze, end_of_maze, start, blizzards_locations)
results.append(result)
result, blizzards_locations = run_through_maze(maze, start, end_of_maze, blizzards_locations)
results.append(result)

print("Task 1:", results[0])
print("Task 2:", sum(results))
print("Runtime:", datetime.now() - time_start) #for my input +- 5 seconds