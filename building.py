from elevator import Elevator

class Building:
    def __init__(self, bottom, top, elevator_count):
        self.bottom = bottom
        self.top = top
        self.elevator_count = elevator_count
        self.elevators = []
        for i in range(elevator_count):
            self.elevators.append(Elevator(self.bottom, self.top))

    def run_elevator(self, num, target_floor):
        self.elevators[num - 1].go_to_floor(target_floor)
