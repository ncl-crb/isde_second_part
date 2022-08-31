from abc import ABC, abstractmethod

#  module: strategy
class Strategy(ABC):

    @abstractmethod
    def add_drink(self, n_drinks, price):
        pass

    @abstractmethod
    def get_actual_dress(self):
        pass


class NormalHour:
    def add_drink(self, value):
        return value

    def get_actual_dress(self):
        print('normal dress')


class HappyHour:
    def add_drink(self, value):
        happy_hour_discount = 0.5

        return value * happy_hour_discount

    def get_actual_dress(self):
        print('happy hour dress')

#  module: customer
class Customer:
    def __init__(self, strategy):
        self.cost = 0
        self._strategy = strategy

    def add_drink

if __name__ == '__main__':
    # NORMAL BILLING
    customer1 = CustomerNormalHour()
    customer1.add_drink(1, 7)
    customer1.get_actual_dress()
    # START HAPPY HOUR (50% discount)
    customer1.__class__ = CustomerHappyHour
    # You are changing class at runtime!
    # It is possible, but are we sure it is a good idea?
    customer1.add_drink(2, 5)
    customer1.get_actual_dress()
    # FINAL BILL
    customer1.get_actual_dress()
    customer1.print_bill()  # 12
