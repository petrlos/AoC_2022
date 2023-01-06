#Advent of Code 2022: Day 25

def snafu_to_decimal(number): #only for testing and to understand, not used to get result
    number = reversed(number)
    result = 0
    for index, char in enumerate(number):
        result += (5 ** index) * dictionary[char]
    return result

def snafu_plus_snafu(number1, number2):
    if len(number1) < len(number2): #number1 must be always longer
        number1, number2 = number2, number1
    diff = len(number1) - len(number2)
    number2 = "0"*diff + number2 #fill out number2 left with zeros
    result = []
    plus_one = 0
    for char1, char2 in zip(reversed(number1), reversed(number2)):
        #take digits from both numbers from left und sum up
        new_digit = dictionary[char1] + dictionary[char2] + plus_one
        plus_one = 0
        if new_digit > 2: #if sum is larger than 2: next number must add +1, actual number number +5
            plus_one = 1
            new_digit = new_digit - 5
        elif new_digit < -2: #if sum is smaller than -2: next number must add -1, actual number number  +5
            plus_one = -1
            new_digit = new_digit + 5
        result.append(new_digit)
    if plus_one == 1:
        result.append(1)
    snafu = ""
    for digit in reversed(result):
        snafu += dictionary_back[digit]
    return snafu

#MAIN
dictionary = dict(zip("210-=", range(2,-3,-1)))
dictionary_back = dict(zip(range(2,-3,-1),"210-=", ))

with open("data.txt") as file:
    numbers = file.read().splitlines()

result_snafu_sum = ""
for number in numbers:
    result_snafu_sum = snafu_plus_snafu(result_snafu_sum, number)
print("Result:",result_snafu_sum)