#Advent of Code 2022: Day 18
from datetime import datetime
start = datetime.now()
def create_cubes(lines):
    cubes = set()
    for line in lines:
        cube = tuple(map(int,line.split(",")))
        cubes.add(cube)
    return cubes

def create_directions():
    directions = []
    all_directions = set([(x, y, z) for x in range(-1,2) for y in range(-1, 2) for z in range(-1,2)])
    for direction in all_directions:
        if manhDistance(direction, (0,0,0)) == 1:
            directions.append(direction)
    return directions

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def manhDistance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def check_neighbour(cube):
    open_sides = 6
    for direction in directions:
            neighbour = tuple_sum(direction, cube)
            if neighbour in cubes:
                open_sides -= 1
    return open_sides

def check_sides(cubes):
    counter = 0
    for cube in cubes:
        open_sides = check_neighbour(cube)
        counter += open_sides
    return counter

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()
cubes = create_cubes(lines)
directions = create_directions()

#Task1:
task1 = check_sides(cubes)
print("Task 1:", task1)
print("Runtime:", datetime.now()-start)

# Task2: nalit vodu - zacit v souradnici 1,1,1 a postupne rozsirovat vsude, kde neni zed
#v druhem kroku projit vsechny kosticky vody a zkouset jestli jestli ma souseda zed v aspon 1 z 6 smeru
#pokud ano, je to vnejsi kosticka - vytvorit list vnejsich kosticek a spocitat jejich povrch