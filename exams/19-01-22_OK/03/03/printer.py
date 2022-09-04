from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def process_1(self, el):
        pass

    @abstractmethod
    def process_2(self, el):
        pass


class Strategy1(Strategy):  # working day

    def process_1(self, el):
        print(el)

    def process_2(self, el):
        print(el.upper())



class Strategy2(Strategy):  # weekend
    def process_1(self, el):
        if el.isdigit():
            print(el, '-> IT IS A NUMBER!')
        else:
            print(el.upper())

    def process_2(self, el):
        print(el, ' ASCII -> ',ord(el))



class Printer():
    def __init__(self, strategy=Strategy1()):
        self._processor = strategy
        self.observers = set()

    @property
    def processor(self):
        return self._processor

    @processor.setter
    def processor(self, value):
        if value != self._processor:
            self.dispatch()
            self._processor = value
        else:
            self._processor = value

    def process_1(self, el):
        self._processor.process_1(el)

    def process_2(self, el):
        self._processor.process_2(el)

    def register(self, obs):
        self.observers.add(obs)
    def unregister(self, obs):
        self.observers.remove(obs)

    def dispatch(self):
        for obs in self.observers:
            obs.update()


class Observer:
    def __init__(self, name):
        self.name = name

    def update(self):
        print(self.name + ' -> New Strategy!')
