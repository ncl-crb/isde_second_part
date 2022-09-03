class Publisher():
    def __init__(self):
        self.observers = dict()

    def register(self, obs, callback=None):
        default_method = 'update'
        if callback is None:
            callback = getattr(obs, default_method)
            self.observers[obs] = callback
        else:
            self.observers[obs] = callback

    def unregister(self, obs):
        del self.observers[obs]

    def dispatch(self, msg):
        for obs, method in self.observers.items():
            method(msg)


class SubscriberOne():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def update(self, msg):
        print(self._name + ' (Update)has recived the messagge **' + msg + '**')

class SubscriberTwo():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def receive(self, msg):
        print(self._name + ' (Recive) has recived the messagge **' + msg + '**')


if __name__ == '__main__':
    publisher = Publisher()
    bob = SubscriberOne('Bob')
    alice = SubscriberOne('Alice')
    john = SubscriberTwo('John')
    # explicitly uses the 'update()' method
    publisher.register(bob, bob.update)
    # implicitly uses the 'update()' method
    publisher.register(alice)
    # explicitly uses the 'receive()' method
    publisher.register(john, john.receive)
    # send a message
    publisher.dispatch('Lunchtime!')
    publisher.unregister(john)
    publisher.dispatch('Happy hour!')


