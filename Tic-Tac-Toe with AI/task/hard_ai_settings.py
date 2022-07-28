import copy
from tictactoe import game_board
from constants import X_CHAR
from constants import O_CHAR
from constants import __CHAR
from board_settings import check_victory
from constants import USER
from constants import EASY
from constants import MEDIUM

# original_board = copy.deepcopy(game_board)


def empty_indexes(board):
    new_board = []
    for i in range(0, len(board)):
        if isinstance(board[i], int):
            new_board.append(board[i])
    return new_board


def minimax(new_board, player, ai_player, opponent_player):
    available_spots = empty_indexes(new_board)

    if check_victory(new_board, [opponent_player]):
        return -10
    elif check_victory(new_board, [ai_player]):
        return 10
    elif len(available_spots) == 0:
        return 0

    moves = []
    for i in range(0, len(available_spots)):
        move = []
        index = new_board[available_spots[i]]

        # set the empty spot to the current player
        new_board[available_spots[i]] = ai_player

        #collect the score resulted from calling minimax
        #  on the opponent of the current player*/
        if player in [USER, EASY, MEDIUM]:
            result = minimax(new_board, "user", opponent_player, ai_player)
            move.append(result)
        else:
            result = minimax(new_board, "hard", ai_player, opponent_player)
            move.append(result)

        # reset the spot to empty
        new_board[available_spots[i]] = index

        # push the object to the array
        moves.append(move)

    # if it is the computer's turn loop over the moves and choose the move with the highest score
    best_move = None
    if player in [USER, EASY, MEDIUM]:
        best_score = -10000
        for i in range(0, len(moves)):
            if sum(moves[i]) > best_score:
                best_score = sum(moves[i])
                best_move = i
    else:
    # else loop over the moves and choose the move with the lowest score
        best_score = 10000
        for i in range(0, len(moves)):
            if sum(moves[i]) < best_score:
                best_score = sum(moves[i])
                best_move = i

    # return the chosen move (object) from the moves array
    return moves[best_move]
