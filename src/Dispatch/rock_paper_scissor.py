from abc import ABC, abstractmethod


class RockPaperScissor(ABC):

    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def fight_against(self, w):
        pass


class Rock(RockPaperScissor):
    def __init__(self):
        self.wep = 'Rock'

    def fight_against(self, w):
        if isinstance(w, Paper):
            return 'PAPER'
        elif isinstance(w, Rock):
            return 'TIE'
        elif isinstance(w, Scissor):
            return 'ROCK'


class Paper(RockPaperScissor):
    def __init__(self):
        self.wep = 'Paper'

    def fight_against(self, w):
        if isinstance(w, Paper):
            return 'TIE'
        elif isinstance(w, Rock):
            return 'PAPER'
        elif isinstance(w, Scissor):
            return 'SCISSOR'


class Scissor(RockPaperScissor):
    def __init__(self):
        self.wep = 'Scissor'

    def fight_against(self, w):
        if isinstance(w, Paper):
            return 'SCISSOR'
        elif isinstance(w, Rock):
            return 'ROCK'
        elif isinstance(w, Scissor):
            return 'TIE'


if __name__ == '__main__':
    print('\n')
    list_of_weapons = [Scissor(), Paper(), Rock()]
    for w1 in list_of_weapons:
        for w2 in list_of_weapons:
            print(w1, " vs ", w2, ' --> ', w1.fight_against(w2))
