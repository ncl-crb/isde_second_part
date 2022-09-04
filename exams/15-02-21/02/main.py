from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def attack(self, attacker, victim):
        pass


class StrategyDay(Strategy):
    def attack(self, attacker, victim):
        new_att = attacker * 0.8
        new_vic  =victim * 0.7
        return new_att, new_vic



class StrategyNight(Strategy):
    def attack(self, attacker, victim):
        new_att = attacker * 0.9
        new_vic = victim * 0.6
        return new_att, new_vic


class Character(ABC):
    def __init__(self, energy=100, strategy=StrategyDay()):
        self.energy = energy
        self.strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, value):
        self._strategy = value
    def eat(self, x):
        self.energy += x

    def attack(self, victim):
        self.energy, victim.energy = self.strategy.attack(self.energy, victim.energy)

class Gnome(Character):
    def __init__(self, energy=100):
        super().__init__(energy)


class Orc(Character):
    def __init__(self, energy=200):
        super().__init__(energy)


if __name__ == '__main__':
    # Use exactly this 'MAIN'
    # This code must run correctly, producing the showed output.
    # Write your code into a 'main_1.py' file
    orc1 = Orc()
    gnome1 = Gnome()
    print('orc1 energy:', orc1.energy)
    print('gnome1 energy:', gnome1.energy)
    print('gnome1 eats 10')
    gnome1.eat(10)
    print('gnome1 energy:', gnome1.energy)

    """
    orc1 energy: 200
    gnome1 energy: 100
    gnome1 eats 10
    gnome1 energy: 110
    """

    # Use this 'MAIN'
    # complete where necessary, but without deleting or altering the instructions
    #alread present
    # This code must run correctly, producing the showed output.
    # Write your code into a 'main_2.py' file
    orc1 = Orc()
    gnome1 = Gnome()
    ## ATTACK - DAY
    print('\n \n')
    print('\nATTACK - DAY.')
    print('orc1 energy:', orc1.energy, '- gnome1 energy:', gnome1.energy)
    print('orc1 attacks gnome1!')
    orc1.attack(gnome1)
    print('orc1 energy:', orc1.energy, '- gnome1 energy:', gnome1.energy)
    ## ATTACK - NIGHT
    orc1.strategy = StrategyNight()

    print('\n \n')
    print('\nATTACK - NIGHT.')
    print('orc1 energy:', orc1.energy, '- gnome1 energy:', gnome1.energy)
    print('orc1 attacks gnome1!')
    orc1.attack(gnome1)
    print('orc1 energy:', orc1.energy, '- gnome1 energy:', gnome1.energy)

    """
    The output is:
    ATTACK - DAY.
    orc1 energy: 200 - gnome1 energy: 100
    orc1 attacks gnome1!
    orc1 energy: 160.0 - gnome1 energy: 70.0
    ATTACK - NIGHT.
    orc1 energy: 160.0 - gnome1 energy: 70.0
    orc1 attacks gnome1!
    orc1 energy: 144.0 - gnome1 energy: 42.0
    """