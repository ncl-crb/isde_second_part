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



class Printer:
    def __init__(self, strategy):
        self.processor = strategy

    @property
    def processor(self):
        return self._processor

    @processor.setter
    def processor(self, value):
        self._processor = value

    def process_1(self, el):
        self._processor.process_1(el)

    def process_2(self, el):
        self._processor.process_2(el)


class Observer:
    pass
