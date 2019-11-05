#!/usr/bin/python3.7

from os import system, name
from random import randint
from time import sleep
from termcolor import colored
import game as g
import strategy as s
import time

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

INPUT_ERROR_MSG = colored('Input is invalid!', 'red') + ' Try again.'
MOVE_ERROR_MSG = colored('Move is invalid!', 'red') + ' Try another move.'

def main():
    log = open('log.txt', 'w')
    state, msg = g.initialize(), ''
    while g.is_final_state(state) == 0:
        # display
        clear()
        print(msg)
        msg = ''
        g.display_board(state)
        if state[1] == -1:
            sleep(1)
        # game logic
        if state[1] == 1:
            # old_pos, new_pos = (0, 0), (0, 0)
            # try:
            #     print('choose a piece to move:')
            #     old_pos = (int(input('   row = ')), int(input('   col = ')))
            #     print('choose where to move it:')
            #     new_pos = (int(input('   row = ')), int(input('   col = ')))
            # except:
            #     msg = INPUT_ERROR_MSG
            #     continue
            # if g.is_valid_transition(state, old_pos, new_pos):
            #     state = g.transition(state, old_pos, new_pos)
            # else:
            #     msg = MOVE_ERROR_MSG
            starting_time = time.time()
            t = s.maximum_value(state)[0]
            state = g.transition(state, t[0], t[1])
            log.write('Alfa-beta ' + str( (time.time() - starting_time) * 1000 ) + '\n')
        else:
            starting_time = time.time()
            t = s.minimax(state)[0]
            state = g.transition(state, t[0], t[1])
            log.write('Minimax ' + str( (time.time() - starting_time) * 1000 ) + '\n')

    # end game
    clear()
    g.display_board(state)
    switch = {
         1: lambda: print(colored('⬤ ', 'white') + 'White won!'),
        -1: lambda: print(colored('⬤ ', 'gray')  + 'Black won!'),
         2: lambda: print(colored('⬤ ', 'white') + 'White is blocked. It\'s a draw!'),
        -2: lambda: print(colored('⬤ ', 'gray')  + 'Black is blocked. It\'s a draw!')
    }
    switch[g.is_final_state(state)]()

if __name__ == '__main__':
    main()
