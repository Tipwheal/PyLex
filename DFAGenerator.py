import NFA
import DFA
import ClosureGetter


count = [0]


def get_transition_table():
    num = 0
    update_dfa_input()
    while num < count[0] or count[0] == 0:
        if count[0] == 0:
            cur_state = ClosureGetter.closure_map[NFA.start_state]
            d_state = str(count[0])
            count[0] += 1
        else:
            d_state = str(num)
            cur_state = DFA.dn_map[d_state]
        if is_end_state(cur_state) and d_state not in DFA.end_state:
            DFA.end_state.append(d_state)
        elif (not is_end_state(cur_state)) and d_state not in DFA.not_end_state:
            DFA.not_end_state.append(d_state)
        num += 1
        DFA.transition_table[d_state] = {}
        DFA.dn_map[d_state] = cur_state
        for input_ in DFA.input_list:
            next_set = ClosureGetter.get_closure(NFA.get_next(cur_state, input_))
            if next_set != []:
                d_id = ""
                for key in DFA.dn_map.keys():
                    if DFA.dn_map[key] == next_set:
                        d_id = key
                        break
                if d_id == "":
                    d_id = str(count[0])
                    count[0] += 1
                    DFA.dn_map[d_id] = next_set
                DFA.transition_table[d_state][input_] = d_id


def update_dfa_input():
    for input_ in NFA.input_set:
        if input_ != "ε":
            DFA.input_list.append(input_)


def is_end_state(state_list):
    for s in state_list:
        if s in NFA.end_set:
            return True
    return False
