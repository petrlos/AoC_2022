#Advent of Code 2022: Day23
from collections import Counter
def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def parse_data(lines):
    elf = 35
    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                grid[elf] = (x,y)
                elf += 1
    return grid

def print_grid(grid):
    x_s = [coord[0] for coord in grid.values()]
    y_s = [coord[1] for coord in grid.values()]
    """print(min(y_s), min(x_s))
    for y in range(min(y_s)-1, max(y_s)+2):
        for x in range(min(x_s)-3, max(x_s)+2):
            if (x,y) in grid.values():
                print("#", end="")
            else:
                print(".", end="")
        print(" ")
    """
    x_size = abs(min(x_s) - max(x_s)) +1
    y_size = abs(min(y_s) - max(y_s)) +1
    print("Size:", x_size*y_size-len(grid))
    print("Elf count:", len(grid))

def move_possible(directions, coord):
    for direction in directions:
        if tuple_sum(direction, coord) in grid.values():
            return False
    return True

def clean_up(new_grid, grid):
    duplicate_coords= [item for item, count in Counter(new_grid.values()).items() if count >= 2]
    for elf, coord in new_grid.items():
        if coord in duplicate_coords:
            new_grid[elf] = grid[elf]
    return new_grid

def space_around_free(coord):
    for delta in all_neighbours:
        neighbour = tuple_sum(delta, coord)
        if neighbour in grid.values():
            return False
    return True

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()
grid = parse_data(lines)

north = [(-1,-1), (0,-1), (1,-1)]
west = [(-1,-1), (-1,0), (-1,1)]
south = [(-1,1), (0,1), (1,1)]
east = [(1,-1), (1,0), (1,1)]

all_neighbours = set(north+west+south+east)
look_directions = [north, south, west, east]

start_look = 0
for counter in range(10):
    print(counter)
    new_grid = {}
    for elf, coord in grid.items():
        if space_around_free(coord):
            new_grid[elf] = coord
        else:
            new_grid[elf] = coord
            for i in range(4):
                if move_possible(look_directions[(i + start_look) %4], coord):
                    new_grid[elf] = tuple_sum(coord, look_directions[(i + start_look) %4][1])
                    break
    grid = clean_up(new_grid, grid)
    start_look += 1
print_grid(grid)
