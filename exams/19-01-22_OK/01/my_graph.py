from abc import ABC, abstractmethod


class Shapes(ABC):
    def __init__(self, shape):
        self.shape = shape

    @abstractmethod
    def draw(self):
        pass



class Rectangle(Shapes):
    def __init__(self, rectangle):
        super().__init__(rectangle)

    def draw(self):
        string = 'draw the rectangle  ' + self.shape
        return string



class Circle(Shapes):
    def __init__(self, circle):
        super().__init__(circle)

    def draw(self):
        return 'draw the circle  ' + self.shape


class Display(ABC):
    def __init__(self, display_type):
        self.display_type = display_type

    @abstractmethod
    def draw(self, shape):
        pass


class Display1(Display):
    def __init__(self, display):
        super().__init__(display)

    def draw(self, shape):
        print(shape.draw() + '  into the display of type 1 : ' + self.display_type)

class Display2(Display):
    def __init__(self, display):
        super().__init__(display)

    def draw(self, shape):
        print(shape.draw() + '  into the display of type 2: ' + self.display_type)