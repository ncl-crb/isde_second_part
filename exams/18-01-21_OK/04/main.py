from abc import ABC, abstractmethod


class State(ABC):
    def process_input(self, obj, el):
        self._action(obj, el)
        self._change_stae(obj, el)

    @abstractmethod
    def _action(self, obj, el):
        pass

    @abstractmethod
    def _change_stae(self, obj, el):
        pass

    def _printWrong(self):
        print('Wrong sequence!')


class State0(State):

    def _action(self, obj, el):
        if el != 'HAM':
            self._printWrong()

    def _change_stae(self, obj, el):
        if el == 'HAM':
            obj.state = Ham()
        else:
            obj.state = State0()


class Ham(State):
    def _action(self, obj, el):
        if el != 'SPAM':
            self._printWrong()

    def _change_stae(self, obj, el):
        if el == 'SPAM':
            obj.state = Spam()
        elif el == 'HAM':
            obj.state = Ham()
        elif el == 'JAM':
            obj.state = State0()


class Spam(State):
    def _action(self, obj, el):
        if el != 'JAM':
            self._printWrong()
        else:
            print('HAM - SPAM - JAM')

    def _change_stae(self, obj, el):
        if el == 'JAM':
            obj.state = State0()
        elif el == 'HAM':
            obj.state = Ham()
        else:
            obj.state = State0()


class Machine:
    def __init__(self, init_State=State0()):
        self.state = init_State

    def process_input(self, el):
        self.state.process_input(self, el)


if __name__ == '__main__':

    # MAIN
    sequence1 = ['HAM', 'SPAM', 'JAM']
    sequence2 = ['X',
                 'HAM', 'SPAM', 'JAM',
                 'X']
    sequence3 = ['HAM', 'SPAM', 'JAM',
                 'HAM', 'SPAM', 'X', 'JAM',
                 'HAM', 'SPAM', 'JAM']
    print('\nSEQUENCE 1')
    m = Machine()
    for s in sequence1:
        m.process_input(s)
    print('\nSEQUENCE 2')
    m = Machine()
    for s in sequence2:
        m.process_input(s)
    print('\nSEQUENCE 3')
    m = Machine()
    for s in sequence3:
        m.process_input(s)

        """
        SEQUENCE 1
        HAM - SPAM - JAM
        SEQUENCE 2
        wrong sequence!
        HAM - SPAM - JAM
        wrong sequence!
        SEQUENCE 3
        HAM - SPAM - JAM
        wrong sequence!
        wrong sequence!
        HAM - SPAM – JAM
        """
