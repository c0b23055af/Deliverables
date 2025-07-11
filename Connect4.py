import random

lst = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "]
]

inf = 30000
WIN_SCORE = 1000
LOSE_SCORE = -1000
DRAW_SCORE = 0
testwin = 0
bestwin = 0
drawcount = 0
count_turn=0

def show_connect4_board(lst, file=None):
    print("-----------------------------", file=file)
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if j == 6:
                print("|", lst[i][j], "|", file=file)
                print("-----------------------------", file=file)
            else:
                print("|", lst[i][j], "", end="", file=file)
    print("  1   2   3   4   5   6   7", file=file)

def evaluate_board(lst,mark):
    score = 0
    directions = [(0,1),(1,0),(1,1),(1,-1)]
    for i in range(6):
        for j in range(7):
            current = lst[i][j]
            if current == " ":
                continue
            for dy, dx in directions:
                count = 1
                blocked = [False,False] 
                for k in range(1,4):
                    ni = i + dy*k
                    nj = j + dx*k
                    if 0 <= ni < 6 and 0 <= nj < 7 and lst[ni][nj] == current:
                        count += 1
                    else:
                        break
                    
                # 前のマス（連結の前に空白があるかチェック）
                prev_i = i - dy
                prev_j = j - dx
                if 0 <= prev_i < 6 and 0 <= prev_j < 7:
                    if lst[prev_i][prev_j] != " ":
                        blocked[0] = True
                else:
                    blocked[0] = True

                # 次のマス（連結の後に空白があるかチェック）
                next_i = i + dy * count
                next_j = j + dx * count
                if 0 <= next_i < 6 and 0 <= next_j < 7:
                    if lst[next_i][next_j] != " ":
                        blocked[1] = True
                else:
                    blocked[1] = True

                if blocked[0] and blocked[1]:
                    continue  # 両端が塞がれている場合はスコアに加えない
                
                if mark=="1": #bestAI
                    if count == 2:
                        score += 60 if current == "1" else -25
                    elif count == 3:
                        score += 45 if current == "1" else -50
                        
                if mark=="2": #testAI
                    if count == 2:
                        score += 10 if current == "2" else -10
                    elif count == 3:
                        score += 20 if current == "2" else -20
    return score

def decide_minmax_ai_move(lst, mark, current_player, hukasa=0):
    if hukasa >= 3:
        eval_score = evaluate_board(lst,current_player)
        # 評価スコアは最大化プレイヤー（mark）の視点から計算されるべき
        # current_playerが相手の場合、スコアを反転させる必要がある
        if current_player != mark:
             eval_score *= -1
        return eval_score, None

    if current_player == mark:
        best_score = -inf
    else:
        best_score = inf

    best_move = None

    # 盤面満杯チェック
    full = True
    for row in lst:
        for cell in row:
            if cell == " ":
                full = False
                break
        if not full:
            break
    if full:
        return DRAW_SCORE, None

    for col in range(7):
        # その列の一番下の空きマスを探す
        row_to_place = None
        for row in reversed(range(6)):
            if lst[row][col] == " ":
                row_to_place = row
                break
        if row_to_place is None:
            continue  # 列が満杯

        lst[row_to_place][col] = current_player # 駒を仮置き

        if chck_winner(lst): # 勝利判定
            # AIが勝利手を見つけた場合、駒を元に戻さずに確定させる
            if hukasa == 0 and current_player == mark: # メインループからの呼び出しでAIの勝ち手の場合
                
                # 何もせず、この駒が置かれたままにする
                return WIN_SCORE - hukasa, (row_to_place, col)
            else: # 探索中の勝ち手、または相手の勝ち手
                lst[row_to_place][col] = " " # 駒を元に戻す（バックトラック）
                if current_player == mark: # AIが勝つ場合
                    return WIN_SCORE - hukasa, (row_to_place, col)
                else: # 相手が勝つ場合
                    return LOSE_SCORE + hukasa, (row_to_place, col)

        # 次のプレイヤーに交代
        next_player = "2" if current_player == "1" else "1"
        score, move = decide_minmax_ai_move(lst, mark, next_player, hukasa + 1)
        lst[row_to_place][col] = " " # 駒を元に戻す（バックトラック）

        if current_player == mark:
            if score > best_score:
                best_score = score
                best_move = (row_to_place, col)
            elif score == best_score and hukasa == 0:
                if random.choice([True, False]):
                    best_move = (row_to_place, col)
        else:
            if score < best_score:
                best_score = score
                best_move = (row_to_place, col)
            if score == best_score and hukasa == 0:
                if random.choice([True, False]):
                    best_move = (row_to_place, col)
                

    # 深さ0なら最善手を盤面に置く
    if hukasa == 0 and best_move is not None:
        i, j = best_move
        lst[i][j] = mark # AIの選択した手をボードに適用

    return best_score, best_move

def chck_winner(lst):
    # 横チェック
    for i in range(6):
        for j in range(4):
            if lst[i][j] != " " and lst[i][j] == lst[i][j+1] == lst[i][j+2] == lst[i][j+3]:
                return True
    # 縦チェック
    for i in range(3):
        for j in range(7):
            if lst[i][j] != " " and lst[i][j] == lst[i+1][j] == lst[i+2][j] == lst[i+3][j]:
                return True
    # 斜め（右下方向）
    for i in range(3):
        for j in range(4):
            if lst[i][j] != " " and lst[i][j] == lst[i+1][j+1] == lst[i+2][j+2] == lst[i+3][j+3]:
                return True
    # 斜め（左下方向）
    for i in range(3):
        for j in range(3,7):
            if lst[i][j] != " " and lst[i][j] == lst[i+1][j-1] == lst[i+2][j-2] == lst[i+3][j-3]:
                return True

    return False

with open("log.txt", "w", encoding="utf-8") as f:
    for i in range(100):
        count_turn = 0
        print(f"Starting game number {i+1}...")
        print(f"Starting game number {i+1}...", file=f)
        print("Best AI - Test AI")
        print("Best AI - Test AI", file=f)
        lst = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "]
        ]

        show_connect4_board(lst, f)

        while True:
            score, move = decide_minmax_ai_move(lst, "1", "1", 0)
            count_turn += 1
            print("First player to move",file=f)
            print(f"Move{count_turn}: {move[1]+1}({score})", file=f)
            show_connect4_board(lst, f)
            if chck_winner(lst):
                print("Gameover: Best player wins", file=f)
                print("Gameover: Best player wins")
                bestwin += 1
                print(f"Current score: Best AI - Test AI {bestwin} - {testwin} (Draws: {drawcount})",file = f)
                print(f"Current score: Best AI - Test AI {bestwin} - {testwin} (Draws: {drawcount})")
                break

            score, move = decide_minmax_ai_move(lst, "2", "2", 0)
            count_turn += 1
            print("Second player to move",file=f)
            print(f"Move{count_turn}: {move[1]+1}({score})", file=f)
            show_connect4_board(lst, f)
            if chck_winner(lst):
                print("Gameover: Test AI wins", file=f)
                print("Gameover: Test AI wins")
                testwin += 1
                print(f"Current score: Best AI - Test AI {bestwin} - {testwin} (Draws: {drawcount})",file = f)
                print(f"Current score: Best AI - Test AI {bestwin} - {testwin} (Draws: {drawcount})")
                break

            one_lst = sum(lst, [])
            if " " not in one_lst:
                print("Draw", file=f)
                drawcount += 1
                print(f"Current score: Best AI - Test AI {bestwin} - {testwin} (Draws: {drawcount})",file = f)
                print(f"Current score: Best AI - Test AI {bestwin} - {testwin} (Draws: {drawcount})")
                break
