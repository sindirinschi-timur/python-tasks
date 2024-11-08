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

class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, battery):
        super().__init__(reg_num, max_speed)
        self.battery = battery

class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, fuel):
        super().__init__(reg_num, max_speed)
        self.fuel = fuel
