#Advent of Code 2022: Day 14:
from pprint import pprint as pp
def create_cave(lines):
    cave = dict()
    for line in lines:
        corners = line.split(" -> ")
        for i in range(len(corners)-1):
            begin, end = corners[i:i+2]
            beginX, beginY = list(map(int, begin.split(",")))
            endX, endY = list(map(int, end.split(",")))
            dx = beginX - endX
            dy = beginY - endY
            if dx == 0: #vertical
                if endY < beginY:
                    endY, beginY = beginY, endY
                for y in range(beginY, endY+1, 1):
                    cave[(beginX, y)] = "#"
            if dy == 0: #horizontal
                if endX < beginX:
                    endX, beginX = beginX, endX
                for x in range(beginX, endX+1, 1):
                    cave[(x, beginY)] = "#"
    return cave

def print_cave(cave):
    for y in range(0,10):
        for x in range(493, 504):
            if (x,y) in cave.keys():
                print(cave[(x,y)], end="")
            else:
                print(".", end="")
        print("")

with open("test.txt") as file:
    lines = file.read().splitlines()

cave = create_cave(lines)
print_cave(cave)