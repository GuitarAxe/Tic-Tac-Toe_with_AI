import ai
import board_settings
from constants import X_CHAR
from constants import O_CHAR
from constants import __CHAR
from constants import USER
from constants import EASY
from constants import MEDIUM
from constants import HARD
import traceback


def play_game(board, mark, *players):
    while True:
        for player in players:
            board_settings.print_board(board)

            if player == USER:
                board = board_settings.change_coordinate(board, mark)
            elif player == EASY:
                board = ai.easy_ai(board, mark)
            elif player == MEDIUM:
                board = ai.medium_ai(board, mark)
            elif player == HARD:
                board = ai.hard_ai(board, player, mark, board_settings.change_mark(mark))
            mark = board_settings.change_mark(mark)

        if board_settings.check_victory(board, [X_CHAR, O_CHAR]):
            board_settings.print_board(board)
            print(mark + " wins")
            break
        elif board_settings.check_draw(board):
            print("Draw")
            break


def check_players(*players):
    possible_players = [USER, EASY, MEDIUM, HARD]
    for player in players:
        if player not in possible_players:
            raise Exception("Bad player!")


game_board = [0, 1, 2,
              3, 4, 5,
              6, 7, 8]

x_turn = True
active_mark = X_CHAR
all_fields = 0

if __name__ == '__main__':
    while True:
        try:
            input_command = input("Input command: ").split(" ")
            isStart = str(input_command[0])
            if isStart == 'exit':
                break
            first_player = str(input_command[1])
            second_player = str(input_command[2])
            check_players(first_player, second_player)

            if isStart == 'start':
                play_game(game_board, active_mark, first_player, second_player)
            else:
                print("Bad parameters!")
        except Exception as e:
            print("Bad parameters!")
            traceback.print_exc()









