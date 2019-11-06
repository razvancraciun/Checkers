#!/usr/bin/python3.7

from tabulate import tabulate
from termcolor import colored
from copy import deepcopy

# The state of the game contains a 8×8 matrix representing the game board
# Each slot on the board can either be:
#       0 - if it is empty
#   +1/-1 - if it is a normal piece
#   +2/-2 - if it is a normal piece
# The state also contains +1/-1 demending on what player must move on the current turn
# +1 represents the white player
# -1 represents the black player
# The sign of any given piece on the board denotes its perspective owner

EMPTY = 0
NPIECE = 1
SPIECE = 2
BOARD_SIZE = 8

def initialize():
    test_state = [
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0,-1, 0,-1, 0,-1, 0],
    [ 0,-1, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1, 0,-1, 0],
    [ 0, 1, 0, 1, 0, 1, 0, 1],
    [ 1, 0, 0, 0, 1, 0, 1, 0],
    [ 0, 1, 0, 1, 0, 1, 0, 0],
    [ 0, 0, 1, 0, 0, 0, 0, 0]
    ]
    # return (test_state, 1)

    state = []
    for i in range(BOARD_SIZE):
        state.append([])
        for j in range(8):
            if i < 3 and i % 2 == 0 and j % 2 == 1:
                state[i].append(-NPIECE)
            elif i < 3 and i % 2 == 1 and j % 2 == 0:
                state[i].append(-NPIECE)
            elif i > 4 and i % 2 == 0 and j % 2 == 1:
                state[i].append(NPIECE)
            elif i > 4 and i % 2 == 1 and j % 2 == 0:
                state[i].append(NPIECE)
            else:
                state[i].append(EMPTY)

    return (state, 1)

def interpolate(pos1, pos2):
    sign = lambda x: (1, -1)[x < 0]
    idiff = pos2[0] - pos1[0] - sign(pos2[0] - pos1[0])
    jdiff = pos2[1] - pos1[1] - sign(pos2[1] - pos1[1])
    return (pos1[0] + idiff, pos1[1] + jdiff)

def transition(state, old_pos, new_pos):
    state = deepcopy(state)
    old_row, old_col = old_pos
    new_row, new_col = new_pos

    # set the piece to its new location and clear the space it was in
    # change piece to special piece if it reaches the end of the board
    if state[1] == 1 and new_row == 0:
        state[0][new_row][new_col] = SPIECE
    elif state[1] == -1 and new_row == 7:
        state[0][new_row][new_col] = -SPIECE
    else:
        state[0][new_row][new_col] = state[0][old_row][old_col]
    state[0][old_row][old_col] = 0

    # if the move is a jump
    if abs(new_row - old_row) == 2:
        jump_row, jump_col = interpolate(old_pos, new_pos)
        # if the piece that was jumped upon was an enemy
        if state[0][jump_row][jump_col] * state[1] < 0:
            state[0][jump_row][jump_col] = 0

    # return new board with the turn set to the opponent
    return (state[0], -1 if state[1] == 1 else 1)

def is_valid_transition(state, old_pos, new_pos):
    old_row, old_col = old_pos
    new_row, new_col = new_pos
    # must move within bounds of the board
    if new_row < 0 or new_col < 0 or new_row > 7 or new_col > 7:
        return False
    # must move to free space
    if state[0][new_row][new_col] != EMPTY:
        return False
    # player must move a piece and that piece must be his
    if state[1] * state[0][old_row][old_col] <= 0:
        return False
    # move must be normal or jump
    if abs(new_row - old_row) > 2:
        return False
    # a normal piece must always move forward
    if abs(state[0][old_row][old_col]) == NPIECE and (new_row - old_row) * state[1] > 0:
        return False
    # there needs to be a piece for the jump to be performed
    # the piece it jumped over needs to be an enemy
    if abs(new_row - old_row) == 2:
        jump_row, jump_col = interpolate(old_pos, new_pos)
        # if the piece that was jumped upon was an enemy
        if state[0][jump_row][jump_col] * state[1] >= 0:
            return False

    return True

#  0 - if the state is not final
# +1 - if white won
# -1 - if black won
# +2 - if white is blocked
# -2 - if black is blocked
def is_final_state(state):
    white, black = 0, 0
    for row in state[0]:
        for cell in row:
            if cell == NPIECE or cell == SPIECE:
                white += 1
            elif cell == -NPIECE or cell == -SPIECE:
                black += 1
    if white > 0 and black == 0:
        return 1
    if white == 0 and black > 0:
        return -1
    if len(possible_transitions(state)) == 0:
        return 2 * state[1]
    return 0

# check the difference in pieces but special pieces are more important
# white will maximise, black will minimise
def heuristic(state):
    result = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if abs(state[0][i][j]) == NPIECE:
                result += state[0][i][j]
            elif abs(state[0][i][j]) == SPIECE:
                result += 2 * state[0][i][j]
    return result

def possible_transitions_normal(state):
    result = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            pos = (i, j)
            # check front diagonal move options
            if state[0][i][j] == state[1] * NPIECE or state[0][i][j] == state[1] * SPIECE:
                trans_pos = (i - state[1], j - 1)
                if is_valid_transition(state, pos, trans_pos):
                    result.append((pos, trans_pos))
                trans_pos = (i - state[1], j + 1)
                if is_valid_transition(state, pos, trans_pos):
                    result.append((pos, trans_pos))
            # check back diagonal move options if piece is special
            if state[0][i][j] == state[1] * SPIECE:
                trans_pos = (i + state[1], j - 1)
                if is_valid_transition(state, pos, trans_pos):
                    result.append((pos, trans_pos))
                trans_pos = (i + state[1], j + 1)
                if is_valid_transition(state, pos, trans_pos):
                    result.append((pos, trans_pos))
    return result

def possible_transitions_jump(state):
    result = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            pos = (i, j)
            # check front diagonal jump options
            if state[0][i][j] == state[1] * NPIECE or state[0][i][j] == state[1] * SPIECE:
                trans_pos = (i - 2 * state[1], j - 2)
                if is_valid_transition(state, pos, trans_pos):
                    result.append((pos, trans_pos))
                trans_pos = (i - 2 * state[1], j + 2)
                if is_valid_transition(state, pos, trans_pos):
                    result.append((pos, trans_pos))
            # check back diagonal jump options if piece is special
            if state[0][i][j] == state[1] * SPIECE:
                trans_pos = (i + 2 * state[1], j - 2)
                if is_valid_transition(state, pos, trans_pos):
                    result.append((pos, trans_pos))
                trans_pos = (i + 2 * state[1], j + 2)
                if is_valid_transition(state, pos, trans_pos):
                    result.append((pos, trans_pos))
    return result

def possible_transitions(state):
    return possible_transitions_normal(state) + possible_transitions_jump(state)

def display_board(state):
    result = []
    for row in range(len(state[0])):
        result.append([])
        for el in state[0][row]:
            if el == NPIECE:
                result[row].append(colored('⬤', 'white'))
            elif el == -NPIECE:
                result[row].append(colored('⬤', 'grey'))
            elif el == SPIECE:
                result[row].append(colored('⬤⬤', 'white'))
            elif el == -SPIECE:
                result[row].append(colored('⬤⬤', 'grey'))
            else:
                result[row].append('')

    print(f'{colored("⬤ ", "white") + "White" if state[1] == 1 else colored("⬤ ", "grey") + "Black"}s turn:')
    print(tabulate(result, headers = range(8), showindex='always', tablefmt='fancy_grid'))
