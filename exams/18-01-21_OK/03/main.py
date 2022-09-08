from abc import ABC, abstractmethod

class Observer:
    def __init__(self, name):
        self.name = name

    def below_threshold(self, value):
        print("\nmessage from ", self.name)
        print("the amount is too low - it is only", value)


class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, an_observer):
        self.subscribers.add(an_observer)

    def unregister(self, an_observer):
        self.subscribers.discard(an_observer)

    @abstractmethod
    def dispatch(self):
        pass


class PiggyBank(Publisher):
    def __init__(self, initial_amount, lower_threshold):
        super().__init__()
        self.amount = initial_amount
        self.lower_threshold = lower_threshold

    def dispatch(self):
        for subscriber in self.subscribers:
            subscriber.below_threshold(self.amount)

    def save(self, value):
        self.amount += value

    def retrieve(self, value):
        possible_withdraw = self.amount >= value
        if possible_withdraw:
            self.amount -= value
        if self.amount < self.lower_threshold:
            self.dispatch()
        return possible_withdraw


if __name__ == '__main__':
    # MAIN
    piggy_bank = PiggyBank(initial_amount=40, lower_threshold=20)
    obs1 = Observer('Observer 1')
    obs2 = Observer('Observer 2')
    piggy_bank.register(obs1)
    piggy_bank.register(obs2)
    piggy_bank.retrieve(15)
    piggy_bank.retrieve(15)
    piggy_bank.unregister(obs2)
    piggy_bank.retrieve(5)
