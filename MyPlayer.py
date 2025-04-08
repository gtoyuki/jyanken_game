import sys
from Player import Player

class MyPlayer(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def setHand(self):
        self.hand = input("プレイヤーの手を整数で入力して下さい>>")
        try:
            self.hand = int (self.hand)
            self.handName = self.jyanken_t[self.hand]
        except ValueError:
            print("数字ではない文字が入力されました")
            sys.exit()
        except IndexError:
            print("0, 1, 2以外の入力がされました")
            sys.exit()
