from abc import ABC, abstractmethod


class Shape(ABC):

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, shape):
        self._shape = shape

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def draw_on_d1(self):
        pass

    @abstractmethod
    def draw_on_d2(self):
        pass

class Rectangle(Shape):
    def __init__(self, shape):
        self.shape = shape


    def draw(self):
        return 'draw the rectangle  ' + self._shape


    def draw_on_d1(self):
        return 'draw the rectangle  ' + self._shape


    def draw_on_d2(self):
        return 'draw the rectangle  ' + self._shape


class Circle(Shape):
    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        pass

    def draw_on_d1(self):
        return 'draw the circle  ' + self._shape


    def draw_on_d2(self):
        return 'draw the circle  ' + self._shape


class Display(ABC):
    def __init__(self, display):
        self.display = display

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, display):
        self._display = display

    @abstractmethod
    def draw(self, shape):
        pass


class Display1(Display):
    def __init__(self, display):
        super().__init__(display)

    def draw(self, shape):
        print(shape.draw_on_d1() + 'into the display of type 1 : ' + self._display)


class Display2(Display):
    def __init__(self, display):
        super().__init__(display)

    def draw(self, shape):
       print(shape.draw_on_d2() + 'into the display of type 1 : ' + self._display)
