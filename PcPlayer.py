from Player import Player
from random import randint

class PcPlayer(Player):
    #constructor
    def __init__(self, name): #PCの番号
        super().__init__()
        self.name = name

    #手は乱数で決定
    def setHand(self):
        self.hand = randint(0, 2)
        self.handName = self.jyanken_t[self.hand]


