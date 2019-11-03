import game as g
from util import to_tuple

def minimax(state, maximise = False, depth = 0, max_depth = 2):
    if depth >= max_depth or g.is_final_state(state) != 0:
        return (None, g.heuristic(state))
    
    hs = []
    for t in g.possible_transitions(state):
        new_state = g.transition(state, t[0], t[1])
        hs.append((t, minimax(new_state, not maximise, depth + 1, max_depth)[1]))
    
    if maximise:
        result = max(hs, key = lambda item: item[1])
        return result
    else:
        result = min(hs, key = lambda item: item[1])
        return result

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
