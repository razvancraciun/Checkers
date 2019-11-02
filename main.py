#!/usr/bin/python3.7

from os import system, name
from random import randint
from time import sleep
from termcolor import colored
import game as g
import strategy as s

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

INPUT_ERROR_MSG = colored('Input is invalid!', 'red') + ' Try again.'
MOVE_ERROR_MSG = colored('Move is invalid!', 'red') + ' Try another move.'

# TODO: actual computer login (choose transition based on heuristic)
# display winner
def main():
    state, msg = g.initialize(), ''
    # while not g.is_final_state(state):
    #     # display
    #     clear()
    #     print(msg)
    #     msg = ''
    #     g.display_board(state)
    #     if state[1] == -1:
    #         sleep(1)
    #     # game logic
    #     if state[1] == 1:
    #         old_pos, new_pos = (0, 0), (0, 0)
    #         try:
    #             print('choose a piece to move:')
    #             old_pos = (int(input('   row = ')), int(input('   col = ')))
    #             print('choose where to move it:')
    #             new_pos = (int(input('   row = ')), int(input('   col = ')))
    #         except:
    #             msg = INPUT_ERROR_MSG
    #             continue
    #         if g.is_valid_transition(state, old_pos, new_pos):
    #             state = g.transition(state, old_pos, new_pos)
    #         else:
    #             msg = MOVE_ERROR_MSG
    #     else:
    #         possible_states = [g.transition(state, t[0], t[1]) for t in g.possible_transitions(state)]
    #         min_heuristic = min([g.heuristic(s) for s in possible_states])
    #         possible_states = list(filter(lambda s: g.heuristic(s) == min_heuristic, possible_states))
    #
    #         state = possible_states[randint(0, len(possible_states) - 1)]
    s.minimax(state, 5)

if __name__ == '__main__':
    main()
