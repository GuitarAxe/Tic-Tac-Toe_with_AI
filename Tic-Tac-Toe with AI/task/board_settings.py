from constants import X_CHAR
from constants import O_CHAR
from constants import __CHAR
import traceback


def print_board(board):
    print("---------")
    for y in range(1, 4):
        print("| ", end="")
        for x in range(1, 4):
            board_field = count_board_field(y, x)
            if isinstance(board[board_field], int):
                print("  ", end="")
            else:
                print(str(board[board_field]) + " ", end="")
        print("|")
    print("---------")


def change_coordinate(board, mark):
    while True:
        coordinates = input("Enter the coordinates: ").split(" ")
        try:
            y = int(coordinates[0])
            x = int(coordinates[1])

            if y > 3 or y < 1 or x > 3 or x < 1:
                print("Coordinates should be from 1 to 3!")
            elif not isinstance(y, int) and not isinstance(x, int):
                print("This cell is occupied! Choose another one!")
            else:
                board_field = count_board_field(y, x)
                board[board_field] = mark
                return board
        except Exception as e:
            print("You should enter numbers!")
            traceback.print_exc()


def change_mark(new_mark):
    if new_mark == X_CHAR:
        return O_CHAR
    elif new_mark == O_CHAR:
        return X_CHAR


def check_victory(board, marks):
    for char in marks:
        if (board[0] == char and board[1] == char and board[2] == char) or \
                (board[3] == char and board[4] == char and board[5] == char) or \
                (board[6] == char and board[7] == char and board[8] == char) or \
                (board[0] == char and board[3] == char and board[6] == char) or \
                (board[1] == char and board[4] == char and board[7] == char) or \
                (board[2] == char and board[5] == char and board[8] == char) or \
                (board[0] == char and board[4] == char and board[8] == char) or \
                (board[2] == char and board[4] == char and board[6] == char):
            return True
    return False


def check_draw(board):
    counter = 0
    for i in range(0, len(board)):
        if not isinstance(board[i], int):
            counter += 1
        else:
            break
    if counter == 9:
        return True
    return False


def count_board_field(y, x):
    if y == 1:
        return x - 1
    elif y == 2:
        return 2 + x
    elif y == 3:
        return 5 + x
    else:
        raise Exception
