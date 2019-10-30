#!/usr/bin/python3.7

import game as g
from os import system, name

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def main():
    state = g.initialize()
    while not g.is_final_state(state):
        # clear()
        g.display(state)
        if state[1] == 1:
            old_pos, new_pos = (0, 0), (0, 0)
            try:
                print('choose a piece to move:')
                old_pos = (int(input('   row = ')), int(input('   col = ')))
                print('choose where to move it:')
                new_pos = (int(input('   row = ')), int(input('   col = ')))
            except:
                continue
            if g.is_valid_transition(state, old_pos, new_pos) and g.transition(state, old_pos, new_pos) in g.possible_transitions(state):
                state = g.transition(state, old_pos, new_pos)
        else:
            pass

if __name__ == '__main__':
    main()
