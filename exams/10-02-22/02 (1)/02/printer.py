from abc import ABC, abstractmethod


class Printer:
    def __init__(self):
        self.state = Print()

    def process(self, el):
        self.state.process(self, el)


class State(ABC):
    changer_value = 'h'

    def process(self, obj, el):
        self._action(obj, el)
        self._change_state(obj, el)

    @abstractmethod
    def _change_state(self, obj, el):
        pass

    @abstractmethod
    def _action(self, obj, el):
        pass


class Print(State):
    def _action(self, obj, el):
        print(el)

    def _change_state(self, obj, el):
        if el == self.changer_value:
            obj.state = PrintFirst()


class PrintFirst(State):
    def _action(self, obj, el):
        print(el)

    def _change_state(self, obj, el):
        if el == self.changer_value:
            obj.state = Print()
        else:
            obj.state = NotPrint()


class NotPrint(State):
    def _action(self, obj, el):
        if el == self.changer_value:
            print(el)

    def _change_state(self, obj, el):
        if el != self.changer_value:
            obj.state = PrintFirst()
        else:
            obj.state = Print()


###################################

class PrinterTransTable:
    def __init__(self):
        self.state = 0
        self.changer_value = 'h'
        # (state_0, input_0): {action: action, next_state: next_state},
        self.transition_table = {
            0: {
                self.changer_value: {'action': self._print, 'next_state': 1},
                'default': {'action': self._print, 'next_state': 0}
            },
            1: {
                self.changer_value: {'action': self._print, 'next_state': 0},
                'default': {'action': self._print, 'next_state': 2}
            },
            2: {
                self.changer_value: {'action': self._print, 'next_state': 0},
                'default': {'action': self._not_print, 'next_state': 1}
            }
        }

    def _print(self, el):
        print(el)

    def _not_print(self, el):
        pass

    def process(self, el):
        dict_action_state = self._retrieve_action_state(el)
        self._action(dict_action_state, el)
        self._transition_state(dict_action_state)

    def _retrieve_action_state(self, el):
        state_dict = self.transition_table[self.state]
        default_action = state_dict['default']
        action_dict = state_dict.get(el, default_action)
        return action_dict

    def _action(self, action, el):
        action['action'](el)

    def _transition_state(self, next_state):
        self.state = next_state['next_state']
