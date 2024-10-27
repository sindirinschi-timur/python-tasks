class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

new_car = Car("ABC-123", 142)
print(new_car.reg_num, new_car.max_speed, new_car.current_speed, new_car.distance)
