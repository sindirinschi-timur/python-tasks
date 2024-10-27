from elevator import Elevator


def main():
    elevator = Elevator(10, 20)
    elevator.go_to_floor(15)
    print(elevator.current_floor)
    elevator.go_to_floor(10)
    print(elevator.current_floor)

if __name__ == '__main__':
    main()