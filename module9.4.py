import random
from tabulate import tabulate

class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, delta_speed):
        self.current_speed += delta_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.distance += hours * self.current_speed


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


