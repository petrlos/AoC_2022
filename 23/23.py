#Advent of Code 2022: Day23
from collections import Counter
def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def parse_data(lines):
    elf = 0 #each elf has unique number
    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                grid[elf] = (x,y) #elf with number is to be found on coords (x,y)
                elf += 1
    return grid

def count_grid(grid):
    x_s = [coord[0] for coord in grid.values()] #find all X coords in grid
    y_s = [coord[1] for coord in grid.values()] #find all Y coords in grid
    x_size = abs(min(x_s) - max(x_s)) +1 #size horizontal
    y_size = abs(min(y_s) - max(y_s)) +1 #size vertical
    """print(min(y_s), min(x_s))
    for y in range(min(y_s)-1, max(y_s)+2):
        for x in range(min(x_s)-3, max(x_s)+2):
            if (x,y) in grid.values():
                print("#", end="")
            else:
                print(".", end="")
        print(" ")
    """
    return x_size*y_size-len(grid) #all points in rectangle of size x*y - elven-count

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

#directions
north = [(-1,-1), (0,-1), (1,-1)]
west = [(-1,-1), (-1,0), (-1,1)]
south = [(-1,1), (0,1), (1,1)]
east = [(1,-1), (1,0), (1,1)]

all_neighbours = set(north+west+south+east) #neighbours
look_directions = [north, south, west, east]

counter = 0
start_look = 0
elf_moved = True
while elf_moved:
    elf_moved = False
    new_grid = {}
    for elf, coord in grid.items():
        if space_around_free(coord):
            new_grid[elf] = coord #everything around three? dont move
        else:
            elf_moved = True #found elf that moved? run again
            new_grid[elf] = coord #for case no move is possible
            for i in range(4): #is move in any direction possible? move
                if move_possible(look_directions[(i + start_look) %4], coord):
                    new_grid[elf] = tuple_sum(coord, look_directions[(i + start_look) %4][1])
                    break
    grid = clean_up(new_grid, grid) #find all elves, that moved to same coords and move them back
    start_look += 1
    counter += 1
    if counter == 10:
        print("Size after {0} rounds: {1}".format(counter, count_grid(grid)))
    if counter % 10 == 0:
        print("Rounds checked:",counter)
#runtime for part2 was about 30minutes
print("Round counter, after no elves moved:",counter)