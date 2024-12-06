import random
from tabulate import tabulate
from car import Car

def main():
    contestants = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        reg_num = f"ABC-{i}"
        contestants.append(Car(reg_num, max_speed))

    race_finished = False
    while not race_finished:
        for car in contestants:
            delta_speed = random.randint(-10, 15)
            car.accelerate(delta_speed)
            car.drive(1)
            if car.distance >= 10000:
                race_finished = True
                break

    car_data = [[car.reg_num, car.max_speed, car.current_speed, car.distance] for car in contestants]

    headers = ['Registration', 'Max Speed (km/h)', 'Current Speed (km/h)', 'Travelled Distance (km)']
    print(tabulate(car_data, headers=headers, tablefmt="grid"))

if __name__ == '__main__':
    main()


