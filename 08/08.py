#Advengt of Code 2022: Day 8
from datetime import datetime
start = datetime.now()
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
    visible_trees = set() #if a tree is visible, add its coordinance to a set
    for y in range(0, maxY):
        for x in range(0, maxX):
            if check_single_tree(forest, (x,y), maxX, maxY):
                visible_trees.add((x,y))
    return visible_trees

def draw_forest(visible_trees, task2=False):
    for y in range(maxY):
        for x in range(maxY):
            if (x, y) in visible_trees:
                if not task2:
                    print(forest[(x, y)], end="")
                else:
                    print(scenic_score[(x,y)], end="") #added possibility to print scenic_score instead of height
            else:
                print(" ", end="")
        print(" ")

def find_distance(ref_tree_height, trees):
    length = 0 #if tree lies on edge, for cycle is skipped and langth would not be defined
    for length in range(len(trees)):
        if trees[:length+1][-1] >= ref_tree_height:
            return length+1 #if a tree with heigth same or higher is found, return distance
    if length+1 == len(trees):
        return length +1 #all trees seen up to the edge
    else:
        return 0 #edge trees have distance 0

def count_scenic_score(forest, maxX, maxY, tree):
    #this function might be put together with "check_single_tree" - the intervals are being count twice
    tree_x, tree_y = tree
    left = [forest[(x,tree_y)] for x in range(0,tree_x)]
    left_distance = find_distance(forest[tree], list(reversed(left))) #must be reversed
    right = [forest[(x,tree_y)] for x in range(tree_x+1,maxX)]
    right_distance = find_distance(forest[tree], right)
    up = [forest[(tree_x, y)] for y in range(0, tree_y)]
    up_distance = find_distance(forest[tree], list(reversed(up))) #must be reversed
    down = [forest[(tree_x, y)] for y in range(tree_y+1, maxY)]
    down_distance = find_distance(forest[tree], down)
    return left_distance * right_distance * up_distance * down_distance

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

#Task1
forest, maxX, maxY = scan_forest(lines)
visible_trees = find_visible_trees(forest, maxX, maxY)
print("Task 1:", len(visible_trees))

#Task2:
scenic_score = dict()
for tree in visible_trees:
    scenic_score[tree] = count_scenic_score(forest, maxX, maxY, tree)
print("Task 2:", max(scenic_score.values()))
print("Runtime:", datetime.now()-start)