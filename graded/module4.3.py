numbers = []

while True:
    num = input("Enter a number (press Enter to quit): ")
    numbers.append(num)
    if num == "":
        numbers[-1] = max(numbers)
        print(f"Smallest number: {min(numbers)} Largest number: {max(numbers)}")
        break
