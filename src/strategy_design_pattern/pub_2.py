from abc import ABC, abstractmethod


class Customer(ABC):

    def __init__(self):
        self.n_drinks = 0
        self.bill = 0

    @abstractmethod
    def add_drink(self, n_drinks, price):
        pass

    @abstractmethod
    def get_actual_dress():
        pass

    def print_bill(self):
        print(self.bill)


class CustomerNormalHour(Customer):
    def add_drink(self, n_drinks, price):
        self.bill += (price * n_drinks)

    @staticmethod
    def get_actual_dress():
        print('normal dress')


class CustomerHappyHour(Customer):
    def add_drink(self, n_drinks, price):
        happy_hour_discount = 0.5

        self.bill += (price * n_drinks) * happy_hour_discount

    @staticmethod
    def get_actual_dress():
        print('happy hour dress')


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
