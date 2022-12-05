#Advent of Code 2022: Day 5
import re
from collections import deque
def parseData(lines):
    #entry data must be edited - delete line with stack Nr. + empty line
    stackCounter = 9
    instructions = []
    warehouse = [deque() for i in range(stackCounter)]
    warehouseReady = False
    for line in lines:
        if "move" in line:
            warehouseReady = True
        if not warehouseReady:
            for i in range(stackCounter):
                possibleCrate = line[1+i*4] #each possible crate is in string on that position
                if possibleCrate.isalpha():
                    warehouse[i].append(possibleCrate)
        else:
            instructions.append(list(map(int,regNum.findall(line))))
    return warehouse, instructions

def performMovesSmallCrane(warehouse, instructions):
    for instruction in instructions:
        count, moveFrom, moveTo = instruction
        for move in range(count):
            crateMoved = warehouse[moveFrom-1][0] #warehouse index starts with Nr. 1
            warehouse[moveTo-1].appendleft(crateMoved)
            warehouse[moveFrom-1].popleft()
    return warehouse

def performMovesLargeCrane(warehouse, instructions):
    for instruction in instructions:
        count, moveFrom, moveTo = instruction
        cratesMoved = list(warehouse[moveFrom-1])[0:count] #deque cant be sliced as a list
        warehouse[moveTo-1] = deque(cratesMoved) + warehouse[moveTo-1]
        for i in range(count): #delete all moved crates
            warehouse[moveFrom-1].popleft()
    return warehouse

def printFinalState(warehouse):
    return "".join([char[0] for char in warehouse])

#MAIN
regNum = re.compile(r"\d+")
with open("data.txt") as file:
    lines = file.read().splitlines()

#Task 1
warehouse, instructions = parseData(lines)
warehouse = performMovesSmallCrane(warehouse, instructions)
print("Task 1:", printFinalState(warehouse))

#Task2
warehouse, instructions = parseData(lines)
performMovesLargeCrane(warehouse, instructions)
print("Task 2:", printFinalState(warehouse))