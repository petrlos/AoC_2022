#Advent of Code 2022: Day 11
import math, re, datetime
start = datetime.datetime.now()
def parse_data(lines):
    lines = lines.split("\n\n")
    monkeys = []
    for index, monkey in enumerate(lines):
        monkey_lines = monkey.splitlines()
        for line in monkey_lines:
            if "items" in line:
                items = list(map(int, regNum.findall(line)))
            elif "Operation" in line:
                if "old * old" in line:
                    operator = "power"
                    value = 1
                elif "+" in line:
                    operator = "add"
                    value = int(regNum.findall(line)[0])
                elif "*" in line:
                    operator = "mul"
                    value = int(regNum.findall(line)[0])
            elif "Test" in line:
                test = int(regNum.findall(line)[0])
            elif "true" in line:
                true = int(regNum.findall(line)[0])
            elif "fals" in line:
                false = int(regNum.findall(line)[0])
        monkey = Monkey(items, operator, value, test, true, false)
        monkeys.append(monkey)
    return monkeys

class Monkey:
    def __init__(self, items, operator, operator_value, test, target_true, target_false):
        self.items = items
        self.operator = operator
        self.operator_value = operator_value
        self.test = test
        self.target_true = target_true
        self.target_false = target_false
        self.counter = 0

    def throw_item(self, item):
        if self.operator == "add":
            new_value = (item + self.operator_value) // 3
        elif self.operator == "mul":
            new_value = (item * self.operator_value) // 3
        else: #operator == "power":
            new_value = (item * item) // 3
        if new_value % self.test == 0:
            target = self.target_true
        else:
            target = self.target_false
        return target, new_value

    def throw_item_2(self, item, divisor):
        if self.operator == "add":
            new_value = (item + self.operator_value)
        elif self.operator == "mul":
            new_value = (item * self.operator_value)
        else: #operator == "power":
            new_value = (item * item)
        if new_value % self.test == 0:
            target = self.target_true
        else:
            target = self.target_false
        return target, new_value % divisor

def part1(monkeys):
    for round in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                target, value = monkey.throw_item(item)
                monkeys[target].items.append(value)
                monkey.counter += 1
            monkey.items = []
    inspections = sorted([monkey.counter for monkey in monkeys])[-2:]
    return inspections[0] * inspections[1]

def part2(monkeys):
    divisor = math.prod([monkey.test for monkey in monkeys])
    for round in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                target, value = monkey.throw_item_2(item, divisor)
                monkeys[target].items.append(value)
                monkey.counter += 1
            monkey.items = []
    inspections = sorted([monkey.counter for monkey in monkeys])[-2:]
    return inspections[0] * inspections[1]

#MAIN
with open("data.txt") as file:
    lines = file.read()

regNum = re.compile(r"\d+")
#Task1
monkeys = parse_data(lines)
print("Task 1:",part1(monkeys))

#Task2
monkeys = parse_data(lines)
print("Task 2:",part2(monkeys))

print("Runtime: ", datetime.datetime.now()-start)