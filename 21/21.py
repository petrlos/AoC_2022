#Advent of Code 2022: Day 21:
from datetime import datetime
time_start = datetime.now()
import re
def monkey_shouter(lines, humn = -1):
    monkeys = {}
    if humn > 0: #for part 1 take humn from *.txt
        monkeys["humn"] = humn
    done = False
    while not done: #run through all instructions as long, as "root" found
        for line in lines[:]:
            operation = line.split(": ")
            if operation[1].isnumeric():
                if operation[0] not in monkeys.keys():
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
                        monkeys[operation[0]] = monkeys[monkey1] / monkeys[monkey2]
            if "root" in monkeys.keys():
                done = True
    return monkeys

def part2():
    top = 10000000000000
    bottom = 0
    while True: #binary search, for my input aproximately 50 numbers needed
        mid = (top + bottom) // 2
        monkeys = monkey_shouter(lines, mid)
        monkey1, monkey2 = monkeys["vpmn"], monkeys["pqtt"] #keys that must be the same
        if monkey1 < monkey2:
            top = mid
        elif monkey1 > monkey2:
            bottom = mid
        elif monkey1 == monkey2:
            break
    return mid

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

re_monkey = re.compile(r"\w{4}")

#Task 1
task1 = monkey_shouter(lines)
print("Task 1:", task1["root"])

#Task2
result = part2()
print("Part 2:", result)
print("Total runtime:", datetime.now() - time_start) #my input +-3sec