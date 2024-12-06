import race
from race import Race
from car import Car
import random

def main():
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        reg_num = f"ABC-{i}"
        cars.append(Car(reg_num, max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)
    print(f"Starting the {race.name} race! Circuit distance: {race.length} km.")

    hours_passed = 0
    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1

        if hours_passed % 10 == 0:
            print(f"Status after {hours_passed} hours:")
            race.print_status()

    print("Final race status:")
    race.print_status()

if __name__ == "__main__":
    main()
