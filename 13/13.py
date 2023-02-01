#Advent of Code 2022: Day 13
import json

def compare(left, right):
    print(left, right)
    return True

with open("test.txt") as file:
    lines = file.read().split("\n\n")

check_sum = 0
for index, line in enumerate(lines, start=1):
    left, right = [json.loads(json_string) for json_string in line.split("\n")]
    if compare(left, right):
        check_sum += index