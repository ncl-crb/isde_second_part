class Rectangle():
    def __init__(self, length, width, parameter_list):
        self._length = length
        self._width = width
        self.observers = {parameter : set() for parameter in parameter_list}

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value >= 0 and value != self._width:
            self._width = value
            for obs in self.observers['width']:
                obs.update(' : -> width has changed!')

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value >= 0 and value != self._length:
            self._length = value
            for obs in self.observers['length']:
                obs.update(' : -> length has changed!')

    def register(self, parameters, obs):
        for p in parameters:
            self.observers[p].add(obs)

    def unregister(self, obs):
        for parameter, _ in self.observers.items():
            set = self.observers[parameter]
            set.discard(obs)


class Observer:
    def __init__(self, name):
        self.name = name


    def update(self, msg):
        print(self.name + msg)


if __name__ == '__main__':

    # Use exactly this 'MAIN'
    # This code must run correctly, producing the output in the comments
    r1 = Rectangle(10, 20, ['length', 'width'])

    # CODE OMITTED --- COMPLETE
    # obs_1 is interested in a change of the length,
    obs_1 = Observer('obs_1')
    r1.register(['length'], obs_1)
    # obs_2 in a change of the width,
    obs_2 = Observer('obs_2')
    r1.register(['width'], obs_2)
    # obs_3 in a change of both.
    obs_3 = Observer('obs_3')
    r1.register(['length', 'width'], obs_3)


    print('\n set length = 15')
    r1.length = 15
    print('r1:', r1.length, r1.width)
    # 15, 20
    print('\n set width = 25')
    r1.width = 25
    print('r1:', r1.length, r1.width)
    # 15, 25
    print('\n\n obs 1 and obs_3 are no longer interested')

    # CODE OMITTED --- COMPLETE
    r1.unregister(obs_1)
    r1.unregister(obs_3)

    print('\n set length = 45')
    r1.length = 45
    print('r1:', r1.length, r1.width)
    # 45, 25
    print('\n set width = 55')
    r1.width = 55
    print('r1:', r1.length, r1.width)
    # 45, 55


    """
    set length = 15
    obs_1 : -> length has changed!
    obs_3 : -> length has changed!
    r1: 15 20
    set width = 25
    obs_3 : -> width has changed!
    obs_2 : -> width has changed!
    r1: 15 25
    obs 1 and obs_3 are no longer interested
    set length = 45
    r1: 45 25
    set width = 55
    obs_2 : -> width has changed!
    r1: 45 55
    """