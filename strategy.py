import game as g

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

ALPHA = float('-inf')
BETA = float('-inf')

def maximum_value(state, depth = 0, max_depth = 10):
    global ALPHA, BETA
    if depth >= max_depth or g.is_final_state(state) != 0:
        return (None, g.heuristic(state)) # here
    max_val = float('-inf')
    action = None
    for t in g.possible_transitions(state):
        succ = g.transition(state, t[0], t[1])
        _,val = minimum_value(succ, depth + 1, max_depth)
        if max_val < val:
            max_val = val
            action = t
        if max_val >= BETA:
            return (action, max_val)
        ALPHA = max(max_val, ALPHA)
    return (action, max_val)



def minimum_value(state, depth = 0, max_depth = 8):
    global ALPHA, BETA
    if depth >= max_depth or g.is_final_state(state) != 0:
        return (None, g.heuristic(state)) # aand here
    val_min = float('inf')
    action = None
    for t in g.possible_transitions(state):
        succ = g.transition(state, t[0], t[1])
        _, val = maximum_value(succ, depth + 1, max_depth)
        if val_min > val:
            val_min = val_min
            action = t
        if ALPHA >= val_min:
            return (action, val_min)
        BETA = min(val_min, BETA)
    return (action, val_min)
