import random

dice_toss = input("How many dice to roll?: ")
total = 0

for i in range(int(dice_toss)):
    dice = random.randint(1,6)
    total = total + dice

print(total)