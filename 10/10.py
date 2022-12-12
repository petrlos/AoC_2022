#Advent of Code 2022: Day 10:
import re
from pprint import pprint as pp
def perforom_lines(lines):
    register_x = 1
    values_at_END = {} #for value DURING process N call value N-1
    for counter, line in enumerate(lines):
        register_x += line
        values_at_END[counter] = register_x
    return values_at_END

def get_part_1(values_at_END):
    check_sum = 0
    for i in range(19,220,40):
        check_sum += values_at_END[i] * (i + 1)
    return check_sum

def draw_letters(values_at_END):
    sprite = 1
    for i in range(0,240):
        if i % 40 == 0 and i > 0:
            print(" ")
        print("█", end="") if abs(sprite - i%40) <= 1 else print(" ", end="")
        sprite = values_at_END[i+1]

#MAIN
with open("data.txt") as file:
    lines = [0] + list(map(int, file.read().replace(" ","\n").replace("addx","0").replace("noop","0").splitlines()))

regNum = re.compile(r"-?\d+")

values_at_END = perforom_lines(lines)
print("Task 1:",get_part_1(values_at_END))

draw_letters(values_at_END)