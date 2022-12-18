#Advent of Code 2022: Day 18
from datetime import datetime
start = datetime.now()
def create_cubes(lines):
    cubes = set()
    for line in lines:
        cube = tuple(map(int,line.split(",")))
        cubes.add(cube)
    return cubes

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def manhDistance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def check_sides(cubes):
    counter = 0
    for cube in cubes:
        open_sides = 6
        for deltaX in (-1,0,1):
            for deltaY in (-1,0,1):
                for deltaZ in (-1,0,1):
                    delta_neighbour = (deltaX, deltaY, deltaZ)
                    neighbour = tuple_sum(delta_neighbour, cube)
                    distance = manhDistance(neighbour, cube)
                    if neighbour in cubes and distance == 1:
                        open_sides -= 1
        counter += open_sides
    return counter

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()
cubes = create_cubes(lines)

#Task1:
task1 = check_sides(cubes)
print("Task 1:", task1)
print("Runtime:", datetime.now()-start)
