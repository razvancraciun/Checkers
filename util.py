def to_tuple(list):
    for i in range(len(list)):
        if type(list[i]) == type([]) and type(list) == type([]):
            list[i] = to_tuple(list[i])
    return tuple(list)
