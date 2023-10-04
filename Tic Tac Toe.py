import random
import pickle


def check_game_over(board):
    for row in board:
        for i in range(len(row) - 2):
            if row[i] == row[i + 1] == row[i + 2] != ' ':
                return True
    for col in range(len(board[0])):
        for i in range(len(board) - 2):
            if board[i][col] == board[i + 1][col] == board[i + 2][col] != ' ':
                return True

    for i in range(len(board) - 2):
        for j in range(len(board[0]) - 2):
            if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] != ' ':
                return True

    for i in range(len(board) - 2):
        for j in range(2, len(board[0])):
            if board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] != ' ':
                return True

    if all([cell != ' ' for row in board for cell in row]):
        return True

    return False


def evaluate_board_state(board):
    count_x = 0
    count_o = 0
    for row in board:
        for cell in row:
            if cell == 'X':
                count_x += 1
            elif cell == 'O':
                count_o += 1
    return count_x - count_o


def generate_possible_moves(board):
    moves = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == ' ':
                moves.append((row, col))
    return moves


def beta_move(board, depth, alpha, beta):
    if depth == 0 or check_game_over(board):
        return evaluate_board_state(board)
    possible_moves = generate_possible_moves(board)

    min_value = float('inf')

    for move in possible_moves:
        board=backtrack(board, move)
        updated_board = update_board(board, move, 'O')
        value = alpha_move(updated_board, depth - 1, alpha, beta)
        beta = min(beta, value)
        if alpha >= beta:
            break
        min_value = min(min_value, value)

    return min_value

def alpha_move(board, depth, alpha, beta):
    if depth == 0 or check_game_over(board):
        return evaluate_board_state(board)
    best_move = -float('inf')

    possible_moves = generate_possible_moves(board)
    for move in possible_moves:

        board = backtrack(board, move)
        updated_board = update_board(board, move, 'O')
        move_value = beta_move(updated_board, depth - 1, alpha, beta)
        if move_value > best_move:
            best_move = move_value

        alpha = max(alpha, best_move)

        if alpha >= beta:
            break

    return best_move


def update_board(board, move, player_symbol):
    row, col = move
    board[row][col] = player_symbol
    return board


def backtrack(board, move):
    row, col = move
    board[row][col] = ' '
    return board

def human_player_move(board):
    valid_move = False
    while not valid_move:
        try:
            move = input(" : ")
            row, col = map(int, move.split(','))
            if board[row][col] != ' ':
                print("Invalid move: That position is already occupied.")
            else:
                valid_move = True
        except:
            print("Invalid input.")
    return (row, col)



def ai_player_move(board):
    empty_cells = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                empty_cells.append((i, j))

    row, col = random.choice(empty_cells)

    return (row, col)

def evaluate_board_state(board):
        score = 0
        for i in range(5):
            for j in range(3):
                if board[i][j] == board[i][j + 1] == board[i][j + 2] != ' ':
                    if board[i][j] == "X":
                        score += 100
                    elif board[i][j] == "O":
                        score -= 100

        for i in range(5):
            for j in range(3):
                if board[j][i] == board[j + 1][i] == board[j + 2][i] != ' ':
                    if board[j][i] == "X":
                        score += 100
                    elif board[j][i] == "O":
                        score -= 100

        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == "X":
                score += 100
            elif board[0][0] == "O":
                score -= 100
        if board[1][1] == board[2][2] == board[3][3]:
            if board[1][1] == "X":
                score += 100
            elif board[1][1] == "O":
                score -= 100
        if board[2][2] == board[3][3] == board[4][4]:
            if board[2][2] == "X":
                score += 100
            elif board[2][2] == "O":
                score -= 100

        if board[4][0] == board[3][1] == board[2][2]:
            if board[4][0] == "X":
                score += 100
            elif board[4][0] == "O":
                score -= 100
        if board[3][1] == board[2][2] == board[1][3]:
            if board[3][1] == "X":
                score += 100
            elif board[3][1] == "O":
                score -= 100
        if board[2][2] == board[1][3] == board[0][4]:
            if board[2][2] == "X":
                score += 100
            elif board[2][2] == "O":
                score -= 100


        return score


def generate_possible_moves(board):
        moves = []
        for i in range(5):
            for j in range(5):
                if board[i][j] == " ":
                    moves.append((i, j))
        return moves


def main():
    current_player = random.choice(['X', 'O'])

    board = [[' ' for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if random.random() < 0.5:
                board[i][j] = 'X'
            else:
                board[i][j] = 'O'

    game_over = False
    # Game loop
    while not game_over:
        if current_player == 'X':
            move = human_player_move(board)
            board = update_board(board, move, current_player)
        else:
            move = ai_player_move(board)
            board = update_board(board, move, current_player)
        if check_game_over(board):
            game_over = True
            print('Game Over')

        current_player = 'X' if current_player == 'O' else 'O'