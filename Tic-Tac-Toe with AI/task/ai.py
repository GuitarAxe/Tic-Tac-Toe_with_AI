import random
import board_settings
import copy
import hard_ai_settings
from constants import __CHAR


def easy_ai(board, mark):
    if all(isinstance(item, str) for item in board):
        return board
    print('Making move level "easy"')
    return generate_random_field(board, mark)


def medium_ai(board, mark):
    if all(isinstance(item, str) for item in board):
        return board
    result = check_possible_moves(board, mark, mark)
    if result is not None:
        return result
    result = check_possible_moves(board, mark, board_settings.change_mark(mark))
    if result is not None:
        return result
    return generate_random_field(board, mark)


def hard_ai(board, player, mark, opponent_mark):
    if all(isinstance(item, str) for item in board):
        return board
    best_move = hard_ai_settings.minimax(board, player, mark, opponent_mark)
    board[best_move] = mark
    return board


def generate_random_field(board, mark):
    while True:
        y = random.randint(1, 3)
        x = random.randint(1, 3)
        board_field = board_settings.count_board_field(x, y)
        if isinstance(board[board_field], int):
            board[board_field] = mark
            return board


def check_possible_moves(board, mark, mark_to_check):
    for i in range(0, len(board)):
        if isinstance(board[i], int):
            check_board = copy.deepcopy(board)
            check_board[i] = mark_to_check
            if board_settings.check_victory(check_board, mark_to_check):
                board[i] = mark
                return board
    return None


def contains(board, given_char):
    if given_char in board:
        return True
    return False
