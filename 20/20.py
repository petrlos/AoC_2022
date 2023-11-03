#Advent of Code 2022: Day 20
class Node:
    def __init__(self, number):
        self.value = number
        self.left = None
        self.right = None
    def __str__(self):
        return self.value

def print_numbers(a,b,c,start=False):
    num = numbers[0]
    if not start:
        print("{0} moves between {1} and {2}".format(a,b,c))
    for i in range(len(numbers)):
        print(num.value, " ", end="")
        num = num.right
    print("\n")

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

#vytvori list instanci tridy Node bez definovaneho odkazu na leveho a praveho clena
numbers = [Node(int(number)) for number in lines]

for i in range(len(numbers)):
    #circular linked list - modulo % zajisti "nepreteceni" listu a napojeni do kruhu
    #tzn. i=0 vrati len(numbers) = posledni clen, index posledniho clena + 1 vrati 0 = prvni clen
    numbers[i].left = numbers[(i-1) % len(numbers)]
    numbers[i].right = numbers[(i+1) % len(numbers)]

print("Initial arrangement")
print_numbers(0,0,0,start=False)

for num in numbers:
    if num.value == 0:
        zero = num #save position=index in list of zero
    target = num
    if num.value > 0: #move right
        for _ in range(num.value):
             target = target.right
        #delete number from current position
        num.right.left = num.left #vlevo od nasledujiciho bude predchozi
        num.left.right = num.right #vpravo od predchoziho bude nasledujici
        #insert on new position
        target.right.left = num #nasledujici od targetu bude vlozene cislo
        num.right = target.right #od vlozeneho cisla vpravo bude nasledujici cislo
        target.right = num #vpravo od targetu bude vlozene cislo
        num.left = target #vlevo od cisla bude target
        print_numbers(num.value, target.value, target.right.value)
    elif num.value < 0: #move left
        for _ in range(-num.value):
             target = target.left
        #delete number from current position
        num.right.left = num.left
        num.left.right = num.right
        #insert on new position
        target.left.right = num
        num.right = target
        target.left = num
        num.left = target.left
        print_numbers(num.value, target.value, target.right.value)
