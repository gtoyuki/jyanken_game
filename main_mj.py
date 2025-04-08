#じゃんけんゲームの実行ファイル
from MyPlayer import MyPlayer
from PcPlayer import PcPlayer
from judgement_mj import Judgement

#プレイヤー(自身)
my = MyPlayer("私")
#PCの人数を設定
Pc_num = int(input("敵プレイヤー人数を設定してください>>"))

#敵プレイヤーごとに名前をあてて、PCリストに格納
Pc_list = list()
for i in range(Pc_num):
    pc = PcPlayer("PC" + str(i + 1))
    Pc_list.append( pc )

#審判員
j = Judgement()

#ゲーム開始
j.startGame()
must_push_enterkey = input("")

#ルール説明
j.showRule()

#勝者を格納するリストの作成
winList = list()

#勝者を格納するリストの作成　※プレイヤーより先に勝ち抜けを決めた者のみを格納する
win_before_List = list()

#プレイヤーが負け残った場合に必要なboolean型変数の宣言
isWin = True

#じゃんけんでプレイヤーが勝つまで続行
while True:

    #グー、チョキ、パーのじゃんけんリストを作成
    Block_handList = list()
    Scissors_handList = list()
    Paper_handList = list()

    #プレイヤーの手を決め、表示
    my.setHand()
    my.showHand()

    #プレイヤーの手をじゃんけんリストに格納
    if my.handName == "グー" :
        Block_handList.append(my)
    elif my.handName == "チョキ" :
        Scissors_handList.append(my)
    else :
        Paper_handList.append(my)

    # PCの手を決め、表示、さらにPCそれぞれの手をじゃんけんリストに格納
    for i in range(len(Pc_list)):
        Pc_list[i].setHand()
        print(f"{Pc_list[i].name}の手は{Pc_list[i].handName}です")
        if Pc_list[i].handName == "グー" :
            Block_handList.append(Pc_list[i])
        elif Pc_list[i].handName == "チョキ" :
            Scissors_handList.append(Pc_list[i])
        else :
            Paper_handList.append(Pc_list[i])
        
        

    #判定
    j.judge_majority(Block_handList, Scissors_handList, Paper_handList,winList, Pc_list)


    #プレイヤーが最後まで残ってしまったら終了
    if  "私" not in winList and (len(winList) == Pc_num):
        isWin = False
        break

    #プレイヤーが勝てばゲームの終了        
    if "私" in winList:
        print("あなたは勝ち抜けしました")
        break
    

    #プレイヤーが負けであればwin_beforeリストに格納
    for c in winList :
        if c not in win_before_List:
            win_before_List.append(c)



#何番抜けであるか、または負け残りか
if not isWin:
    print("あなたは負けました。")
else:
    rank = len(win_before_List) + 1
    print(f"あなたは{rank}番抜けです")

