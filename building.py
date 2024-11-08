from elevator import Elevator

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"Running Elevator {elevator_number} to floor {target_floor}")
            self.elevators[elevator_number].go_to_floor(target_floor)
        else:
            print("Invalid elevator number")

    def fire_alarm(self):
        print("Fire alarm! Moving all elevators to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"Moving Elevator {i} to the bottom floor")
            elevator.go_to_floor(elevator.bottom_floor)
