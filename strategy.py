import game as g
from util import to_tuple


# def minimax(state, max = True, depth = 0, max_depth = 5):
#     val = {}
#     if depth >= max_depth or g.is_final_state(state) != 0:
#         return (None, g.heuristic(state))
#     for transition in g.possible_transitions(state):
#         old_pos,new_pos = transition
#         new_state = g.transition(state, old_pos, new_pos)
#         _, val[to_tuple(state)] = minimax(new_state, not max, depth+1, max_depth)

    # if max:
    #     # return (starea cu val maxim din tranzitiile posibile, valoarea maxima)
    #     return (g.possible_transitions(state)[val.argmax()])


def minimax_it(state, max_depth = 5):
    vals = {}
    depth = {hash(state) : 0}
    parent = { hash(state) : None }
    states = [state]
    while states:
        #TODO add visited check
        current = states.pop()
        possible_transitions = g.possible_transitions(current)
        possible_transitions = [transition for transition in possible_transitions if not g.transition(current, transition[0], transition[1]) in states]
        for transition in g.possible_transitions(current):
            new_state = g.transition(current, old_pos, new_pos)
            depth[hash(new_state)] = depth[hash(current)] + 1
            parent[hash(new_state)] = current
            if depth[hash(new_state)] >= max_depth or g.is_final_state(new_state) != 0:
                vals[hash(new_state)] = g.heuristic(current)
                # here we have the values for all the states on the last level
    #TODO propagate values up the tree



def hash(state):
    pow = 0
    conf1 = 0
    conf2 = 0
    for row in state[0]:
        for el in row:
            if el > 0:
                conf1 += 2**pow
            else:
                conf2 += 2**pow
            pow += 1
    return (conf1, conf2, state[1])
