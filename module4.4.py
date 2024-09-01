import random

num = random.randint(1, 10)

while True:
    guess = input("Guess a number between 1 and 10: ")

    if int(guess) == num:
        print("Correct!")
        break
    elif 1 < int(guess) > 10:
        print("Please guess a number between 1 and 10: ")
    elif int(guess) < num:
        print("Too low!")
        continue
    elif int(guess) > num:
        print("Too high!")
        continue
    else:
        break
