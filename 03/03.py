#Advent of Code 2022: Day 3

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

#create list of priorities
numbers = range(1,53)
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
prioroties = dict(zip(letters,numbers))

#Task1
sum = 0
for line in lines:
    length = len(line)//2
    left, right = set(line[0:length]), set(line[length: ])
    onlyOne = str(list(left.intersection(right))[0]) #convert set to list, take 1st item
    sum += prioroties[onlyOne]
print("Task 1:", sum)

#Task2
sum = 0
for index in range(len(lines)//3):
    group = lines[index*3:(index*3) + 3] #create tripplets
    group = [set(setted) for setted in group]
    result = group[0].intersection(group[1]).intersection(group[2]) #intersection of all three sets
    sum += prioroties[list(result)[0]] #convert to list, take 1st item, count priority
print("Task 2:", sum)