#Advent of Code 2022: Day 4

import re
regNum = re.compile(r"\d+")

with open("data.txt") as file:
    lines = file.read().splitlines()

part1 = 0
part2 = 0
for line in lines:
    numbers = list(map(int, regNum.findall(line)))
    left = set(range(numbers[0], numbers[1]+1))
    right = set(range(numbers[2], numbers[3]+1))
    if left & right == left or left & right == right:
        #all numbers from left in right or from right in left
        part1 += 1
    if len(left & right) > 0:
        #at least one number in both
        part2 += 1
print("Task 1:", part1)
print("Task 2:", part2)