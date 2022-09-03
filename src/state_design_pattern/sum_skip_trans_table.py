class SkipWithState:
    def __init__(self, el_to_skip=13):
        self._sum = 0
        self._state = 0

        self.transition_table = {
            # (state, input) : [nex_state, action]
            0: {
                    el_to_skip: {'next_state': 1, 'action': self.f_skip},
                    'default':          {'next_state': 0, 'action': self.f_sum}
                },
            1:
                {
                    el_to_skip: {'next_state': 1, 'action': self.f_skip},
                    'default':           {'next_state': 0, 'action': self.f_skip}
                }  # ,
        }

    def process_input(self,input_value):

        d1 = self.transition_table[self._state]
        d2 = d1.get(input_value, d1['default'])
        self._state = d2['next_state']
        d2['action'](input_value)

    def f_skip(self, el):
        pass

    def f_sum(self, el):
        self._sum += el


if __name__ == '__main__':
    nums1 = [1, 13, 10, 1, 13, 13, 13, 10, 1, 13]
    nums2 = [1, 13, 10, 1, 13, 13, 13, 10, 1]
    nums3 = [13, 10, 1, 13, 13, 13, 10, 1]

    s = SkipWithState(13)
    for el in nums1:
        s.process_input(el)
    print(s._sum)
    s = SkipWithState(13)
    for el in nums2:
        s.process_input(el)
    print(s._sum)
    s = SkipWithState(13)
    for el in nums3:
        s.process_input(el)
    print(s._sum)
