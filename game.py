#!/usr/bin/python3.7

# import numpy as np
from tabulate import tabulate
import copy

EMPTY = 0
PIECE = 1
DOUBLE = 2

def initialize():
    test_state = [
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0,-1, 0, 0, 0, 0, 0],
    [ 0, 1, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0,-1, 0,-1, 0,-1, 0],
    [ 0, 0, 0, 2, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return (test_state, 1, None)

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

    return (state, 1, None)

def transition(state, old_pos, new_pos):
    state = copy.deepcopy(state)
    old_row, old_col = old_pos
    new_row, new_col = new_pos

    sign = lambda x: (1, -1)[x < 0]

    # if the move is a jump
    if abs(new_row - old_row) == 2:
        row_diff, col_diff = new_row - old_row, new_col - old_col
        row_diff, col_diff = row_diff - sign(row_diff), col_diff - sign(col_diff)
        state[0][old_row + row_diff][old_col + col_diff] = 0

        # set the piece to its new location and clear the space it was in
        state[0][new_row][new_col] = state[0][old_row][old_col]
        state[0][old_row][old_col] = 0
        state = (state[0], state[1], (new_row,new_col))
        if possible_jumps(state, new_pos):
            return state
    else:
        # set the piece to its new location and clear the space it was in
        state[0][new_row][new_col] = state[0][old_row][old_col]
        state[0][old_row][old_col] = 0

    # return new board with the turn set to the opponent
    return (state[0], -1 if state[1] == 1 else 1, None)


def is_valid_transition(state, old_pos, new_pos):
    old_row, old_col = old_pos
    new_row, new_col = new_pos
    # bounds
    if new_row < 0 or new_col < 0 or new_row > 7 or new_col > 7:
        return False
    # overlap
    if state[0][new_row][new_col] != EMPTY:
        return False

    # player moves his own piece
    if state[1] == -1 and state[0][old_pos[0]][old_pos[1]] > 0:
        return False
    if state[1] == 1 and state[0][old_pos[0]][old_pos[1]] < 0:
        return False

    # if a jump started move the same piece
    if state[2] != None and old_pos != state[2]:
        return False

    return True

def possible_transitions(state):
    if state[2] != None:
        return possible_jumps(state, state[2])
    return possible_transitions_normal(state) + possible_transitions_jump(state)

def possible_transitions_normal(state):
    result = []
    # sign = state[1]
    # for i in range(len(state[0])):
    #     for j in range(len(state[0][i])):
    #         old_pos = (i, j)
    #         if state[0][i][j] == sign * PIECE or state[0][i][j] == sign * DOUBLE:
    #             new_pos1 = (i + sign * -1, j - 1)
    #             new_pos2 = (i + sign * -1, j + 1)
    #             if is_valid_transition(state, old_pos, new_pos1):
    #                 result.append(transition(state, old_pos, new_pos1))
    #             if is_valid_transition(state, old_pos, new_pos2):
    #                 result.append(transition(state, old_pos, new_pos2))
    #         if state[0][i][j] == sign * DOUBLE:
    #             new_pos3 = (i + sign, j - 1)
    #             new_pos4 = (i + sign, j + 1)
    #             if is_valid_transition(state, old_pos, new_pos3):
    #                 result.append(transition(state, old_pos, new_pos3))
    #             if is_valid_transition(state, old_pos, new_pos4):
    #                 result.append(transition(state, old_pos, new_pos4))
    return result

def possible_transitions_jump(state):
    result = []
    for i in range(len(state[0])):
        for j in range(len(state[0][i])):
            result += possible_jumps(state, (i,j))
    return result


def possible_jumps(state, piece):
    result = []
    sign = state[1]
    i,j = piece
    print('possible_jumps', state[0][i][j])
    if state[0][i][j] == sign * PIECE or state[0][i][j] == sign * DOUBLE:
        new_pos1 = (i + sign * -2, j - 2)
        jump_over1 = (i + sign * -1, j - 1)
        new_pos2 = (i + sign * -2, j + 2)
        jump_over2 = (i + sign * -1, j + 1)
        if is_valid_transition(state, piece, new_pos1) and enemy_piece(state, jump_over1[0], jump_over1[1]):
            result += possible_jumps(state, new_pos1)

        if is_valid_transition(state, piece, new_pos2) and enemy_piece(state, jump_over2[0], jump_over2[1]):
            result += possible_jumps(state, new_pos2)

    if state[0][i][j] == sign * DOUBLE:
        new_pos3 = (i + sign * 2, j - 2)
        jump_over3 = (i + sign, j - 1)
        new_pos4 = (i + sign * 2, j + 2)
        jump_over4 = (i + sign, j + 1)
        if is_valid_transition(state, piece, new_pos3) and enemy_piece(state, jump_over3[0], jump_over3[1]):
            result += possible_jumps(state, new_pos3)
        if is_valid_transition(state, piece, new_pos4) and enemy_piece(state, jump_over4[0], jump_over4[1]):
            result += possible_jumps(state, new_pos4)
    return result

def enemy_piece(state, row, col):
    if state[1] == 1 and state[0][row][col] < 0:
        return True
    elif state[1] == -1 and state[0][row][col] > 0:
        return True
    return False


#  0 - if the state is not final
#  1 - if white won
# -1 - if black won
def is_final_state(state):
    white, black = 0, 0
    for row in state[0]:
        for cell in row:
            if cell == PIECE or cell == DOUBLE:
                white += 1
            elif cell == -PIECE or cell == -DOUBLE:
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
            elif el == DOUBLE:
                result[row].append('●●')
            elif el == -DOUBLE:
                result[row].append('○○')
            else:
                result[row].append('')

    print(f'{"white" if state[1] == 1 else "black"}s turn:')
    print(tabulate(result, headers = range(8), showindex='always', tablefmt='fancy_grid'))
