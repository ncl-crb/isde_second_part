from abc import ABC, abstractmethod


class Character(ABC):

    def __init__(self, energy=None):
        self.energy = energy

    def eat(self, x):
        self.energy += x

    @abstractmethod
    def attack(self, other):
        pass

    @abstractmethod
    def attack_gnome(self, other):
        pass

    @abstractmethod
    def attack_orc(self, other):
        pass


class Gnome(Character):
    def __init__(self, energy=100):
        super().__init__(energy)

    def attack(self, other):
        other.attack_gnome(self)

    def attack_gnome(self, other):
        self.energy -= 7
        other.energy -= 7

    def attack_orc(self, other):
        self.energy -= 5
        other.energy -= 1

class Orc(Character):
    def __init__(self, energy=200):
        super().__init__(energy)

    def attack(self, other):
        other.attack_orc(self)

    def attack_gnome(self, other):
        self.energy -= 3
        other.energy -= 2

    def attack_orc(self, other):
        self.energy -= 10
        other.energy -= 10