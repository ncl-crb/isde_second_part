from printer import Printer, Strategy1, Strategy2, Observer

# COMPLETE THE CODE

if __name__ == '__main__':
    ## COMPLETE THE CODE!
    print("\n\n")

    p = Printer(Strategy1())
    print(p.__dict__)
    elements = ['a', 'B', '3']


    print('MONDAY - FRIDAY\n')
    for el in elements:
        p.process_1(el)
        p.process_2(el)


    print("\n\n")
    print('SATURDAY - SUNDAY')
    p.processor = Strategy2()


    for el in elements:
        p.process_1(el)
        p.process_2(el)

"""OUTPUT:


MONDAY - FRIDAY
a
A
B
B
3
3



SATURDAY - SUNDAY
A
a  ASCII ->  97
B
B  ASCII ->  66
3  -> IT IS A NUMBER!
3  ASCII ->  51

"""