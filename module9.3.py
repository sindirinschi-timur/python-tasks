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


new_car = Car("ABC-123", 142)
print(new_car.reg_num, new_car.max_speed, new_car.current_speed, new_car.distance)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print(f"current speed {new_car.current_speed} km/h")

new_car.accelerate(-200)
print(f"final speed {new_car.current_speed} km/h")

