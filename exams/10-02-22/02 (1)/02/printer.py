class PrinterTransT():
    def __init__(self, state=0):
        self.state = state
        self.set_print = True
        self.state_changer = 'h'

        self.transition_table = {
            0: {
                self.state_changer: {'next_state': 1, 'action': self.print},
                'default' : {'next_state': 0, 'action': self.print}
            },
            1: {
                self.state_changer: {'next_state': 0, 'action': self.print},
                'default': {'next_state': 1, 'action': self.jump}
            }
        }

    def print(self, ch):
        print(ch)

    def jump(self, ch):
        if self.set_print:
            print(ch)
            self.set_print = not self.set_print
        else:
#            print('else')
            self.set_print = not self.set_print

    def process(self, ch):
        d1 = self.transition_table[self.state]
        d2 = d1.get(ch, d1['default'])
        self.state = d2['next_state']
        d2['action'](ch)




class Printer():
    def __init__(self, state=0):
        self.state = state
        self.set_print = True
        self.state_changer = 'h'

    def process(self, ch):

        if self.state == 0:
            if ch != self.state_changer:
                print(ch)
            elif ch == self.state_changer:
                print(ch)
                self.state = 1
        elif self.state == 1:
            if ch != self.state_changer:
                if self.set_print:
                    print(ch)
                    self.set_print = not self.set_print
                else:
                    self.set_print = not self.set_print
                    return
            elif ch == self.state_changer:
                print(ch)
                self.state = 0
