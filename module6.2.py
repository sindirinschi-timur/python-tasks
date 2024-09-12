import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    sides = int(input("Enter number of sides: "))
    while True:
        dice = roll_dice(sides)
        print(dice)
        if dice == sides:
            break

if __name__ == '__main__':
    main()