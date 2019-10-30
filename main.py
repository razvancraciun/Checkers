#!/usr/bin/python3.7

from os import system, name
from termcolor import colored
import game as g

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

INPUT_ERROR_MSG = colored('Input is invalid!', 'red') + ' Try again.'
MOVE_ERROR_MSG = colored('Move is invalid!', 'red') + ' Try another move.'

def main():
    state, msg = g.initialize(), ''
    while not g.is_final_state(state):
        # display
        clear()
        print(msg)
        msg = ''
        g.display_board(state)

        # game logic
        old_pos, new_pos = (0, 0), (0, 0)
        try:
            print('choose a piece to move:')
            old_pos = (int(input('   row = ')), int(input('   col = ')))
            print('choose where to move it:')
            new_pos = (int(input('   row = ')), int(input('   col = ')))
        except:
            msg = INPUT_ERROR_MSG
            continue
        if g.is_valid_transition(state, old_pos, new_pos):
            state = g.transition(state, old_pos, new_pos)
        else:
            msg = MOVE_ERROR_MSG

if __name__ == '__main__':
    main()


# if state[1] == 1:
#     old_pos, new_pos = (0, 0), (0, 0)
#     try:
#         print('choose a piece to move:')
#         old_pos = (int(input('   row = ')), int(input('   col = ')))
#         print('choose where to move it:')
#         new_pos = (int(input('   row = ')), int(input('   col = ')))
#     except:
#         msg = INPUT_ERROR_MSG
#         continue
#     if g.is_valid_transition(state, old_pos, new_pos):
#         state = g.transition(state, old_pos, new_pos)
#     else:
#         msg = MOVE_ERROR_MSG
# else:
#    # computer logic here
#    pass