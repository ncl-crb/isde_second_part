class PiggyBank():
    def __init__(self, initial_amount, lower_threshold):
        self.account = initial_amount
        self.threshold = lower_threshold
        self.observers = set()

    def save(self, amount):
        self.account += amount

    def retrieve(self, amount):
        if amount < self.account:
            self.account -= amount
            if self.account < self.threshold:
                self.dispatch()
            return True
        else:
            return False

    def register(self, obs):
        self.observers.add(obs)

    def unregister(self, obs):
        self.observers.discard(obs)

    def dispatch(self):
        for obs in self.observers:
            print(obs.update() + ' ' + str(self.account) + '\n')


class Observer():
    def __init__(self, name):
        self.name = name

    def update(self):
        print('message from Observer ', self.name)
        return 'the amount is too low - it is only'
