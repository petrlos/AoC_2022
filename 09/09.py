#Advent of Code 2022: Day 9
def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def manh_distance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def print_grid(visited):
    for y in range(5, -2, -1):
        for x in range(-2, 9):
            if (x,y) == (0,0):
                print("s", end="")
            elif (x,y) in visited:
                print("T", end="")
            else:
                print(".", end="")
        print("")

def head_tail_diagonal(a,b):
    dx, dy = tuple([x + y for x, y in zip(a,b)])
    if abs(dx) == 1 and abs(dy) == 1:
        return True
    else:
        return False

def perform_move(head, tail, direction):
    dirs = dict(zip("ULDR","DRUL"))
    new_head = tuple_sum(head, directions[direction])
    new_tail = tail
    if manh_distance(new_head, tail) == 2:
        if head_tail_diagonal(new_head, tail):
            new_tail = tail
        else:
            new_tail = tuple_sum(tail, directions[direction])
    elif manh_distance(new_head, tail) == 3:
        new_tail = tuple_sum(new_head, directions[dirs[direction]])
    return new_head, new_tail

#MAIN
with open("test.txt") as file:
    instructions = file.read().splitlines()

print(instructions)
directions = {"U":(0, 1),"D":(0, -1), "L":(-1, 0),"R":(1, 0)}  # UDLR

visited = set()
tail = (0,0)
head = (0,0)

print(perform_move((-1,0),(0,0),"R"))

#Task1:
for instruction in instructions:
    direction, counter = instruction.split(" ")
    for _ in range(int(counter)):
        head,tail = perform_move(head,tail,direction)
        visited.add(tail)
print_grid(visited)
print(len(visited))