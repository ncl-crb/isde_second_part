"""
Exercise 4 slides OOP_2 n°31
"""
import copy


class Engine():
    def __init__(self, displacement=1000):
        self.displacement = int(displacement)


class Wheel():
    def __init__(self, pressure=1):
        self.pressure = pressure


class Seat():
    def __init__(self, color=1):
        self.color = color


class Car():
    def __init__(self, displacement=1000, n_wheels=2, presseure=7, n_seats=5):
        self.engine = Engine(displacement)  # create an engine
        self.seats = [Seat() for i in range(n_seats)]  # create a list of wheels
        self.wheels = [Wheel(presseure) for i in range(n_wheels)]  # create a list of seats

    @property
    def displacement(self):
        return self.engine.displacement

    @property
    def n_seats(self):
        return len(self.seats)

    @property
    def wheels_pressure(self):
        pressures = []
        for i in self.wheels:
            pressures.append(i.pressure)
        return pressures


def main():
    # Client
    # input parameters with default
    # displacement=1000, n_wheels=4, pressure=7
    car = Car(2000, 4, 7)
    car2 = Car(1000, 2, 3, 2)

    print('displacement:', car.displacement)  # 2000
    print('wheel pressure:', car.wheels_pressure)  # [7, 7, 7, 7]
    print('n seats:', car.n_seats)  # 5

    print('displacement:', car2.displacement)
    print('wheel pressure:', car2.wheels_pressure)
    print('n seats:', car2.n_seats)

    car.wheels[0].pressure = 5

    print('\nWHEEL - PRESSURE after that we change the pressure of WHEEL 0 - CAR 1')
    print('car 1:', car.wheels[0].pressure)
    print('car 2:', car2.wheels[0].pressure)

if __name__ == "__main__":
    main()
