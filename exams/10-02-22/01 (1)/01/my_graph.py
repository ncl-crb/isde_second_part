from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def draw_on_display1(self, display):
        pass

    def draw_on_display2(self, display):
        pass


class Rectangle(Shape):
    def __init__(self, name):
        self.name = name

    def draw_on_display1(self, display):
        print('draw the rectangle  ' + self.name + '  into the display of type 1 : ' + display.name)

    def draw_on_display2(self, display):
        print('draw the rectangle  ' + self.name + '  into the display of type 2 : ' + display.name)


class Circle(Shape):
    def __init__(self, name):
        self.name = name

    def draw_on_display1(self, display):
        print('draw the circle  ' + self.name + '  into the display of type 1 : ' + display.name)

    def draw_on_display2(self, display):
        print('draw the circle  ' + self.name + '  into the display of type 2 : ' + display.name)


class Display(ABC):
    @abstractmethod
    def draw(self, shape):
        pass


class Display1(Display):
    def __init__(self, name):
        self.name = name

    def draw(self, shape):
        shape.draw_on_display1(self)


class Display2(Display):
    def __init__(self, name):
        self.name = name

    def draw(self, shape):
        shape.draw_on_display2(self)
