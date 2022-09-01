from abc import ABC, abstractmethod


#  module: strategy
class Strategy(ABC):

    @abstractmethod
    def add_drink(self, n_drinks, price):
        return n_drinks * price

    @abstractmethod
    def get_actual_dress(self):
        pass


class NormalHour(Strategy):
    def add_drink(self, n_drinks, price):
        return super().add_drink(n_drinks, price)

    def get_actual_dress(self):
        print('normal dress')


class HappyHour(Strategy):
    def add_drink(self, n_drinks, price):
        happy_hour_discount = 0.5
        return super().add_drink(n_drinks, price) * happy_hour_discount

    def get_actual_dress(self):
        print('happy hour dress')


#  module: customer
class Customer:
    def __init__(self, Strategy):
        self.cost = 0
        self.strategy = Strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, value):
        self._strategy = value

    def print_bill(self):
        print(self.cost)

    def add_drink(self, n_drinks, price):
        self.cost += self._strategy.add_drink(n_drinks, price)

    def get_actual_dress(self):
        self._strategy.get_actual_dress()


if __name__ == '__main__':
    # Prepare strategies

    normal_strategy = NormalHour()
    happy_hour_strategy = HappyHour()

    # NORMAL BILLING

    customer1 = Customer(normal_strategy)
    customer1.add_drink(1, 7)

    customer1.get_actual_dress()

    # START HAPPY HOUR (50% discount)

    customer1.strategy = happy_hour_strategy
    customer2 = Customer(happy_hour_strategy)

    customer2.add_drink(1, 7)

    customer1.add_drink(2, 5)
    customer2.add_drink(2, 5)
    customer1.get_actual_dress()

    # FINAL BILL
    customer1.get_actual_dress()

    customer1.print_bill()  # 12
    customer2.print_bill()  # 8.5
