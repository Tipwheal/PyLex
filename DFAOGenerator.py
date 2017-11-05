import DFA
import NFA
import DFAO
import ReadLex


def get_combine_list():
    not_end_state = DFA.not_end_state.copy()
    end_state = DFA.end_state.copy()
    input_list = DFA.input_list.copy()
    cur_list = [not_end_state, end_state]
    cur_list = pre_divide(cur_list)
    next_list = get_division(cur_list, input_list)
    while cur_list != next_list:
        cur_list = next_list.copy()
        next_list = get_division(next_list, input_list)
    get_dfa_o(next_list)


def get_dfa_o(o_list):
    more_than_2 = []
    update_input()
    for a_list in o_list:
        if len(a_list) > 1:
            more_than_2.append(a_list)
    combine_map = {}
    remove_list = []
    for a_list in more_than_2:
        combine_map[a_list[0]] = a_list[1:]
        for item in a_list[1:]:
            remove_list.append(item)
    update_se(remove_list)
    for d_state in DFA.transition_table.keys():
        for path in DFA.transition_table[d_state].keys():
            d_next = DFA.transition_table[d_state][path]
            add_state(remove_list, combine_map, d_state, d_next, path)


def update_se(remove_list):
    for s in DFA.start_state:
        if s not in remove_list and s not in DFAO.not_end_list:
            DFAO.not_end_list.append(s)
    for s in DFA.end_state:
        if s not in remove_list and s not in DFAO.end_and_action.keys():
            DFAO.end_and_action[s] = get_action(s)


def update_input():
    for input_ in DFA.input_list:
        DFAO.input_list.append(input_)


def add_state(remove_list, combine_map, from_state, to_state, path):
    if from_state in remove_list:
        for key in combine_map.keys():
            if from_state in combine_map[key]:
                from_state = key
                break
    if to_state in remove_list:
        for key in combine_map.keys():
            if to_state in combine_map[key]:
                to_state = key
                break
    if from_state not in DFAO.path_map.keys():
        DFAO.path_map[from_state] = {}
    DFAO.path_map[from_state][path] = to_state
    if from_state in DFA.not_end_state and from_state not in DFAO.not_end_list:
        DFAO.not_end_list.append(from_state)
    elif from_state in DFA.end_state and from_state not in DFAO.end_and_action.keys():
        DFAO.end_and_action[from_state] = get_action(from_state)
    if to_state in DFA.not_end_state and to_state not in DFAO.not_end_list:
        DFAO.not_end_list.append(to_state)
    elif from_state in DFA.end_state and from_state not in DFAO.end_and_action.keys():
        DFAO.end_and_action[to_state] = get_action(from_state)


def get_action(state):
    n_states = DFA.dn_map[state]
    ends = []
    for s in n_states:
        if s in NFA.end_set:
            ends.append(s)
    min_v = -1
    for s in ends:
        if min_v == -1:
            min_v = int(s)
        else:
            min_v = min(int(s), min_v)
    min_v = str(min_v)
    action = None
    actions = ReadLex.use_map.keys()
    copied_a = []
    for a in actions:
        copied_a.append(a)
    for i in range(len(NFA.end_set)):
        if min_v == NFA.end_set[i]:
            action = ReadLex.use_map[copied_a[i]]
    return action


def get_division(cur_list, input_list):
    result = []
    for a_list in cur_list:
        reach_map = {}
        for d_state in a_list:
            each_list = []
            for input_ in input_list:
                if input_ in DFA.transition_table[d_state].keys():
                    next_ = DFA.transition_table[d_state][input_]
                    for i in range(len(cur_list)):
                        if next_ in cur_list[i]:
                            each_list.append(i)
                else:
                    each_list.append(-1)
            reach_map[d_state] = each_list
        for sub in get_group(reach_map):
            result.append(sub)
    return result


def get_group(a_map):
    key_set = a_map.keys()
    result_list = []
    for key in key_set:
        if result_list == []:
            result_list.append([key])
        else:
            in_ = -1
            for inner_list in result_list:
                if a_map[inner_list[0]] == a_map[key]:
                    in_ = inner_list
                    break
            if in_ == -1:
                result_list.append([key])
            else:
                in_.append(key)
    return result_list


def pre_divide(a_list):
    end_list = a_list[1].copy()
    l_split = {}
    result_list = []
    for d_state in end_list:
        temp = []
        n_states = DFA.dn_map[d_state]
        for n_s in n_states:
            if n_s in NFA.end_set:
                temp.append(n_s)
        l_split[d_state] = temp
    for key in l_split:
        if result_list == []:
            result_list.append([key])
        else:
            in_ = -1
            for inner_list in result_list:
                if l_split[inner_list[0]] == l_split[key]:
                    in_ = inner_list
                    break
            if in_ == -1:
                result_list.append([key])
            else:
                in_.append(key)
    result_list.append(a_list[0])
    return result_list