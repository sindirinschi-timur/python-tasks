def main():
    airports = {}

    while True:
        choice = input("Choose: Enter a new airport (Type 1); Fetch airport data (Type 2); (Press Enter to quit) ")
        if choice == "1":
            icao = input("Enter ICAO Code: ").upper()
            airport = input("Enter airport name: ")
            airports[icao] = airport
        elif choice == "2":
            icao = input("Enter ICAO Code: ").upper()
            if icao in airports:
                airport = airports[icao]
                print(f"Airport {airport} has icao code {icao}.")
            else:
                print("Airport not found.")
        elif choice == "":
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()


