#Advent of Code 2022: Day 20
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def schuffle_linked_list(multiplicator=1, rounds=1):
    #create a list of nodes
    linked_list = [Node(number*multiplicator) for number in numbers]
    #connect them to left and right
    for i in range(len(linked_list)):
        linked_list[i].left = linked_list[i - 1]
        linked_list[i].right = linked_list[(i + 1) % len(linked_list)]
    #modulo for large numbers - have to go only once around
    modulo = len(linked_list) - 1
    for i in range(rounds):
        for num in linked_list:
            if num.value == 0: #save the position of ZERO for counting final result
                final_target = num
                continue
            target = num
            if num.value > 0: #positive number - step right num.value-times to find target
                for _ in range(num.value % modulo):
                    target = target.right
            if num.value < 0: #negative number - step left num.value-times +1 to find target - insert always on right
                for _ in range((-num.value + 1) % modulo):
                    target = target.left
            # de-link current number
            num.right.left = num.left
            num.left.right = num.right
            # make a new connection
            target.right.left = num
            num.right = target.right
            target.right = num
            num.left = target
    result = []
    for i in range(3):
        for j in range(1000): #find position 1000th, 2000th and 3000th
            final_target = final_target.right
        result.append(final_target.value)
    return result

#MAIN
with open("data.txt") as file:
    numbers = list(map(int,file.read().splitlines()))

part1 = schuffle_linked_list()
print(f"Part 1: {part1}, sum = {sum(part1)}")

part2 = schuffle_linked_list(811589153, 10)
print(f"Part 2: {part2}, sum = {sum(part2)}")