from math import sqrt


def pizza_seller(diameter, price):
    diameter = diameter / 100
    radius = diameter / 2
    area = 2 * 3.14 * sqrt(radius)
    pizza_wholesale = price / area
    return pizza_wholesale

def main():
    price1 = float(input(f"Enter 1st pizza price: "))
    diameter1 = float(input("Enter 1st diameter (cm): "))
    price2 = float(input(f"Enter 2nd pizza price: "))
    diameter2 = float(input("Enter 2nd diameter (cm): "))
    pizza_wholesale1 = pizza_seller(diameter1, price1)
    pizza_wholesale2 = pizza_seller(diameter2, price2)

    if pizza_wholesale1 > pizza_wholesale2:
        print(f"Second pizza provides better value at {pizza_wholesale2:.2f} Euros/m2.")
    elif pizza_wholesale2 < pizza_wholesale1:
        print(f"First pizza provides better value at {pizza_wholesale1:.2f} Euros/m2.")
    else:
        print(f"The pizzas provide the same value at {pizza_wholesale1:.2f} Euros/m2.")

if __name__ == "__main__":
    main()

