import math

def print_board(b):
    for i in range(3):
        print(' | '.join(b[i*3:(i+1)*3]))
        if i < 2: print('---------')

def check_win(b, p):
    
    wins = ([0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6])
    return any(all(b[i] == p for i in line) for line in wins)

def is_full(b):
    return ' ' not in b

def score_board(b, ai, human):
    if check_win(b, ai): return 10
    if check_win(b, human): return -10
    return 0


def minimax(b, is_max, ai, human):
    s = score_board(b, ai, human)
    if s != 0 or is_full(b): return s

    
    best_score = -math.inf if is_max else math.inf
    optimize = max if is_max else min

    
    for i in range(9):
        if b[i] == ' ':
            b[i] = ai if is_max else human
            val = minimax(b, not is_max, ai, human)
            b[i] = ' '
            best_score = optimize(best_score, val)
    return best_score

def find_best_move(b, ai, human):
    best_val = -math.inf
    best_idx = -1
    for i in range(9):
        if b[i] == ' ':
            b[i] = ai
            move_val = minimax(b, False, ai, human)
            b[i] = ' ' 
            if move_val > best_val:
                best_val = move_val
                best_idx = i
    return best_idx

def main():
    board = [' '] * 9
    human, ai = 'X', 'O'
    player = human

    print("Welcome to Tic Tac Toe! Positions: 0-8")
    print_board([str(i) for i in range(9)])

    while True:
        print("\nCurrent board:")
        print_board(board)

        if player == human:
            try:
                move = int(input(f"Your move ({human}): "))
                if move not in range(9) or board[move] != ' ':
                    print("Invalid move.")
                    continue
            except ValueError:
                print("Enter a number 0-8.")
                continue
        else: 
            move = find_best_move(board, ai, human)
            print(f"AI chooses position {move}")

        board[move] = player

        if check_win(board, player):
            print_board(board)
            print("You win!" if player == human else "AI wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
    
        player = ai if player == human else human

if __name__ == "__main__":
    main()