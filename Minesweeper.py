import random
import sys

directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

count=0
win_count=0
lose_count=0

with open("result.txt", "w", encoding="utf-8") as f:
    def count_mines(board, row, col):
        rows, cols = len(board), len(board[0])
        count = 0
        for dr, dc in directions:
            r, c = row+dr, col+dc
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'M':
                count += 1
        return count

    def open_board(board, display, row, col):
        if display[row][col] != 'X':
            return
        count = count_mines(board, row, col)
        display[row][col] = str(count)
        if count == 0:
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(board) and 0 <= c < len(board[0]):
                    open_board(board, display, r, c)

    def get_kakureban(display):
        ban = []
        for r, row in enumerate(display):
            for c, cell in enumerate(row):
                if cell == 'X':
                    ban.append((r, c))
        return ban

    def random_move(display):
        ban = get_kakureban(display)
        if not ban:
            return "WIN"
        return random.choice(ban)

    def print_board(display):
        print("Player Board:",file=f)
        for row in display:
            print(' ', ' '.join(row),file=f)
        print(file=f)

    def win(display, board, mine_count):
        count = 0
        for row in display:
            for cell in row:
                if cell == 'F':
                    count += 1
        return count == mine_count #真ならTrue

    def flag(display):#1
        rows, cols = len(display), len(display[0]) #盤面の行数と列数を取得
        for r in range(rows):
            for c in range(cols): #全マスに対して
                if display[r][c].isdigit(): #そのマスが数字ならば
                    num = int(display[r][c]) #数字をintに変換
                    hidden = []
                    flag_count = 0
                    for dr, dc in directions: #8方向に対して
                        nr, nc = r+dr, c+dc 
                        if 0 <= nr < rows and 0 <= nc < cols: #はみ出しチェック
                            if display[nr][nc] == 'X':
                                hidden.append((nr, nc))#Xなら隠れマスに
                            elif display[nr][nc] == 'F':
                                flag_count += 1#Fならカウント
                                ####------1-2-----------
                    if hidden and num - flag_count == len(hidden):#隠れマス=残りの地雷数
                        for (nr, nc) in hidden:
                            display[nr][nc] = 'F' #隠れマスに旗を立てる
                            print(f"Mine found! Flagged {nr+1} {nc+1} from {r+1} {c+1}",file=f)

    def safe_move(display): #2
        safe_moves = [] #安全リスト
        rows, cols = len(display), len(display[0])
        for r in range(rows):
            for c in range(cols):
                if display[r][c].isdigit():
                    num = int(display[r][c])
                    hidden = []
                    flag_count = 0
                    for dr, dc in directions: #8方向の隠れますと波多野加アズをカウント
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if display[nr][nc] == 'X':
                                hidden.append((nr, nc))
                            elif display[nr][nc] == 'F':
                                flag_count += 1
                    if hidden and flag_count == num: #周囲の旗の数がそのマスの数字と一致する → 残りの隠れマスはすべて安全
                        for (nr, nc) in hidden:
                            if (nr, nc) not in safe_moves:#重複回避
                                safe_moves.append((nr, nc))#安全である現在のマスを安全にする
                                print(f"Safe square: {nr+1} {nc+1} from {r+1} {c+1}",file=f)
        return safe_moves

    def check_1_1_rule(display):
        rows, cols = len(display), len(display[0])
        safe_moves = []

        for r in range(2, rows - 2):
            for c in range(2, cols - 2):
                # 右より
                if (c==cols-1 and
                    display[r][c-1] == '1' and
                    display[r][c] == '1' and
                    display[r+1][c] == 'X' and
                    display[r+1][c-1] == 'X' and
                    display[r+1][c-2] == 'X'):
                    
                    if (r+1, c-2) not in safe_moves:
                        safe_moves.append((r+1, c-2))
                        print(f"Safe square found by 1-1 rule: {c+3} {r+2} from {c+1} {r+1}",file=f)
                        
                if (c==cols-1 and
                    display[r][c-1] == '1' and
                    display[r][c] == '1' and
                    display[r-1][c] == 'X' and
                    display[r-1][c-1] == 'X' and
                    display[r-1][c-2] == 'X'):
                    
                    if (r-1, c-2) not in safe_moves:
                        safe_moves.append((r-1, c-2))
                        print(f"Safe square found by 1-1 rule: {c+3} {r-2} from {c+1} {r+1}",file=f)

                if (r==rows-1 and
                    display[r-1][c] == '1' and
                    display[r][c] == '1' and
                    display[r][c-1] == 'X' and
                    display[r-1][c-1] == 'X' and
                    display[r-2][c-1] == 'X'):
                    
                    if (r-2, c-1) not in safe_moves:
                        safe_moves.append((r-2, c-1))
                        print(f"Safe square found by 1-1 rule: {c} {r-1} from {c+1} {r+1}",file=f)   
                        
                if (r==rows-1 and
                    display[r-1][c] == '1' and
                    display[r][c] == '1' and
                    display[r][c-1] == 'X' and
                    display[r-1][c+1] == 'X' and
                    display[r-2][c+1] == 'X'):
                    
                    if (r-2, c+1) not in safe_moves:
                        safe_moves.append((r-2, c+1))
                        print(f"Safe square found by 1-1 rule: {c+2} {r-1} from {c+1} {r+1}",file=f)           
                    
                if (r==0 and
                    display[r+1][c] == '1' and
                    display[r][c] == '1' and
                    display[r][c] == 'X' and
                    display[r+1][c-1] == 'X' and
                    display[r+2][c-1] == 'X'):
                    
                    if (r+2, c-1) not in safe_moves:
                        safe_moves.append((r+2, c-1))
                        print(f"Safe square found by 1-1 rule: {c} {r+3} from {c+1} {r+1}",file=f)
                        
                if (r==0 and
                    display[r+1][c] == '1' and
                    display[r][c] == '1' and
                    display[r][c] == 'X' and
                    display[r+1][c+1] == 'X' and
                    display[r+2][c+1] == 'X'):
                    
                    if (r+2, c+1) not in safe_moves:
                        safe_moves.append((r+2, c+1))
                        print(f"Safe square found by 1-1 rule: {c+2} {r+3} from {c+1} {r+1}",file=f)

                # 左より下方向X
                if (c==0 and
                    display[r][c+1] == '1' and
                    display[r][c] == '1' and
                    display[r+1][c] == 'X' and
                    display[r+1][c+1] == 'X' and
                    display[r+1][c+2] == 'X'):
                    if (r+1, c+2) not in safe_moves:
                        safe_moves.append((r+1, c+2))
                        print(f"Safe square found by 1-1 rule: {c+3} {r+2} from {c+1} {r+1}",file=f)
                        
                if (c==0 and
                    display[r][c+1] == '1' and
                    display[r][c] == '1' and
                    display[r-1][c] == 'X' and
                    display[r-1][c+1] == 'X' and
                    display[r-1][c+2] == 'X'):
                    if (r-1, c+2) not in safe_moves:
                        safe_moves.append((r-1, c+2))
                        print(f"Safe square found by 1-1 rule: {c+3} {r-2} from {c+1} {r+1}",file=f)

        return safe_moves    

    def generate_random_ms_board(x, y, mine):#引数：横の大きさx、縦の大きさy、地雷の数
        
        #x、yの大きさの盤（リスト）を作成する
        board = []
        for _ in range(y):#縦
            row = []
            for _ in range(x):#横
                row.append('0')
            board.append(row)#これで縦横y,xが0の盤面

        #地雷をランダムに配置する（random.sampleメソッドが便利）
        all_board = []
        for r in range(y):
            for c in range(x):
                all_board.append((r, c))
        mine_posi = random.sample(all_board, mine)#全部の盤の中からランダムで引数個選択
        for r, c in mine_posi:#選択した場所にM
            board[r][c] = 'M'

        # 地雷の隣接のマスの地雷の数情報を追加
        for r in range(y):
            for c in range(x):
                if board[r][c] == 'M':
                    continue
                count = 0
                for dr, dc in directions:#各方向に対して
                    nr, nc = r + dr, c + dc #現在地に対して+1の方向差分(隣接)
                    if 0 <= nr < y and 0 <= nc < x and board[nr][nc] == 'M':#はみ出し防止＆隣接がMなら
                        count += 1
                board[r][c] = str(count)#隣接するMの数を文字列として現在地に代入
        return board

    def print_generated_board(board):
        for row in board:
            print(' '.join(row),file=f)
            
    def save_board_to_txt(board, filename):
        with open(filename, 'w') as f:
            for row in board:
                f.write(' '.join(row) + '\n')

    #================================================================#

    def play_game():
        board = generate_random_ms_board(12, 9, 13)
        print_generated_board(board)
        save_board_to_txt(board, "board.txt")
        with open("board.txt") as ff:
            board = [line.split() for line in ff]

        rows, cols = len(board), len(board[0])
        display = [['X'] * cols for _ in range(rows)]
        total_mines = sum(cell == 'M' for row in board for cell in row)
        count=0

        while True:
            count+=1
            print_board(display)
            print(f"Number of mines: {total_mines}",file=f)

            flag(display)  # 旗を付ける
            safe = safe_move(display)  # 安全マス探索
            safe += check_1_1_rule(display)

            if safe:
                r, c = safe.pop()
                print(f"Playing safe square: {c+1} {r+1}",file=f)
            else:
                move = random_move(display)
                if move == "WIN":
                    print_board(display)
                    print("All safe squares opened! You win!",file=f)
                    print("Number of mines:", total_mines,file=f)
                    return True
                r, c = move
                print(f"random played: {c+1} {r+1}",file=f)
                

            if board[r][c] == 'M':
                display[r][c] = 'M'
                print_board(display)
                print("Number of mines: ", total_mines,file=f)
                print("You stepped on a mine. Gameover",file=f)
                print("You stepped on a mine. Gameover")
                return False  # 負けた

            else:
                open_board(board, display, r, c)

            if win(display, board, total_mines):
                print_board(display)
                print("Number of mines: ", total_mines,file=f)
                print("You found all the mines. Well done!",file=f)
                print("You found all the mines. Well done!")
                return True  # 勝った


    for _ in range(100):
        count += 1
        print(f"Board number {count}",file=f)
        print(f"Board number {count}")
        if play_game():
            win_count += 1
        else:
            lose_count += 1
        syouritu = win_count/count *100
        syouritu_round = round(syouritu,2)
        print(f"Solved {win_count} out of {count} boards ({syouritu_round} %)",file=f)
        print(f"Solved {win_count} out of {count} boards ({syouritu_round} %)")
