#Advent of Code 2022: Day 6

def solver(line, length):
    for index in range(len(line)):
        subset = set(line[index:index+length])
        if len(subset) == length:
            return (index+length)

#MAIN

with open("data.txt") as file:
    lines = file.read().splitlines()

print("Task 1:",solver(lines[0], 4))
print("Task 2:",solver(lines[0], 14))