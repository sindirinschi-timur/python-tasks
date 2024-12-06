year = input("Enter a year: ")

if year != int and int(year) <= 0:
    print("Invalid year.")
elif int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
    print("It's a leap year!")
else:
    print("It's not a leap year!")