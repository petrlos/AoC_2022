#Advent of Code 2022: Day 24
from collections import deque

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def create_maze(lines):
    maze = {}
    blizzard_ID = 0
    blizzards_location = {} # blizzard_ID: (x,y)
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
    return maze, x,y, blizzards_location, blizzards_direction

def move_blizzard(max_x, max_y, blizzards_location):
    for blizzard, location in blizzards_location.items():
        new_location = tuple_sum(location, directions[blizzards_direction[blizzard]])
        x, y = new_location
        if maze[new_location] == "#": #blizzard hits a wall
            if blizzards_direction[blizzard] == ">": #roll over to left border: x = 1
                x = 1
            elif blizzards_direction[blizzard] == "<": #roll over right: x = max_x - 1
                x = max_x - 1
            elif blizzards_direction[blizzard] == "v": #roll over up: y = 1
                y = 1
            elif blizzards_direction[blizzard] == "^": #roll over down: y = max_x - 1
                y = max_y - 1
        blizzards_location[blizzard] = (x,y)
    return blizzards_location

def print_maze():
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x,y) in blizzards_location.values():
                blizzard_chars = []
                for blizzard, location in blizzards_location.items():
                    if location == (x,y):
                        blizzard_chars.append(blizzards_direction[blizzard])
                if len(blizzard_chars) == 1:
                    print(blizzard_chars[0], end= "")
                else:
                    print(len(blizzard_chars), end="")
            else:
                print(maze[(x,y)], end = "")
        print(" ")

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()
directions = dict(zip("^v<>",[(0, -1), (0, 1), (-1, 0), (1, 0)]))  # UDLR

maze, max_x, max_y, blizzards_location, blizzards_direction = create_maze(lines)