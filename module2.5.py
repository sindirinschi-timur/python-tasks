talents = input("Enter talents: ")
lots = input("Enter lots: ")
pounds = input("Enter pounds: ")
totalGrams = (20 * 32 * 13.3 * float(talents)) + (13.3 * float(lots)) + (32 * 13.3 * float(pounds))
kilograms = totalGrams // 1000
grams = totalGrams % 1000
print(totalGrams)
print(f"The weight in modern units: {kilograms} kilograms and {round(grams, 2)} grams ")