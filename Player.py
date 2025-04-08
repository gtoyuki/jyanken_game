# from abc import ABC, abstractmethod

class Player():
    #constructor
    def __init__(self):
        self.hand = None  #0, 1, 2
        self.handName = "" #グー, チョキ, パー
        self.jyanken_t = ("グー", "チョキ", "パー")

    #手を決める
    # @abstractmethod
    def setHand(self):
        pass

    #手を表示する(str)
    def showHand(self):
        assert self.handName != "", "Error:setHandが実施されていません。"
        print(f"{self.name}の手は{self.handName}です")

    #手を表示する(int)
    def returnHand(self):
        return self.hand

