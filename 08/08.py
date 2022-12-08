#Advengt of Code 2022: Day 8

def scan_forest(lines):
    forest = dict()
    for y, line in enumerate(lines):
        for x, height in enumerate(line):
            forest[(x,y)] = int(height)
    return forest, x+1, y+1

def check_single_tree(forest, tree, maxX, maxY):
    #find all trees in each direction and a tallest one - trees on edge have heigt -1,
    #because 0 would not be visible
    tree_x, tree_y = tree
    left = [forest[(x,tree_y)] for x in range(0,tree_x)]
    left = -1 if len(left) == 0 else max(left)
    right = [forest[(x,tree_y)] for x in range(tree_x+1,maxX)]
    right = -1 if len(right) == 0 else max(right)
    up = [forest[(tree_x, y)] for y in range(0, tree_y)]
    up = -1 if len(up) == 0 else max(up)
    down = [forest[(tree_x, y)] for y in range(tree_y+1, maxY)]
    down = -1 if len(down) == 0 else max(down)
    if forest[tree] > left or forest[tree] > right or forest[tree] > up or forest[tree] > down:
        return True
    return False

def find_visible_trees(forest, maxX, maxY):
    visible_trees = set()
    for y in range(0, maxY):
        for x in range(0, maxX):
            if check_single_tree(forest, (x,y), maxX, maxY):
                visible_trees.add((x,y))
    return visible_trees

def draw_forest(visible_trees): #visible trees only
    for y in range(maxY):
        for x in range(maxY):
            if (x, y) in visible_trees:
                print(forest[(x, y)], end="")
            else:
                print(" ", end="")
        print(" ")

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

#Task1
forest, maxX, maxY = scan_forest(lines)
visible_trees = find_visible_trees(forest, maxX, maxY)
print("Task 1:", len(visible_trees))
