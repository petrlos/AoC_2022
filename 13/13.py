#Advent of Code 2022: Day 13
import ast
def compare_list(left, right):
    if len(left) > len(right):
        return False
    elif len(left) < len(right):
        return True
    else:
        for item1, item2 in zip(left, right):
            if item1 > item2:
                return False
    return True

def compare_numbers(numbers):
    num1, num2 = numbers
    cut1 = num1[0]
    cut2 = num2[0]
    while len(cut1) > 0:
        if isinstance(cut1, int):
            cut1 = [cut1]
        if isinstance(cut2, int):
            cut2 = [cut2]
        compare_list(cut1, cut2)



with open("test.txt") as file:
    lines = file.read().split("\n\n")

for line in lines:
    numbers = [ast.literal_eval(lst) for lst in line.split("\n")]
    compare_numbers(numbers)

num1= [7,7,7]
num2= [7,7,7,7]
print(compare_list(num1, num2))