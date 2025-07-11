import random

lst=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
count=0
count_num=0
win_x = 0
win_o = 0
draw = 0
inf = 30000
WIN_SCORE = 20000
LOSE_SCORE = -20000
DRAW_SCORE = 0

with open("TicTacToeSelfPlayMinMaxData.txt", "w", encoding="utf-8") as f:

    def show_tictactoe_board(lst):
        print("-------------",file=f)
        for i in range(len(lst)):
            for j in range(len(lst)):
                if j==2:
                    print("|",lst[i][j],"|",file=f)
                    print("-------------",file=f)
                else:
                    print("|",lst[i][j],"",end="",file=f)
            

    def get_next_move(lst,mark,count):
        if mark=="x":
            while True:
                tgt_i=random.randint(0,2)
                tgt_j=random.randint(0,2)
                if lst[tgt_i][tgt_j]=="x" or lst[tgt_i][tgt_j]=="o":
                    continue
                else:
                    lst[tgt_i][tgt_j]="x"
                    print(f"X to move{count}:Random AI played {tgt_i} {tgt_j}",file=f)
                    show_tictactoe_board(lst)
                    break

    def RuleAI(lst,mark,count):
        if mark=="o":
            print("O to move",file=f)
        #横
            if lst[0][0] == "o" and lst[0][1] == "o" and lst[0][2] == " ":
                tgt_i=0
                tgt_j=2
                lst[0][2] = "o"
            elif lst[0][0] == "o" and lst[0][2] == "o" and lst[0][1] == " ":
                tgt_i=0
                tgt_j=1
                lst[0][1] = "o"
            elif lst[0][1] == "o" and lst[0][2] == "o" and lst[0][0] == " ":
                tgt_i=0
                tgt_j=0
                lst[0][0] = "o"
            elif lst[1][0] == "o" and lst[1][1] == "o" and lst[1][2] == " ":
                tgt_i=1
                tgt_j=2
                lst[1][2] = "o"
            elif lst[1][0] == "o" and lst[1][2] == "o" and lst[1][1] == " ":
                tgt_i=1
                tgt_j=1
                lst[1][1] = "o"
            elif lst[1][1] == "o" and lst[1][2] == "o" and lst[1][0] == " ":
                tgt_i=1
                tgt_j=0
                lst[1][0] = "o"
            elif lst[2][0] == "o" and lst[2][1] == "o" and lst[2][2] == " ":
                tgt_i=2
                tgt_j=2
                lst[2][2] = "o"
            elif lst[2][0] == "o" and lst[2][2] == "o" and lst[2][1] == " ":
                tgt_i=2
                tgt_j=1
                lst[2][1] = "o"
            elif lst[2][1] == "o" and lst[2][2] == "o" and lst[2][0] == " ":
                tgt_i=2
                tgt_j=0
                lst[2][0] = "o"

            # 縦
            elif lst[0][0] == "o" and lst[1][0] == "o" and lst[2][0] == " ":
                tgt_i=2
                tgt_j=0
                lst[2][0] = "o"
            elif lst[0][0] == "o" and lst[2][0] == "o" and lst[1][0] == " ":
                tgt_i=1
                tgt_j=0
                lst[1][0] = "o"
            elif lst[1][0] == "o" and lst[2][0] == "o" and lst[0][0] == " ":
                tgt_i=0
                tgt_j=0
                lst[0][0] = "o"
            elif lst[0][1] == "o" and lst[1][1] == "o" and lst[2][1] == " ":
                tgt_i=2
                tgt_j=1
                lst[2][1] = "o"
            elif lst[0][1] == "o" and lst[2][1] == "o" and lst[1][1] == " ":
                tgt_i=1
                tgt_j=1
                lst[1][1] = "o"
            elif lst[1][1] == "o" and lst[2][1] == "o" and lst[0][1] == " ":
                tgt_i=0
                tgt_j=1
                lst[0][1] = "o"
            elif lst[0][2] == "o" and lst[1][2] == "o" and lst[2][2] == " ":
                tgt_i=2
                tgt_j=2
                lst[2][2] = "o"
            elif lst[0][2] == "o" and lst[2][2] == "o" and lst[1][2] == " ":
                tgt_i=1
                tgt_j=2
                lst[1][2] = "o"
            elif lst[1][2] == "o" and lst[2][2] == "o" and lst[0][2] == " ":
                tgt_i=0
                tgt_j=2
                lst[0][2] = "o"
            # 斜め
            elif lst[0][0] == "o" and lst[1][1] == "o" and lst[2][2] == " ":
                tgt_i=2
                tgt_j=2
                lst[2][2] = "o"
            elif lst[0][0] == "o" and lst[2][2] == "o" and lst[1][1] == " ":
                tgt_i=1
                tgt_j=1
                lst[1][1] = "o"
            elif lst[1][1] == "o" and lst[2][2] == "o" and lst[0][0] == " ":
                tgt_i=0
                tgt_j=0
                lst[0][0] = "o"
            elif lst[0][2] == "o" and lst[1][1] == "o" and lst[2][0] == " ":
                tgt_i=2
                tgt_j=0
                lst[2][0] = "o"
            elif lst[0][2] == "o" and lst[2][0] == "o" and lst[1][1] == " ":
                tgt_i=1
                tgt_j=1
                lst[1][1] = "o"
            elif lst[1][1] == "o" and lst[2][0] == "o" and lst[0][2] == " ":
                tgt_i=0
                tgt_j=2
                lst[0][2] = "o"
            
            else:
                if lst[0][0] == "x" and lst[0][1] == "x" and lst[0][2] == " ":
                    tgt_i=0
                    tgt_j=2
                    lst[0][2] = "o"
                elif lst[0][0] == "x" and lst[0][2] == "x" and lst[0][1] == " ":
                    tgt_i=0
                    tgt_j=1
                    lst[0][1] = "o"
                elif lst[0][1] == "x" and lst[0][2] == "x" and lst[0][0] == " ":
                    tgt_i=0
                    tgt_j=0
                    lst[0][0] = "o"
                elif lst[1][0] == "x" and lst[1][1] == "x" and lst[1][2] == " ":
                    tgt_i=1
                    tgt_j=2
                    lst[1][2] = "o"
                elif lst[1][0] == "x" and lst[1][2] == "x" and lst[1][1] == " ":
                    tgt_i=1
                    tgt_j=1
                    lst[1][1] = "o"
                elif lst[1][1] == "x" and lst[1][2] == "x" and lst[1][0] == " ":
                    tgt_i=1
                    tgt_j=0
                    lst[1][0] = "o"
                elif lst[2][0] == "x" and lst[2][1] == "x" and lst[2][2] == " ":
                    tgt_i=2
                    tgt_j=2
                    lst[2][2] = "o"
                elif lst[2][0] == "x" and lst[2][2] == "x" and lst[2][1] == " ":
                    tgt_i=2
                    tgt_j=1
                    lst[2][1] = "o"
                elif lst[2][1] == "x" and lst[2][2] == "x" and lst[2][0] == " ":
                    tgt_i=2
                    tgt_j=0
                    lst[2][0] = "o"

                # 縦
                elif lst[0][0] == "x" and lst[1][0] == "x" and lst[2][0] == " ":
                    tgt_i=2
                    tgt_j=0
                    lst[2][0] = "o"
                elif lst[0][0] == "x" and lst[2][0] == "x" and lst[1][0] == " ":
                    tgt_i=1
                    tgt_j=0
                    lst[1][0] = "o"
                elif lst[1][0] == "x" and lst[2][0] == "x" and lst[0][0] == " ":
                    tgt_i=0
                    tgt_j=0
                    lst[0][0] = "o"
                elif lst[0][1] == "x" and lst[1][1] == "x" and lst[2][1] == " ":
                    tgt_i=2
                    tgt_j=1
                    lst[2][1] = "o"
                elif lst[0][1] == "x" and lst[2][1] == "x" and lst[1][1] == " ":
                    tgt_i=1
                    tgt_j=1
                    lst[1][1] = "o"
                elif lst[1][1] == "x" and lst[2][1] == "x" and lst[0][1] == " ":
                    tgt_i=0
                    tgt_j=1
                    lst[0][1] = "o"
                elif lst[0][2] == "x" and lst[1][2] == "x" and lst[2][2] == " ":
                    tgt_i=2
                    tgt_j=2
                    lst[2][2] = "o"
                elif lst[0][2] == "x" and lst[2][2] == "x" and lst[1][2] == " ":
                    tgt_i=1
                    tgt_j=2
                    lst[1][2] = "o"
                elif lst[1][2] == "x" and lst[2][2] == "x" and lst[0][2] == " ":
                    tgt_i=0
                    tgt_j=2
                    lst[0][2] = "o"
                # 斜め
                elif lst[0][0] == "x" and lst[1][1] == "x" and lst[2][2] == " ":
                    tgt_i=2
                    tgt_j=2
                    lst[2][2] = "o"
                elif lst[0][0] == "x" and lst[2][2] == "x" and lst[1][1] == " ":
                    tgt_i=1
                    tgt_j=1
                    lst[1][1] = "o"
                elif lst[1][1] == "x" and lst[2][2] == "x" and lst[0][0] == " ":
                    tgt_i=0
                    tgt_j=0
                    lst[0][0] = "o"
                elif lst[0][2] == "x" and lst[1][1] == "x" and lst[2][0] == " ":
                    tgt_i=2
                    tgt_j=0
                    lst[2][0] = "o"
                elif lst[0][2] == "x" and lst[2][0] == "x" and lst[1][1] == " ":
                    tgt_i=1
                    tgt_j=1
                    lst[1][1] = "o"
                elif lst[1][1] == "x" and lst[2][0] == "x" and lst[0][2] == " ":
                    tgt_i=0
                    tgt_j=2
                    lst[0][2] = "o"
                else:
                    if lst[1][1]==" ":
                        tgt_i=1
                        tgt_j=1
                        lst[1][1]="o"
                    else:
                        while True:
                            tgt_i=random.randint(0,2)
                            tgt_j=random.randint(0,2)
                            if lst[tgt_i][tgt_j]=="x" or lst[tgt_i][tgt_j]=="o":
                                continue
                            else:
                                lst[tgt_i][tgt_j]="o"
                                print(f"{count}:Random AI played {tgt_i} {tgt_j}",file=f)
                                show_tictactoe_board(lst)
                                break
            print(f"{count}:Rule-based AI played {tgt_i} {tgt_j}",file=f)
            show_tictactoe_board(lst)
                    

    def chck_winner(lst):
        if lst[0][0] =="x" and lst[0][1]=="x" and lst[0][2] =="x" or lst[1][0]=="x" and lst[1][1]=="x" and lst[1][2] =="x" or lst[2][0]=="x" and lst[2][1]=="x" and lst[2][2] =="x" or lst[0][0]=="x" and lst[1][0]=="x" and lst[2][0] =="x" or lst[0][1]=="x" and lst[1][1]=="x" and lst[2][1] =="x" or lst[0][2]=="x" and lst[1][2]=="x" and lst[2][2] =="x" or lst[0][0]=="x" and lst[1][1]=="x" and lst[2][2] =="x" or lst[0][2]=="x" and lst[1][1]=="x" and lst[2][0] =="x":
            return True
        elif lst[0][0]=="o" and lst[0][1]=="o" and lst[0][2] =="o" or lst[1][0]=="o" and lst[1][1]=="o" and lst[1][2] =="o" or lst[2][0]=="o" and lst[2][1]=="o" and lst[2][2] =="o" or lst[0][0]=="o" and lst[1][0]=="o" and lst[2][0] =="o" or lst[0][1]=="o" and lst[1][1]=="o" and lst[2][1] =="o" or lst[0][2]=="o" and lst[1][2]=="o" and lst[2][2] =="o" or lst[0][0]=="o" and lst[1][1]=="o" and lst[2][2] =="o" or lst[0][2]=="o" and lst[1][1]=="o" and lst[2][0] =="o":
            return True
        else:
            return False

    def decide_minmax_ai_move(lst, mark, current_player, hukasa=0):
        if current_player == mark:
            best_score = -inf  # MAXプレイヤー
        else:
            best_score = inf  # MINプレイヤー

        best_move = None

        # 空きマスがないから0を返す
        full=True
        for row in lst:
            for cell in row:
                if cell == " ":
                    full = False
                    break
            if full == False:
                break
        if full==True:
            return DRAW_SCORE, None
                

        for i in range(3):
            for j in range(3):
                if lst[i][j] == " ":
                    lst[i][j] = current_player  # 1

                    if chck_winner(lst) == True:        # 2
                        lst[i][j] = " "         # 5
                        if current_player == mark:# 3 
                            return WIN_SCORE , (i, j)
                        else:
                            return LOSE_SCORE , (i, j)

                    # 4
                    
                    if current_player == "x":
                        next_player = "o"
                    else:
                        next_player = "x"

                    score, move = decide_minmax_ai_move(lst, mark, next_player, hukasa + 1)

                    lst[i][j] = " "  # 5

                    # 6
                    if current_player == mark:
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)
                    else:
                        if score < best_score:
                            best_score = score
                            best_move = (i, j)

        # 深さ0のとき手を置く
        if hukasa == 0:
            i, j = best_move
            score = best_score
            lst[i][j] = mark

        return best_score, best_move
            
    for o in range(100):
        count_num+=1
        print(f"Starting game number {count_num}...",file=f)
        print(f"Starting game number {count_num}...")
        lst=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
        ]
        count=0
        show_tictactoe_board(lst)
        while True:
            count+=1
            score,move = decide_minmax_ai_move(lst,"o","o",0)
            # print(lst[move])
            lst[move[0]][move[1]] = "o"
            print("O to move",file=f)
            print(f"Evaluation: {score}",file=f)
            print(f"{count}:MinMax AI played {move[0]} {move[1]}",file=f)
            show_tictactoe_board(lst)
            judge=chck_winner(lst)
            if judge == True:
                print("Gameover:MInMax AI wins",file=f)
                print("Gameover:MinMax AI wins")
                win_o+=1
                print(f"Current score: Minmax AI - Random AI {win_o} - {win_x} (Draws: {draw})",file=f)
                print(f"Current score: Minmax AI - Random AI {win_o} - {win_x} (Draws: {draw})")
                break
            one_lst = sum(lst,[]) #1次元リストにする
            if " " not in one_lst:
                print("Gameover:Draw",file=f)
                print("Gameover:Draw")
                draw += 1
                print(f"Current score: MinMax AI - Random AI {win_o} - {win_x} (Draws: {draw})",file=f)
                print(f"Current score: MinMax AI - Random AI {win_o} - {win_x} (Draws: {draw})")
                break
            count+=1
            get_next_move(lst,"x",count)
            judge=chck_winner(lst)
            if judge == True:
                print("Gameover:Random AI wins",file=f)
                print("Gameover:Random AI wins")
                win_x+=1
                print(f"Current score: MinMax AI - Random AI {win_o} - {win_x} (Draws: {draw})",file=f)
                print(f"Current score: MinMax AI - Random AI {win_o} - {win_x} (Draws: {draw})")
                break
            