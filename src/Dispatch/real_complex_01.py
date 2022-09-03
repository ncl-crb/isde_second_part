from abc import ABC, abstractmethod


class MathEntity(ABC):

    # first dispatch
    @abstractmethod
    def sum_with(self, a):
        pass

    # second dispatch
    @abstractmethod
    def _sum_with_R(self, a):
        pass

    @abstractmethod
    def _sum_with_C(self, a, b):
        pass


class R(MathEntity):
    def __init__(self, a):
        self.a = a

    def sum_with(self, n):
        return n._sum_with_R(self.a)

    def _sum_with_R(self, a):
        return self.a + a

    def _sum_with_C(self, a, b):
        return self.a + a, b


class C(MathEntity):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum_with(self, n):
        return n._sum_with_C(self.a, self.b)

    def _sum_with_R(self, a):
        return self.a + a, self.b

    def _sum_with_C(self, a, b):
        return self.a + a, self.b + b


def main():
    real1 = R(2)
    real2 = R(3)
    comp1 = C(1, 1)
    comp2 = C(4, 4)

    print(real1.sum_with(real2))  # 5
    print(real1.sum_with(comp1))  # 3, 1
    print(comp1.sum_with(real1))  # 3, 1
    print(comp1.sum_with(comp2))  # 5, 5


if __name__ == '__main__':
    main()
