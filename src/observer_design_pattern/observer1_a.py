class Publisher():
    def __init__(self):
        self.observers = set()

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
    # to the the subscribers' set of the Publisher
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