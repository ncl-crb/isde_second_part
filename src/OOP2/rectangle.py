class Rectangle:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, a):
        self._a = a

    @b.setter
    def b(self, b):
        self._b = b


class Square(Rectangle):

    def __init__(self, a=0, b=None):
        super().__init__(a, a)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, a):
        self._a = a
        self._b = a

    @b.setter
    def b(self, b):
        self._a = self._b
        self._b = self._b


def main():
    print('rectangle')
    r1 = Rectangle(1, 2)
    print(r1.a, r1.b)  # 1, 2
    r1.a = 10  # 10, 2
    print(r1.a, r1.b)

    print('square')

    s1 = Square(2)
    print(s1.a, s1.b)  # 2, 2
    s1.a = 10
    print(s1.a, s1.b)  # 10, 10
    s1.b = 20
    print(s1.a, s1.b)  # 20, 20


if __name__ == '__main__':
    main()
