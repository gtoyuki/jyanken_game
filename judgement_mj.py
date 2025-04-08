class Judgement():
    #コンストラクタ
    def __init__(self):
        self.Judgement_t = ("引き分け", "あなたは負け", "あなたは勝ち")

    #開始宣言
    def startGame(self):
        print("じゃんけんゲームを始めます")

    #ルールの説明
    def showRule(self):
        print("0:グー, 1:チョキ, 2:パー")

    #判定
    def judge_majority(self, BList, SList, PList,winList,Pc_list):
        #全員同じ、またはグー・チョキ・パー全てある場合
        if (len(BList) != 0 and len(SList) != 0 and len(PList) != 0) or (len(BList) == 0 and len(SList) == 0) or (len(BList) == 0 and len(PList) == 0) or (len(SList) == 0 and len(PList) == 0) :
            print("あいこでしょ！")
        
        elif len(BList) == 0 :
            for k in range(len(SList)):
                winList.append(SList[k].name)
                for b in range(len(Pc_list)):
                    if SList[k].name == Pc_list[b].name:
                        Pc_list.remove(SList[k])
                        print(f"{SList[k].name}は抜けました")
                        break

        
        elif len(SList) == 0 :
            for k in range(len(PList)):
                winList.append(PList[k].name)
                for b in range(len(Pc_list)):
                    if PList[k].name == Pc_list[b].name:
                        Pc_list.remove(PList[k])
                        print(f"{PList[k].name}は抜けました")
                        break
            
        else :
            for k in range(len(BList)):
                winList.append(BList[k].name)
                for b in range(len(Pc_list)):
                    if BList[k].name == Pc_list[b].name:
                        Pc_list.remove(BList[k])
                        print(f"{BList[k].name}は抜けました")
                        break

        



        
