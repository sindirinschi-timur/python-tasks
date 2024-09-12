from os import remove


def kill_uneven(numbers):
    for number in numbers:
        if number % 2 != 0:
            numbers.remove(number)

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numbers)
    kill_uneven(numbers)
    print(numbers)

if __name__ == '__main__':
    main()

