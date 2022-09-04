# COMPLETE THE CODE
from printer import Printer, PrinterTransTable

if __name__ == '__main__':
    ## COMPLETE THE CODE!
    print("\n\n")

    p = Printer()
    elements = ['a', 'e', 'h', 'i', 'o', 'u', 'w', 'h', 'a', 'e', 'i']

    for el in elements:
        p.process(el)


    print("\n\n")

    p = PrinterTransTable()

    for el in elements:
        p.process(el)

"""OUTPUT:


a
e
h
i
u
h
a
e
i

"""
