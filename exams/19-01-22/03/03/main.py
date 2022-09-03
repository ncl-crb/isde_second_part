from printer import Printer, Strategy1, Strategy2, Observer
# COMPLETE THE CODE IF NEEDED



if __name__ == '__main__':

    print("\n\n")


    p = Printer()
    elements = ['a', 'B', '3']

    # Observers s1 and s2 are interested in strategy changes
    # HERE I'M USING THE INITIAL STRATEGY - NO CHANGES
    s1 = Observer('s1')
    s2 = Observer('s2')

    p.register(s1)
    p.register(s2)

    print('MONDAY - FRIDAY')
    for el in elements:
        p.process_1(el)
        p.process_2(el)

    print("\n\n")
    print('SATURDAY - SUNDAY')
    # CHANGE STRATEGY - Observers must print
    # s1 ->  New Strategy!
    # s2 ->  New Strategy!

    p.processor = Strategy2()
    for el in elements:
        p.process_1(el)
        p.process_2(el)


    # Observer s1 is no more interested in strategy changes
    p.unregister(s1)


    print("\n\n")
    print('MONDAY - FRIDAY')

    # CHANGE STRATEGY - Observers must print

    # s2 ->  New Strategy!

    p.processor = Strategy1()

    for el in elements:
        p.process_1(el)
        p.process_2(el)


""" OUTPUT:


MONDAY - FRIDAY
a
A
B
B
3
3



SATURDAY - SUNDAY
s2 ->  New Strategy!
s1 ->  New Strategy!
A
a  ASCII ->  97
B
B  ASCII ->  66
3  -> IT IS A NUMBER!
3  ASCII ->  51



MONDAY - FRIDAY
s2 ->  New Strategy!
a
A
B
B
3
3



"""