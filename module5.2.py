numbers = []

while True:
    number = input("Enter a number (Press enter to Quit): ")

    if number == "":
        break
    elif number.isdigit():
        numbers.append(number)

greatest_numbers = []
for i in range(min(5, len(numbers))):
        greatest_numbers.append(numbers[i])

greatest_numbers.sort(reverse=True)
print(greatest_numbers)