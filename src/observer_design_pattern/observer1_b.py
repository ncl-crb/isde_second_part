class Publisher():
    def __init__(self):
        self.observers = set()
        self._a = 0

    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, value):
        if value >= 0 and value != self._a:
            self._a = value
            self.dispatch(f'Value changed. The new value is {self.a}')
        elif value == self._a:
            print('The value is not changed')
        elif value < 0:
            print("ERROR: negative value")

    def register(self, obs):
        self.observers.add(obs)

    def unregister(self, obs):
        self.observers.remove(obs)

    def dispatch(self, msg):
        for obs in self.observers:
            obs.update(msg)


class Subscriber():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def update(self, msg):
        print(self._name + ' has recived the messagge **' + msg + '**')


if __name__ == '__main__':
    publisher=Publisher() # the observed object
    bob=Subscriber('Bob') # an observer
    alice=Subscriber('Alice') # an observer
    john=Subscriber('John') # an observer

    # add the subscribers (bob, alice, john)
    # to the subscribers' set of the Publisher
    publisher.register(bob)
    publisher.register(alice)
    publisher.register(john)

    # send a message
    publisher.dispatch('Lunchtime!')
    # Bob received the message **Lunchtime!**
    # John received the message **Lunchtime!**
    # Alice received the message **Lunchtime!**
    print('\n')
    publisher.unregister(john)
    publisher.dispatch('Happy hour!')
    # Bob received the message **Happy hour!**
    # Alice received the message **Happy hour!**
    print('\n')
    print('\n')

    publisher.a = 10
    publisher.a = -10
    publisher.a = 3
    publisher.a = 3
