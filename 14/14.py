#Advent of Code 2022: Day 14:
from datetime import datetime
time_start = datetime.now()
def create_cave(lines):
    lowestY = []
    cave = dict()
    for line in lines:
        corners = line.split(" -> ")
        for i in range(len(corners)-1):
            begin, end = corners[i:i+2]
            beginX, beginY = list(map(int, begin.split(",")))
            endX, endY = list(map(int, end.split(",")))
            lowestY.append(endY)
            lowestY.append(beginY)
            dx = beginX - endX
            dy = beginY - endY
            if dx == 0: #vertical
                if endY < beginY:
                    endY, beginY = beginY, endY
                for y in range(beginY, endY+1, 1):
                    cave[(beginX, y)] = "#"
            if dy == 0: #horizontal
                if endX < beginX:
                    endX, beginX = beginX, endX
                for x in range(beginX, endX+1, 1):
                    cave[(x, beginY)] = "#"
    return max(lowestY), cave

def print_cave(cave): # for test purpose only, real cave is too big to be printed in console
    for y in range(0,12):
        print(y, end="")
        for x in range(490, 510):
            if (x,y) in cave.keys():
                print(cave[(x,y)], end="")
            else:
                print(".", end="")
        print("")

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def fill_up_the_cave(cave, bottom):
    dir_down = (0, 1)
    dir_left_down = (-1, 1)
    dir_right_down = (1, 1)

    falling_possible = True
    start = (500, 0)
    # Task1
    while falling_possible:
        active_drop = start
        active_drop_active = True
        while active_drop_active:
            down = tuple_sum(active_drop, dir_down)
            left_down = tuple_sum(active_drop, dir_left_down)
            right_down = tuple_sum(active_drop, dir_right_down)
            if down not in cave.keys(): #move down possible
                active_drop = down
            elif left_down not in cave.keys(): #move down/left possible
                active_drop = left_down
            elif right_down not in cave.keys(): #move down/right possible
                active_drop = right_down
            else: #no move possible
                active_drop_active = False
                cave[active_drop] = "o" #save drop to cave
                if active_drop == (start): #active drop is saved to start position -> no more drops possible
                    active_drop_active = False
                    falling_possible = False
            if active_drop[1] > bottom: #y coord is under bottom
                active_drop_active = False
                falling_possible = False
    return list(cave.values()).count("o")

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

bottom, cave = create_cave(lines)

#Task1
task1 = fill_up_the_cave(cave, bottom)
print("Task 1:",task1)
print("Runtime:",datetime.now() - time_start)
print(" ")

#Task2:
bottom, cave= create_cave(lines)
for x in range(0,1000): #range tried out,
    cave[(x,bottom + 2)] = "#"
task2 = fill_up_the_cave(cave, bottom+2)
print("Task 2:", task2)
print("Runtime:",datetime.now() - time_start)