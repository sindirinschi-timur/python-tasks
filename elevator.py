class Elevator:
    def __init__(self, bottom, top, num):
        self.num_of_elevators = num
        self.bottom = bottom
        self.top = top
        self.current_floor = self.bottom

    def floor_up(self):
        if self.current_floor < self.target_floor:
            self.current_floor += 1
            print(f"Current Floor: {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.target_floor:
            self.current_floor -= 1
            print(f"Current Floor: {self.current_floor}")

    def go_to_floor(self, target_floor):
        self.target_floor = target_floor
        if self.bottom < target_floor > self.top:
            print("Invalid Floor")
            return

        while self.current_floor < self.target_floor:
            self.floor_up()
        while self.current_floor > self.target_floor:
            self.floor_down()

