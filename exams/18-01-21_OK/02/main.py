from piggy_bank import *
if __name__ == '__main__':
    # MAIN
    piggy_bank = PiggyBank(initial_amount=40, lower_threshold=20)
    obs1 = Observer('Observer 1')
    obs2 = Observer('Observer 2')
    piggy_bank.register(obs1)
    piggy_bank.register(obs2)
    piggy_bank.retrieve(15)
    piggy_bank.retrieve(15)
    piggy_bank.unregister(obs2)
    piggy_bank.retrieve(5)

    """
    message from Observer 2
    the amount is too low - it is only 10
    message from Observer 1
    the amount is too low - it is only 10
    message from Observer 1
    the amount is too low - it is only 5
    """