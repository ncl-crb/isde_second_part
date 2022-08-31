
class Customer():

    def __init__(self):
        self.n_drinks = 0
        self.bill = 0

    def add_drink(self, n_drinks, price, happy_hour=False):
        happy_hour_discount = 0.5

        self.n_drinks += n_drinks
        if happy_hour:
            self.bill += (price * n_drinks) * happy_hour_discount
        else:
            self.bill += (price * n_drinks)

    @staticmethod
    def get_actual_dress(happy_hour=False):
        if happy_hour:
            print('happy hour dress')
        else:
            print('normal dress')

    def print_bill(self):
        print(self.bill)


def main ():
    # NORMAL BILLING
    customer1 = Customer()
    customer1.add_drink(1, 7)
    customer1.get_actual_dress()
    # START HAPPY HOUR (50% discount)
    customer1.add_drink(2, 5, happy_hour=True)
    customer1.get_actual_dress(happy_hour=True)
    # FINAL BILL
    customer1.get_actual_dress(happy_hour=True)
    customer1.print_bill()  # 12


if __name__ == '__main__':
    main()