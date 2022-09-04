# COMPLETE THE CODE...
from my_graph import Rectangle,Circle,Display1, Display2


if __name__ == '__main__':
    print("\n\n")

    r = Rectangle('**blue rectangle**')
    c = Circle('**big red circle**')
    d1 = Display1('800x600x8')
    d2_a = Display2('1600x1600x16 - A')
    d2_b = Display2('1600x1600x16 - B')

    d1.draw(r)
    d1.draw(c)
    d2_a.draw(r)
    d2_a.draw(c)
    d2_b.draw(r)
    d2_b.draw(c)

    print("\n\n")

    """ OUTPUT:
    
draw the rectangle  **blue rectangle**  into the display of type 1 : 800x600x8
draw the circle  **big red circle**  into the display of type 1 : 800x600x8
draw the rectangle  **blue rectangle**  into the display of type 2 : 1600x1600x16 - A
draw the circle  **big red circle**  into the display of type 2 : 1600x1600x16 - A
draw the rectangle  **blue rectangle**  into the display of type 2 : 1600x1600x16 - B
draw the circle  **big red circle**  into the display of type 2 : 1600x1600x16 - B

    """
