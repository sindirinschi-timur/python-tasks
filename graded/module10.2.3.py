from building import Building

def main():
    building1 = Building(1, 10, 4)

    building1.run_elevator(3, 9)

    building1.fire_alarm()

if __name__ == '__main__':
    main()