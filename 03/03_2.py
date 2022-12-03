#Advent of Code 2022: Day 3
import string
def listSetIntersection(lst):
    #returns ONE letter, that is intersections of items of a list (there is always a single one)
    result = set(lst[0])
    for item in lst:
        result = result.intersection(set(item))
    return list(result)[0]

def cutBagInHalf(bag):
    length = len(bag)
    left, right = bag[0:length//2], bag[length//2:]
    return [left, right]

#MAIN
prioroties = dict(zip(string.ascii_letters,range(1,53)))

with open("data.txt") as file:
    bags = file.read().splitlines()

#Task1
sum = 0
for bag in bags:
    bagCutted = cutBagInHalf(bag)
    getLetter = listSetIntersection(bagCutted)
    sum += prioroties[getLetter]
print(sum)

#Task2
sum = 0
for index in range(len(bags)//3):
    group = bags[index*3:(index*3) + 3] #create tripplets
    getLetter = listSetIntersection(group)
    sum += prioroties[getLetter]
print("Task 2:", sum)