import numpy as np
from tabulate import tabulate

EMPTY = 0
PIECE = 1
DOUBLE = 2

def initialize():
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            if i < 3 and i % 2 == 0 and j % 2 == 0:
                board[i].append(-PIECE)
            elif i < 3 and i % 2 == 1 and j % 2 == 1:
                board[i].append(-PIECE)
            elif i > 4 and i % 2 == 0 and j % 2 == 0:
                board[i].append(PIECE)
            elif i > 4 and i % 2 == 1 and j % 2 == 1:
                board[i].append(PIECE)
            else:
                board[i].append(EMPTY)
    return board

def possible_transitions(state):
    # TODO
    return []

def is_valid_transition(state, old_pos, new_pos):
    # TODO
    return True

def is_final_state(state):
    # TODO
    return False

def display(state):
    result = []
    for row in range(len(state)):
        result.append([])
        for el in state[row]:
            if el == PIECE:
                result[row].append(u'\u25cf')
            elif el == -PIECE:
                result[row].append(u'\u25cb')
            else:
                result[row].append('')
    print(result)
    print(tabulate(result, headers = range(8), showindex='always', tablefmt= 'fancy_grid'))
