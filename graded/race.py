from car import Car
import random
from tabulate import tabulate

class Race():
    def __init__(self, name, length, car_list):
        self.name = name
        self.length = length
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            delta_speed = random.randint(-10, 15)
            car.accelerate(delta_speed)
            car.drive(1)

    def print_status(self):
        car_data = [[car.reg_num, car.max_speed, car.current_speed, car.distance] for car in self.car_list]

        headers = ['Registration', 'Max Speed (km/h)', 'Current Speed (km/h)', 'Travelled Distance (km)']
        print(tabulate(car_data, headers=headers, tablefmt="grid"))

    def race_finished(self):
        for car in self.car_list:
            if car.distance >= self.length:
                return True
