"""
Exercise 3 slides OOP_2 """
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
    def __init__(self, engine, wheels, seats):
        self.engine = engine
        self.seats = copy.deepcopy(seats)
        self.wheels = copy.deepcopy(wheels)

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

    # @displacement.setter
    # def displacement(self, value):
    #     self.displacement = value
    #
    # @property
    # def n_seats(self):
    #     return len(self.seats)


def main():
    # Client
    engine = Engine(2000)  # create an engine
    wheels = [Wheel(7) for i in range(4)]  # create a list of wheels
    seats = [Seat() for i in range(4)]  # create a list of seats

    car = Car(engine, wheels, seats)
    print('displacement:', car.displacement)
    print('wheel pressure:', car.wheels_pressure)
    print('n seats:', car.n_seats)

    car2 = Car(engine, wheels, seats)
    car.wheels[0].pressure = 5

    print('displacement:', car.displacement)
    print('wheel pressure:', car.wheels_pressure)
    print('wheel pressure:', car2.wheels_pressure)
    print('n seats:', car.n_seats)


if __name__ == "__main__":
    main()
