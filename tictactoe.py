import math

def print_board(board):
    for i in range(3):
        print('|'.join(board[i*3:(i+1)*3]))
        if i < 2:
            print('-')

def check_winner(board, player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[pos] == player for pos in line) for line in wins)

def is_board_full(board):
    return all(space != '' for space in board)

def utility(board, ai, human):
    if check_winner(board, ai):
        return 10
    elif check_winner(board, human):
        return -10
    else:
        return 0

def minimax(board, depth, is_maximizing, ai, human):
    score = utility(board, ai, human)

    if score == 10 or score == -10 or is_board_full(board):
        return score

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == '':
                board[i] = ai
                val = minimax(board, depth + 1, False, ai, human)
                board[i] = ''
                best_score = max(best_score, val)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == '':
                board[i] = human
                val = minimax(board, depth + 1, True, ai, human)
                board[i] = ''
                best_score = min(best_score, val)

        return best_score

def best_move(board, ai, human):
    best_val = -math.inf
    move = None

    for i in range(9):
        if board[i] == '':
            board[i] = ai
            move_val = minimax(board, 0, False, ai, human)
            board[i] = ''

            if move_val > best_val:
                best_val = move_val
                move = i

    return move

def main():
    board = ['' for _ in range(9)]
    human = 'X'
    ai = 'O'
    current_player = human

    print("Welcome to Tic Tac Toe!")
    print("Positions on the board are numbered 0-8 as follows:")
    print_board([str(i) for i in range(9)])

    while True:
        print("\nCurrent board:")
        print_board(board)

        if current_player == human:
            try:
                move = int(input("Your move (0-8): "))
                if move < 0 or move > 8 or board[move] != '':
                    print("Invalid move. Please try again.")
                    continue
            except ValueError:
                print("Please enter a valid integer from 0 to 8.")
                continue
            
            board[move] = human

        else:
            move = best_move(board, ai, human)
            print(f"AI chooses position {move}")
            board[move] = ai

        if check_winner(board, current_player):
            print_board(board)
            if current_player == human:
                print("Congratulations! You win!")
            else:
                print("AI wins! Better luck next time.")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = ai if current_player == human else human

if __name__ == "__main__":
    main()
