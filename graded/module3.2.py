cabinClass = input("Enter the cabin class (LUX; A; B; C): ")

if cabinClass == "LUX":
    print("Your cabin class is LUX: upper-deck cabin with a balcony.")
elif cabinClass == "A":
    print("Your cabin class is A: above the car deck, equipped with a window.")
elif cabinClass == "B":
    print("Your cabin class is B: windowless cabin above the car deck.")
elif cabinClass == "C":
    print("Your cabin class is C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")