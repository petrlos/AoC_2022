#Advent of Code 2022: Day 17

def define_rocks():
    rocks = []
    with open("rocks.txt") as file:
        rocks_text = file.read().split("\n\n")
    for rock_text in rocks_text:
        rock = []
        for y, line in enumerate(rock_text.split("\n")):
            for x, char in enumerate(line):
                if char == "#":
                    rock.append((x,y))
        rocks.append(rock)
    return rocks

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def move_rock(rock, direction):
    new_rock = set()
    for coord in rock:
        new_rock.add(tuple_sum(coord, direction))
    return new_rock

def move_possible(rock):
    for coord in rock:
        x,y = coord
        if x > 6 or x < 0 or y < 1: #out of borders on left or right; or under bottom
            return False
        if coord in column: #collision with existing rock
            return False
    return True

def draw_column(column):
    for y in range(20,0,-1):
        if y < 10:
            print(" ", end="")
        print("{0}|".format(y), end="")
        for x in range(7):
            if (x,y) in column:
                print("#", end="")
            else:
                print(".", end="")
        print("|")
    print(" +0123456+   CH:{0}".format(current_height))

#MAIN
rocks = define_rocks()
left_right = {">":(1,0), "<":(-1,0)}
down = (0,-1)

with open("data.txt") as file:
    pattern = file.read()

#Task1
column = set()
current_height = 0
index = 0 #index in list of moves
for rock_counter in range(2022):
    rock = rocks[rock_counter % 5] #choose rock
    move_up = current_height + 3 + 1
    rock = move_rock(rock, (2,move_up)) #set rock to start position
    falling_possible = True
    while falling_possible:
        move = left_right[pattern[index % len(pattern)]] #after the end is reached, start over
        new_rock = move_rock(rock, move)
        if move_possible(new_rock): # is move left/right possible?
            rock = new_rock
        new_rock = move_rock(rock, down)
        if move_possible(new_rock): #is move down possible?
            rock = new_rock
        else: #rock is written to column
            falling_possible = False
            for coord in rock:
                column.add(coord)
            new_height= max([y for x, y in rock])
            if new_height > current_height:
                current_height = new_height
        index += 1
print("Task 1:",current_height)
