#Advent of Code 2022: Day 1

#MAIN

with open("data.txt") as file:
    lines = file.read().splitlines()

elves = []
elf = 0
for line in lines:
    if line == "": #Elf is done - add his sum to list and count a new one
        elves.append(elf)
        elf = 0
    else: #Elf not yet done - sumup
        elf += int(line)

print("Task 1:", max(elves)) #Elf with most Calories
print("Task 2:", sum(sorted(elves)[-3:])) #Top 3 Elves