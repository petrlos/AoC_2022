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
    print(" ")

def perform_move(head, tail, direction):
    transfer = dict(zip("ULDR", "DRUL"))
    new_head = tuple_sum(head, directions[direction])
    distance = manh_distance(new_head, tail) #distance between NEW head and OLD tail
    dx, dy = tuple([abs(x - y) for x, y in zip(new_head,tail)]) #difference in coords of new head and old tail
    if distance in [0,1]: #NEW head lies on OLD tail or lies UDLR - dont move
        new_tail = tail
    elif distance == 2 and (dx == 0 or dy == 0): #old tail laid UDLR - move same direction as head
        new_tail = tuple_sum(tail, directions[direction])
    elif distance == 2 and (dx == 1 and dx == 1): #old tail is diagonal from head - dont move
        new_tail = tail
    elif distance == 3: #NEW tail becomes position of NEW head in opposite direction
        new_tail = tuple_sum(new_head, directions[transfer[direction]])
    return new_head, new_tail

def perform_task1(instructions):
    visited = set()
    tail = (0, 0)
    head = (0, 0)
    for instruction in instructions:
        direction, counter = instruction.split(" ")
        for _ in range(int(counter)):
            head, tail = perform_move(head, tail, direction)
            visited.add(tail)
    return len(visited)

#MAIN
with open("test.txt") as file:
    instructions = file.read().splitlines()

directions = {"U":(0, 1),"D":(0, -1), "L":(-1, 0),"R":(1, 0)}  # UDLR

#Task1:
task1_result = perform_task1(instructions)
print("Task 1:", task1_result)