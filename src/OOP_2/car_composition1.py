class Engine():
    def __init__(self, displacement=1000):
        self.displacement = int(displacement)

    @property
    def displacement(self):
        return self._displacement

    @displacement.setter
    def displacement(self, value):
        self._displacement = value

class Wheels():
    def __init__(self, n_wheels=4, pressure=1):
        self.wheels_pressure = [int(pressure)]*n_wheels
        self.n_wheels = int(n_wheels)
        self.pressure = pressure

    @property
    def pressure(self):
        return self._pressure
    @property
    def wheels_pressure(self):
        return self._wheels_pressure

    @property
    def n_wheels(self):
        return self._n_wheels

    @pressure.setter
    def pressure(self, value):
        self._pressure = value

    @wheels_pressure.setter
    def wheels_pressure(self, value):
        self._wheels_pressure = value

    @n_wheels.setter
    def n_wheels(self, value):
        self._n_wheels = value
class Seats():
    def __init__(self, n_seats=5):
        self.n_seats = n_seats
    @property
    def n_seats(self):
        return self._n_seats

    @n_seats.setter
    def n_seats(self, value):
        self._n_seats = value
class Car():
    def __init__(self, engine, wheels, seats):
        self.n_seats = seats.n_seats
        self.displacement = engine.displacement
        self.wheels_pressure = wheels.pressure
        self.n_wheels = wheels.n_wheels

def main():
    # Client
    engine = Engine(2000)  # create an engine
    print(engine.displacement)
    engine.displacement = 2000
    wheels = Wheels(4, 7)  # create a list of wheels
    print(wheels.n_wheels, wheels.wheels_pressure)
    seats = Seats(5)  # create a list of seats
    print(seats.n_seats)
    car = Car(engine, wheels, seats)
    print('displacement:', car.displacement)
    print('wheel pressure:', car.wheels_pressure)
    print('n seats:', car.n_seats)

if __name__ == "__main__":
    main()