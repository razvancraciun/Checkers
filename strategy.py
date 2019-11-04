import game as g

def minimax(state, maximise = False, depth = 0, max_depth = 5):
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



def maximum_value(state, alpha = float('-inf'), beta = float('-inf'), depth = 0, max_depth = 5):
    if depth >= max_depth or g.is_final_state(state) != 0:
        return (None, g.heuristic(state)) # here
    max_val = float('-inf')
    action = None
    for t in g.possible_transitions(state):
        succ = g.transition(state, t[0], t[1])
        act,val = minimum_value(succ, alpha, beta, depth + 1, max_depth)
        if max_val < val:
            max_val = val
            action = act
        if max_val >= beta:
            return (action, max_val)
        alpha = max(max_val, alfa)
    return (action, max_val)



def minimum_value(state, alpha = float('-inf'), beta = float('-inf'), depth = 0, max_depth = 5):
    if depth >= max_depth or g.is_final_state(state) != 0:
        return (None, g.heuristic(state)) # aand here
    val_min = float('inf')
    action = None
    for t in g.possible_transitions(state):
        succ = g.transition(state, t[0], t[1])
        act, val = maximum_value(succ, alpha, beta, depth + 1, max_depth)
        if val_min > val:
            val_min = val_min
            action = act
        if alpha >= val_min:
            return (action, val_min)
        beta = min(val_min, beta)
    return (action, val_min)
