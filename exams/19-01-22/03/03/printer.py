from abc import ABC, abstractmethod

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(self.name, '->', message)

class Strategy(ABC):
    @abstractmethod
    def process_1(self, el):
        pass

    @abstractmethod
    def process_2(self, el):
        pass


class Strategy1(Strategy):
    def process_1(self, el):
        print(el)

    def process_2(self, el):
        print(el.upper())


class Strategy2(Strategy):
    def process_1(self, el):
        if el.isnumeric():
            print(el, ' -> IT IS A NUMBER!')
        else:
            print(el.upper())

    def process_2(self, el):
        print(el, ' ASCII -> ', ord(el))


class Printer:
    def __init__(self, processor=Strategy1()):
        self._processor = processor
        self.observer = set()

    @property
    def processor(self):
        return self._processor

    @processor.setter
    def processor(self, new_strategy):
        if self.processor != new_strategy:
            self._processor = new_strategy
            self.dispatch('New Strategy!')

    def process_1(self, el):
        self.processor.process_1(el)

    def process_2(self, el):
        self.processor.process_2(el)

    def register(self, an_observer):
        self.observer.add(an_observer)

    def unregister(self, an_observer):
        self.observer.discard(an_observer)

    def dispatch(self, message):
        for obs in self.observer:
            obs.update(message)
