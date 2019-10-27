#!/usr/bin/python3.7

# import numpy as np
from tabulate import tabulate

EMPTY = 0
PIECE = 1
DOUBLE = 2

def initialize():
    #  test_state = [
    #     [ 0,-1, 0,-1, 0,-1, 0,-1],
    #     [ 0, 0, 0, 0, 0, 0, 0, 0],
    #     [ 0, 0, 0, 0, 0, 0, 0, 0],
    #     [ 0, 0,-1, 0,-1, 0, 0, 0],
    #     [ 0, 0, 0,-1, 0, 0, 0, 0],
    #     [ 0, 0,-1, 0,-1, 0, 0, 0],
    #     [ 0, 0, 0, 0, 0, 0, 0, 0],
    #     [ 1, 0, 1, 0, 1, 0, 1, 0]
    # ]
    # return (test_state,  -1)

    state = []
    for i in range(8):
        state.append([])
        for j in range(8):
            if i < 3 and i % 2 == 0 and j % 2 == 1:
                state[i].append(-PIECE)
            elif i < 3 and i % 2 == 1 and j % 2 == 0:
                state[i].append(-PIECE)
            elif i > 4 and i % 2 == 0 and j % 2 == 1:
                state[i].append(PIECE)
            elif i > 4 and i % 2 == 1 and j % 2 == 0:
                state[i].append(PIECE)
            else:
                state[i].append(EMPTY)
    return (state, 1)

def transition(state, old_pos, new_pos):
    old_row, old_col = old_pos
    new_row, new_col = new_pos

    # set the piece to its new location and clear the space it was in
    state[0][new_row][new_col] = state[0][old_row][old_col]
    state[0][old_row][old_col] = 0
    
    sign = lambda x: (1, -1)[x < 0]

    # if the move is a jump
    if abs(new_row - old_row) == 2:
        row_diff, col_diff = new_row - old_row, new_col - old_col
        row_diff, col_diff = row_diff - sign(row_diff), col_diff - sign(col_diff)
        # if the piece that was jumped upon was an enemy
        if state[0][old_row + row_diff][old_col + col_diff] * state[1] < 0:
            state[0][old_row + row_diff][old_col + col_diff] = 0

    # return new board with the turn set to the opponent
    return (state[0], -1 if state[1] == 1 else 1)

def is_valid_transition(state, old_pos, new_pos):
    # TODO
    return True

def possible_transitions(state):
    # TODO
    return []

#  0 - if the state is not final
#  1 - if white won
# -1 - if black won
def is_final_state(state):
    white, black = 0, 0
    for row in state[0]:
        for cell in row:
            if cell == 1:
                white += 1
            else:
                black += 1
    if white > 0 and black == 0:
        return 1
    if white == 0 and black > 0:
        return -1
    return 0

def display(state):
    result = []
    for row in range(len(state[0])):
        result.append([])
        for el in state[0][row]:
            if el == PIECE:
                result[row].append('●')
            elif el == -PIECE:
                result[row].append('○')
            else:
                result[row].append('')

    print(f'{"white" if state[1] == 1 else "black"}s turn:')
    print(tabulate(result, headers = range(8), showindex='always', tablefmt='fancy_grid'))
