class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value >= 0:
            self._width = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value >= 0:
            self._length = value


if __name__ == '__main__':
    # Use exactly this 'MAIN'
    # This code must run correctly, producing the output in the comments
    r1 = Rectangle(10, 20)
    print('r1:', r1.length, r1.width)
    # 10, 20
    r1.length = -5
    print('r1:', r1.length, r1.width)
    # 10, 20
    r1.length = 15
    print('r1:', r1.length, r1.width)
    # 15, 20
    r1.width = 25
    print('r1:', r1.length, r1.width)
    # 15, 25

    """
    The output is:
r1: 10 20
r1: 10 20
r1: 15 20
r1: 15 25
    """