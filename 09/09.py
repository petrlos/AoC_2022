#Advent of Code 2022: Day 9
def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def manh_distance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def print_grid(visited):
    for y in range(10, -10, -1):
        for x in range(-15, 15):
            if (x,y) == (0,0):
                print("s", end="")
            elif (x,y) in visited:
                print("T", end="")
            else:
                print(".", end="")
        print("")
    print(" ")

def perform_move(head, tail, direction, move_head=True):
    if move_head:
        new_head = tuple_sum(head, directions[direction])
    else:
        new_head = head
    distance = manh_distance(new_head, tail) #distance between NEW head and OLD tail
    dx, dy = tuple([(x - y) for x, y in zip(new_head,tail)]) #difference in coords of new head and old tail
    if distance in [0,1]: #NEW head lies on OLD tail or lies UDLR - dont move
        new_tail = tail
    elif distance == 2 and (dx == 0 or dy == 0): #old tail laid UDLR - move same direction as head
        new_tail = tuple_sum(tail, directions[direction])
    elif distance == 2 and (abs(dx) == 1 and abs(dx) == 1): #old tail is diagonal from head - dont move
        new_tail = tail
    elif  distance == 3:
        if (dx,dy) in [(-1,2), (1,2),(-1,-2), (1,-2)]: #UP, DOWN
            new_tail = tuple_sum(tail, (dx,dy//2))
        elif (dx,dy) in [(-2,1),(-2,-1),(2,1),(2,-1)]: #LEFT, RIGHT
            new_tail = tuple_sum(tail, (dx//2,dy))
    elif distance == 4:
        if (abs(dx),abs(dy)) == (2,2):
            new_tail = tuple_sum((dx//2, dy//2), tail)
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

def perform_task2(instructions):
    visited = set()
    rope = [(0,0)]*10
    for instruction in instructions:
        direction, counter = instruction.split(" ")
        for _ in range(int(counter)):
            move_head = True
            for i in range(len(rope)-1):
                head, tail = rope[i:i+2]
                new_head, new_tail = perform_move(head, tail, direction, move_head)
                rope[i], rope[i+1] = new_head, new_tail
                move_head = False
            visited.add(rope[-1])
    return visited

#TODO: task2 not working yet
#MAIN
with open("test_2.txt") as file:
    instructions = file.read().splitlines()

directions = {"U":(0, 1),"D":(0, -1), "L":(-1, 0),"R":(1, 0)}  # UDLR

#Task1:
task1_result = perform_task1(instructions)
print("Task 1:", task1_result)

#Task2:
task2_result = perform_task2(instructions)
print_grid(task2_result)
print("Task 2:", len(task2_result))