class Engine():
    def __init__(self, displacement=1000):
        self.displacement = int(displacement)


class EngineWithWheels(Engine):
    def __init__(self, displacement=1000, n_wheels=4, pressure=1):
        super().__init__(displacement)
        self.wheels_pressure = [int(pressure)]*n_wheels
        self.n_wheels = int(n_wheels)


class Car(EngineWithWheels):
    def __init__(self, displacement=1000, n_wheels=4, pressure=1, n_seats=5):
        super().__init__(displacement=displacement, n_wheels=n_wheels, pressure=pressure)
        self.n_seats = int(n_seats)


def main():
    # Client
    car = Car(2000, 4, 7, 5)
    # input parameters with default
    # displacement=1000, n_wheels=4, pressure=7, n_weats=5
    print('displacement:', car.displacement)  # 2000
    print('wheel pressure:', car.wheels_pressure)  # [7, 7, 7, 7]
    print('n seats:', car.n_seats)  # 5


if __name__ == "__main__":
    main()
