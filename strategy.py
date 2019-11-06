import game as g
from math import inf

def minimax(state, maximise = False, depth = 0, max_depth = 4):
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

def maximum_value(state, alpha = -inf, beta = inf, depth = 0, max_depth = 2):
    if depth >= max_depth or g.is_final_state(state) != 0:
        return (None, g.heuristic(state))

    max_val, action = -inf, None
    for t in g.possible_transitions(state):
        succ = g.transition(state, t[0], t[1])
        _, val = minimum_value(succ, alpha, beta, depth + 1, max_depth)
        if max_val < val:
            max_val = val
            action = t
        if max_val >= beta:
            return (action, max_val)
        alpha = max(max_val, alpha)
        
    return (action, max_val)

def minimum_value(state, alpha = -inf, beta = inf, depth = 0, max_depth = 2):
    if depth >= max_depth or g.is_final_state(state) != 0:
        return (None, g.heuristic(state))

    min_val, action = +inf, None
    for t in g.possible_transitions(state):
        succ = g.transition(state, t[0], t[1])
        _, val = maximum_value(succ, alpha, beta, depth + 1, max_depth)
        if min_val > val:
            min_val = min_val
            action = t
        if alpha >= min_val:
            return (action, min_val)
        beta = min(min_val, beta)

    return (action, min_val)
