#Advent of Code 2022: Day 9 - part2
def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def manh_distance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def perform_move(head, tail):
    distance = manh_distance(head, tail) #distance between two elements of a snake
    dx, dy = tuple([(x - y) for x, y in zip(head,tail)]) #difference in coords of these elements
    if distance == 2 and (dx == 0 or dy == 0):
        tail = tuple_sum(tail, (dx//2, dy//2)) #lies on axe X or Y - move along that axe
    elif  distance == 3:
        if (dx,dy) in [(-1,2), (1,2),(-1,-2), (1,-2)]:
            tail = tuple_sum(tail, (dx,dy//2))
        elif (dx,dy) in [(-2,1),(-2,-1),(2,1),(2,-1)]:
            tail = tuple_sum(tail, (dx//2,dy))
    elif distance == 4:
        tail = tuple_sum(tail, (dx//2, dy // 2))
    return tail

def move_snake_with_length(instructions, snake_length):
    visited = set()
    snake = [(0, 0)] * snake_length
    for instruction in instructions:
        direction, counter = instruction.split(" ")
        for _ in range(int(counter)):
            snake[0] = tuple_sum(snake[0], directions[direction]) #move head
            for i in range(len(snake)-1):
                snake[i+1] = perform_move(snake[i], snake[i+1]) #correct all pairs
            visited.add(snake[-1])
    return len(visited)

#MAIN
with open("data.txt") as file:
    instructions = file.read().splitlines()

directions = {"U":(0, 1),"D":(0, -1), "L":(-1, 0),"R":(1, 0)}  # UDLR

#Task1
print("Task 1:",move_snake_with_length(instructions, 2))

#Task2
print("Task 2:",move_snake_with_length(instructions, 10))