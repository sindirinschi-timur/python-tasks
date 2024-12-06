def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def main():
    numbers = [10, 24, 4, 51, 94]
    print(sum_numbers(numbers))

if __name__ == '__main__':
    main()