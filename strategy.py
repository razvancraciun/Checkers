import game as g
from util import to_tuple


def minimax(state, max = True, depth = 0, max_depth = 5):
    val = {}
    if depth >= max_depth or g.is_final_state(state) != 0:
        return (None, g.heuristic(state))
    for transition in g.possible_transitions(state):
        old_pos,new_pos = transition
        new_state = g.transition(state, old_pos, new_pos)
        _, val[to_tuple(state)] = minimax(new_state, not max, depth+1, max_depth)

    # if max:
    #     # return (starea cu val maxim din tranzitiile posibile, valoarea maxima)
    #     return (g.possible_transitions(state)[val.argmax()])
