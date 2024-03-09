EMPTY = '-'
PLAYER_X = '❌'
PLAYER_O = '⭕'


def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-------------')


def is_winner(board, player):
    
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)


def game_over(board):
    if is_winner(board, PLAYER_X):
        return "Player ❌ wins!"
    elif is_winner(board, PLAYER_O):
        return "Player ⭕ wins!"
    elif is_full(board):
        return "It's a draw!"
    return None


def minimax(board, depth, maximizing_player):
    scores = {'❌': 1, '⭕': -1, 'draw': 0}

    result = game_over(board)
    if result is not None:
        return scores.get(result, 0)  

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

import random

def find_best_move(board):
  
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                if is_winner(board, PLAYER_X):
                    board[i][j] = EMPTY
                    return i, j
                board[i][j] = EMPTY


    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                if is_winner(board, PLAYER_O):
                    board[i][j] = EMPTY
                    return i, j
                board[i][j] = EMPTY

   
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]
    
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return -1, -1  



def play_game():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

    while True:
        print_board(board)
        row, col = map(int, input("Enter your move (row and column, space-separated): ").split())
        
        if board[row][col] == EMPTY:
            board[row][col] = PLAYER_O
        else:
            print("Invalid move. Try again.")
            continue

        result = game_over(board)
        if result is not None:
            print_board(board)
            print(result)
            break

        print("AI is making a move...")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = PLAYER_X

        result = game_over(board)
        if result is not None:
            print_board(board)
            print(result)
            break


if __name__ == "__main__":
    play_game()
