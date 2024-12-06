from car import GasolineCar, ElectricCar

def main():
    tesla = ElectricCar("ABC-15", 180, 52.5)
    ferrari = GasolineCar("ACD-123", 165, 32.3)
    tesla.accelerate(tesla.max_speed)
    ferrari.accelerate(ferrari.max_speed)
    tesla.drive(3)
    ferrari.drive(3)

    print(f"Gasoline Car has driven {ferrari.distance} km")
    print(f"Electric Car has driven {tesla.distance} km")

if __name__ == "__main__":
    main()