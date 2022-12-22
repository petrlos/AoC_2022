#Advent of Code 2022: Day 21:

import re
def part1(lines):
    monkeys = {}
    done = False
    while not done:
        for line in lines:
            operation = line.split(": ")
            if operation[1].isnumeric():
                monkeys[operation[0]] = int(operation[1])
            else:
                monkey1, monkey2 = re_monkey.findall(operation[1])
                if monkey1 in monkeys.keys() and monkey2 in monkeys.keys():
                    if "+" in operation[1]:
                        monkeys[operation[0]] = monkeys[monkey1] + monkeys[monkey2]
                    if "-" in operation[1]:
                        monkeys[operation[0]] = monkeys[monkey1] - monkeys[monkey2]
                    if "*" in operation[1]:
                        monkeys[operation[0]] = monkeys[monkey1] * monkeys[monkey2]
                    if "/" in operation[1]:
                        monkeys[operation[0]] = monkeys[monkey1] // monkeys[monkey2]
            if "root" in monkeys.keys():
                done = True
    return monkeys["root"]

with open("data.txt") as file:
    lines = file.read().splitlines()

re_monkey = re.compile(r"\w{4}")
print(part1(lines))