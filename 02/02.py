#Advent of Code 2022: Day 2

def game(opponent, player):
    if player == opponent:
        return 3 + scoreTable[player] # draw = 3Points
    elif [opponent, player] in [["C", "A"], ["A", "B"], ["B","C"]]:
        return 6 + scoreTable[player] #win = 6Points
    else:
        return scoreTable[player]

#MAIN

with open("data.txt") as file:
    lines = file.read().splitlines()

scoreTable = {"A":1, "B":2, "C":3}

#Task1
scoreCounter = 0
for line in lines:
    opponent, player = line.split(" ")
    decode = {"X": "A", "Y": "B", "Z": "C"}
    player = decode[player]
    scoreCounter += game(opponent, player)
print("Task 1:", scoreCounter)

#Task2
scoreCounter = 0
for line in lines:
    opponent, player = line.split(" ")
    if player == "Y": #draw
        player = opponent
    elif player == "X": #lose
        decode = {"A":"C", "B":"A", "C":"B"}
        player = decode[opponent]
    elif player == "Z": #win
        decode = {"A":"B", "B":"C", "C":"A"}
        player = decode[opponent]
    scoreCounter += game(opponent, player)

print("Task 2:",scoreCounter)