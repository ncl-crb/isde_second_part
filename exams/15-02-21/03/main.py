from abc import ABC, abstractmethod


class SumEvenOdd():
    def __init__(self):
        self.state = SumEven()
        self.sum = 0

    def process_input(self, el):
        self.state.action(self, el)


class State(ABC):
    def __init__(self):
        self.last_sum = 0

    def process_input(self, obj, el):
        self.action(obj, el)

    @abstractmethod
    def action(self, obj, el):
        pass

    @abstractmethod
    def change_state(self, obj, el):
        pass

    def _print_sum(self, obj):
        print(obj.sum)

    def _reset(self, obj):
        obj.sum = 0

    def _check_even_odd(self, el):
        return int(el) % 2 == 0


class SumEven(State):

    def action(self, obj, el):
        if el == 'e':
            return
        elif el == 'o':
            self.change_state(obj, el)
        elif el == 'p':
            self._print_sum(obj)
        elif el == 'r':
            self._reset(obj)
        elif self._check_even_odd(el):
            obj.sum += int(el)
        else:
            return

    def change_state(self, obj, el):
        obj.sum -= self.last_sum
        obj.state = SumOdd()
        self._reset(obj)

class SumOdd(State):
    def action(self, obj, el):
        if el == 'o':
            return
        elif el == 'e':
            self.change_state(obj, el)
        elif el == 'p':
            self._print_sum(obj)
        elif el == 'r':
            self._reset(obj)
        elif not self._check_even_odd(el):
            obj.sum += int(el)
        else:
            return

    def change_state(self, obj, el):
        obj.sum -= self.last_sum
        obj.state = SumEven()
        self._reset(obj)


if __name__ == '__main__':
    # Use exactly this 'MAIN'
    # This code must run correctly, producing the output in the comments
    list_input = ['1', '2', '3', '4', '5', 'p',  # 6
                  '1', '2', '3', 'e', '4', '5', 'p',  # 12
                  'r', 'p',  # 0
                  '1', '2', '3', 'p',  # 2
                  'o',
                  '1', '2', '3', '4', '5', 'p',  # 9
                  '1', '2', '3', 'o', '4', '5', 'p',  # 18
                  'r', 'p',  # 0
                  '1', '2', '3', 'p'  # 4
                  ]
    s = SumEvenOdd()
    for el in list_input:
        s.process_input(el)

    """
    6
    12
    0
    2
    9
    18
    0
    4
    """
