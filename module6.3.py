def gallon_converter(gallons):
    liters = gallons * 3.78541
    return liters

def main():

    while True:
      gallons = float(input("Enter gallons: "))
      liters = gallon_converter(gallons)
      print(liters)
      if gallons < 0:
          break

if __name__ == '__main__':
    main()
