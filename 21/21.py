#Advent of Code 2022: Day 21:
from datetime import datetime
time_start = datetime.now()
import re
def part1(lines):
    monkeys = {}
    done = False
    while not done:
        for line in lines[:]:
            operation = line.split(": ")
            if operation[1].isnumeric():
                monkeys[operation[0]] = int(operation[1])
                index = lines.index(line)
                lines.pop(index)
            else:
                monkey1, monkey2 = re_monkey.findall(operation[1])
                if monkey1 in monkeys.keys() and monkey2 in monkeys.keys():
                    if "+" in operation[1]:
                        monkeys[operation[0]] = monkeys[monkey1] + monkeys[monkey2]
                        index = lines.index(line)
                        lines.pop(index)
                    if "-" in operation[1]:
                        monkeys[operation[0]] = monkeys[monkey1] - monkeys[monkey2]
                        index = lines.index(line)
                        lines.pop(index)
                    if "*" in operation[1]:
                        monkeys[operation[0]] = monkeys[monkey1] * monkeys[monkey2]
                        index = lines.index(line)
                        lines.pop(index)
                    if "/" in operation[1]:
                        monkeys[operation[0]] = monkeys[monkey1] // monkeys[monkey2]
                        index = lines.index(line)
                        lines.pop(index)
            if "root" in monkeys.keys():
                done = True
    return monkeys["root"]

with open("data.txt") as file:
    lines = file.read().splitlines()

re_monkey = re.compile(r"\w{4}")
print("Task 1:",part1(lines))