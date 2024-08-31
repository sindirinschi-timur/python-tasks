zanderLength = input("Enter the zander length (cm): ")
sizeLimit = 42

if float(zanderLength) < sizeLimit:
    sizeDifference = sizeLimit - float(zanderLength)
    print(f"Release the fish! Zander was {sizeDifference} cm below size limit.")
else:
    print("Good job, fish caught.")
