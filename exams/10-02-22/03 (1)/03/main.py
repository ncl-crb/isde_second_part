from abc import ABC, abstractmethod

class State(ABC):
    def process(self, obj, el):
        self._action(obj, el)
        self._change_state(obj, el)

    @abstractmethod
    def _action(self, obj, el):
        pass

    @abstractmethod
    def _change_state(self, obj, el):
        pass

class State0(State):
    def _action(self, obj, el):
        print(el)

    def _change_state(self, obj, el):
        if el == 'h':
            obj.id_state = State1()

class State1(State):
    def _action(self, obj, el):
        print(el)

    def _change_state(self, obj, el):
        if el == 'h':
            obj.id_state = State0()
        else:
            obj.id_state = State2()

class State2(State):
    def _action(self, obj, el):
        if el == 'h':
            print(el)

    def _change_state(self, obj, el):
        if el == 'h':
            obj.id_state = State0()
        else:
            obj.id_state = State1()

class Printer:
    def __init__(self):
        self.id_state = State0()

    def process(self, el):
        self.id_state.process(self, el)



class PrinterTable:
    def __init__(self):
        self.id_state = 0
        self.transition_table = {
            0 : { 'h': {'action': self.f_print, 'next_state': 1},
                  'default_input': {'action': self.f_print, 'next_state': 0}
                  },

            1: { 'h': {'action': self.f_print, 'next_state': 0},
                 'default_input':{'action': self.f_print, 'next_state': 2}
                 },

            2: { 'h': {'action': self.f_print, 'next_state': 0},
                 'default_input':{'action': self.f_null, 'next_state': 1}
                 }

        }

    def f_print(self, el):
        print(el)

    def f_null(self, el):
        pass

    def _retrieve_action_state(self, el):
        current_state_dict = self.transition_table[self.id_state]
        default_action = current_state_dict['default_input']
        action_state_dict = current_state_dict.get(el, default_action)
        return action_state_dict

    def _action(self, dict_action_state, el):
        dict_action_state['action'](el)

    def _change_state(self, dict_action_state):
        self.id_state = dict_action_state['next_state']

    def process_with_table(self, el):
        action_state_dict = self._retrieve_action_state(el)
        self._action(action_state_dict, el)
        self._change_state(action_state_dict)
if __name__ == '__main__':
    ## COMPLETE THE CODE!
    print("\n\n")

    p = Printer()
    elements = ['a', 'e', 'h', 'i', 'o', 'u', 'w', 'h', 'a', 'e', 'i']

    print('STATE DESIGN PATTER')
    for el in elements:
        p.process(el)

    print('\n')

    pt=PrinterTable()

    print('TRANSITION TABLE')
    for el in elements:
        pt.process_with_table(el)

""" OUTPUT:


MONDAY - FRIDAY
a
A
B
B
3
3



SATURDAY - SUNDAY
s2 ->  New Strategy!
s1 ->  New Strategy!
A
a  ASCII ->  97
B
B  ASCII ->  66
3  -> IT IS A NUMBER!
3  ASCII ->  51



MONDAY - FRIDAY
s2 ->  New Strategy!
a
A
B
B
3
3



"""