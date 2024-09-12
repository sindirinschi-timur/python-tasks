number = int(input("Enter a number: "))

is_prime = False

if number == 0 or number == 1:
    print("It's not a prime number.")
elif number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime= True
            break

if is_prime:
    print("It's not a prime number.")
else:
    print("It's a prime number!")