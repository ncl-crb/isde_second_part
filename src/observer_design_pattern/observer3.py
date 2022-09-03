class Publisher():
    def __init__(self, events):
        self.observers = {event: dict() for event in events}

    def get_observer(self, event):
        return self.observers[event]

    def register(self, event, obs, callback=None):
        default_method = 'update'
        if callback is None:
            callback = getattr(obs, default_method)
            self.observers[obs] = callback
        else:
            self.get_observer(event)[obs] = callback

    def unregister(self,event, obs):
        del self.get_observer(event)[obs]

    def dispatch(self, event, msg):
        for obs, method in self.get_observer(event).items():
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
    # driver

    # possible events are ('lunch', 'happyhour')
    publisher = Publisher(['lunch', 'happyhour'])

    bob = SubscriberOne('Bob')
    alice = SubscriberOne('Alice')
    john = SubscriberTwo('John')

    # bob and john are interested in the event 'lunch'
    publisher.register('lunch', bob)  # implicitly uses the 'update()' method
    publisher.register('lunch', john, john.receive)  # explicitly uses the 'receive()' method

    # alice and john are interested in the event 'happyhour'
    publisher.register('happyhour', alice)  # implicitly uses the 'update()' method
    publisher.register('happyhour', john, john.receive)  # explicitly uses the 'receive()' method

    # send a message
    print('\nLUNCHTIME!')
    publisher.dispatch('lunch', 'Lunchtime!')  # event, message
    print('\nHAPPYHOUR!')
    publisher.dispatch('happyhour', 'HAPPY HOUR!')  # event, message

    print("\nNow  john is no longer interested in event 'happyhour'")
    print("but he remains interested in event 'lunch'\n")

    publisher.unregister('happyhour', john)

    # send a message
    print('\nLUNCHTIME!')
    publisher.dispatch('lunch', 'Lunchtime!')  # event, message
    print('\nHAPPYHOUR!')
    publisher.dispatch('happyhour', 'HAPPY HOUR!')  # event, message
