
from ui.ui_util import *

def choose_board_position(board):
    print("Choose position x ({} - {}) ".format(0, board.width))
    x = read_bounded_int(0, board.width)
    if x is None: return None

    print("Choose position y ({} - {}) ".format(0, board.height))
    y = read_bounded_int(0, board.height)
    if y is None: return None

    return (x, y)

def choose_free_board_position(board):

    while True:
        pos = choose_board_position(board)
        if pos is None: return None

        x = pos[0]
        y = pos[1]

        current = board.get(x, y)
        if not current is None:
            print ('Position ({}, {}) is not free', 'Try again', sep='\n')
            continue
        else:
            return (x, y)

