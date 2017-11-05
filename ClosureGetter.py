import NFA


closure_map = {}


def calc_closure():
    all_ep_list = []
    for a_list in NFA.path_list:
        if a_list[1] == "ε":
            all_ep_list.append(a_list.copy())
    for state in NFA.end_set + NFA.not_end_set:
        result = [state]
        walked_list = [state]
        for a_list in all_ep_list:
            if a_list[0] == state and a_list[2] not in result:
                result.append(a_list[2])
        while walked_list != result:
            for s in result:
                if s not in walked_list:
                    walked_list.append(s)
                    for a_list in all_ep_list:
                        if a_list[0] == s and a_list[2] not in result:
                            result.append(a_list[2])
        closure_map[state] = result


def get_closure(state_set):
    result = []
    for s in state_set:
        a_list = closure_map[s]
        for item in a_list:
            if item not in result:
                result.append(item)
    return result