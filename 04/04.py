#Advent of Code 2022: Day 4
import re

#MAIN
regNum = re.compile(r"\d+")
with open("data.txt") as file:
    lines = file.read().splitlines()

checkSumPart1 = 0
checkSumPart2 = 0
for line in lines:
    intervals = list(map(int,regNum.findall(line)))
    leftStart, leftEnd = intervals[0], intervals[1]
    rightStart, rightEnd = intervals[2], intervals[3]
    if (rightStart >= leftStart and rightEnd <= leftEnd) \
            or (rightStart <= leftStart and rightEnd >= leftEnd):
        checkSumPart1 += 1
    if (leftEnd >= rightStart and leftStart <= rightStart) \
            or (rightStart <= leftStart and rightEnd >= leftStart):
        checkSumPart2 += 1

print("Task 1:",checkSumPart1)
print("Task 2:", checkSumPart2)