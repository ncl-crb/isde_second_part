from abc import ABC, abstractmethod


class RockPaperScissor(ABC):

    def __str__(self):
        return self.__class__.__name__

    def fight_against(self, w):
        return look_up_table[(type(self), type(w))]


class Rock(RockPaperScissor):
    def __init__(self):
        self.wep = 'Rock'


class Paper(RockPaperScissor):
    def __init__(self):
        self.wep = 'Paper'


class Scissor(RockPaperScissor):
    def __init__(self):
        self.wep = 'Scissor'


look_up_table = {
    (Scissor, Scissor): 'TIE',
    (Scissor, Rock): 'ROCK',
    (Scissor, Paper): 'SCISSOR',
    (Rock, Rock): 'TIE',
    (Rock, Paper): 'PAPER',
    (Rock, Scissor): 'SCISSOR',
    (Paper, Paper): 'TIE',
    (Paper, Scissor): 'SCISSOR',
    (Paper, Rock): 'PAPER'
}

if __name__ == '__main__':
    print('\n')
    list_of_weapons = [Scissor(), Paper(), Rock()]
    for w1 in list_of_weapons:
        for w2 in list_of_weapons:
            print(w1, " vs ", w2, ' --> ', w1.fight_against(w2))
