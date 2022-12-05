#Advent of Code 2022: Day 5
import re
from collections import deque
def parseData(lines):
    stackCounter = 9
    instructions = []
    warehouse = [deque() for i in range(stackCounter)]
    warehouseReady = False
    for line in lines:
        if "move" in line:
            warehouseReady = True
        if not warehouseReady:
            for i in range(stackCounter):
                possibleCrate = line[1+i*4]
                if possibleCrate.isalpha():
                    warehouse[i].append(possibleCrate)
        else:
            instructions.append(list(map(int,regNum.findall(line))))
    return warehouse, instructions

def performMoves(warehouse, instructions):
    for instruction in instructions:
        count, moveFrom, moveTo = instruction
        for move in range(count):
            crateMoved = warehouse[moveFrom-1][0] #warehouse index starts with Nr. 1
            warehouse[moveTo-1].appendleft(crateMoved)
            warehouse[moveFrom-1].popleft()
    return warehouse

def performMoveLargeCrane(warehouse, instructions):
    for instruction in instructions:
        count, moveFrom, moveTo = instruction
        cratesMoved = list(warehouse[moveFrom-1])[0:count]
        warehouse[moveTo-1] = deque(cratesMoved) + warehouse[moveTo-1]
        for i in range(count):
            warehouse[moveFrom-1].popleft()
    return warehouse

#MAIN
regNum = re.compile(r"\d+")
with open("data.txt") as file:
    lines = file.read().splitlines()

#Task 1
warehouse, instructions = parseData(lines)
warehouse = performMoves(warehouse, instructions)
for line in warehouse:
    print(line[0], end="")

print(" ")
#Task2
warehouse, instructions = parseData(lines)
performMoveLargeCrane(warehouse, instructions)

for line in warehouse:
    print(line[0], end="")


