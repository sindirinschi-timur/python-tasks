from car import Car

new_car = Car("ABC-123", 142)
print(new_car.reg_num, new_car.max_speed, new_car.current_speed, new_car.distance)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print(f"current speed {new_car.current_speed} km/h")

new_car.accelerate(-200)
print(f"final speed {new_car.current_speed} km/h")