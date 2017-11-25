

LT = "LT"
LE = "LE"
EQ = "EQ"
NE = "NE"
GT = "GT"
GE = "GE"
IF = "IF"
THEN = "THEN"
ELSE = "ELSE"
ID = "ID"
NUMBER = "NUMBER"
RELOP = "RELOP"
input_list = ['\\w', '\\n', '%', 't', 'o', 'k', 'e', 'n', 's', 'y', 'a', 'x', ',', ':', ';', "'", '\\+', '\\-', '\\/', '\\*', '\\L', '\\R', '\\O', '=', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'p', 'q', 'r', 'u', 'v', 'w', 'z']
start_state = "0"
not_end_list = ['0', '2', '7', '11', '13', '14', '15', '16', '17', '18', '19', '20', '27', '28', '29', '30', '31', '32', '34']
end_and_action = {'1': '{}', '3': '{ID}', '4': '{DOT}', '5': '{TO}', '6': '{END}', '8': '{SYN_OR}', '9': '{SETV}', '21': '{SYN_ADD}', '22': '{SYN_SUB}', '23': '{SYN_DIV}', '24': '{SYN_MUL}', '25': '{SYN_L}', '26': '{SYN_R}', '33': '{TK_START}', '35': '{SN_START}'}
path_map = {'0': {'\\w': '1', '\\n': '1', '%': '2', 't': '3', 'o': '3', 'k': '3', 'e': '3', 'n': '3', 's': '3', 'y': '3', 'a': '3', 'x': '3', ',': '4', ':': '5', ';': '6', "'": '7', '\\O': '8', '=': '9', 'A': '3', 'B': '3', 'C': '3', 'D': '3', 'E': '3', 'F': '3', 'G': '3', 'H': '3', 'I': '3', 'J': '3', 'K': '3', 'L': '3', 'M': '3', 'N': '3', 'O': '3', 'P': '3', 'Q': '3', 'R': '3', 'S': '3', 'T': '3', 'U': '3', 'V': '3', 'W': '3', 'X': '3', 'Y': '3', 'Z': '3', 'b': '3', 'c': '3', 'd': '3', 'f': '3', 'g': '3', 'h': '3', 'i': '3', 'j': '3', 'l': '3', 'm': '3', 'p': '3', 'q': '3', 'r': '3', 'u': '3', 'v': '3', 'w': '3', 'z': '3'}, '1': {'\\w': '1', '\\n': '1'}, '2': {'%': '11'}, '3': {'t': '3', 'o': '3', 'k': '3', 'e': '3', 'n': '3', 's': '3', 'y': '3', 'a': '3', 'x': '3', 'A': '3', 'B': '3', 'C': '3', 'D': '3', 'E': '3', 'F': '3', 'G': '3', 'H': '3', 'I': '3', 'J': '3', 'K': '3', 'L': '3', 'M': '3', 'N': '3', 'O': '3', 'P': '3', 'Q': '3', 'R': '3', 'S': '3', 'T': '3', 'U': '3', 'V': '3', 'W': '3', 'X': '3', 'Y': '3', 'Z': '3', 'b': '3', 'c': '3', 'd': '3', 'f': '3', 'g': '3', 'h': '3', 'i': '3', 'j': '3', 'l': '3', 'm': '3', 'p': '3', 'q': '3', 'r': '3', 'u': '3', 'v': '3', 'w': '3', 'z': '3'}, '7': {'\\+': '13', '\\-': '14', '\\/': '15', '\\*': '16', '\\L': '17', '\\R': '18'}, '11': {'t': '19', 's': '20'}, '13': {"'": '21'}, '14': {"'": '22'}, '15': {"'": '23'}, '16': {"'": '24'}, '17': {"'": '25'}, '18': {"'": '26'}, '19': {'o': '27'}, '20': {'y': '28'}, '27': {'k': '29'}, '28': {'n': '30'}, '29': {'e': '31'}, '30': {'t': '32'}, '31': {'n': '33'}, '32': {'a': '34'}, '34': {'x': '35'}}
change_map = {" ": "\\w", "\n": "\\n", ".": "\\.", "+": "\\+", "*": "\\*", "(": "\\L", ")": "\\R", "|": "\\O", "/": "\\/","-": "\\-"}
store_str = []
ptr = [0]


def __main__():
    file = open("example.txt", "r")
    lines = file.readlines()
    store_str.append("".join(lines))
    file.close()
    cur_state = start_state
    n = next_char()
    cur_read = n
    while n != "$":
        if n in change_map.keys():
            n = change_map[n]
        if cur_state not in path_map.keys() or n not in path_map[cur_state].keys():
            if cur_state in end_and_action.keys():
                if end_and_action[cur_state] != "{}":
                    if end_and_action[cur_state] in ["{ID}", "{NUM}"]:
                        print(end_and_action[cur_state][1:-1] + "," + cur_read[:-1])
                    else:
                        print(end_and_action[cur_state][1:-1])
                push_back()
                cur_state = start_state
                cur_read = ""
            else:
                print("error " + cur_read[:-1])
                return
        else:
            cur_state = path_map[cur_state][n]
        n = next_char()
        cur_read += n
    if cur_state not in path_map.keys() or n not in path_map[cur_state].keys():
        if cur_state in end_and_action.keys():
            if end_and_action[cur_state] != "{}":
                if end_and_action[cur_state] in ["{ID}", "{NUM}"]:
                    print(end_and_action[cur_state][1:-1] + "," + cur_read[:-1])
                else:
                    print(end_and_action[cur_state][1:-1])
            push_back()
        else:
            print("error " + cur_read[:-1])
            return


def next_char():
    if ptr[0] == len(store_str[0]):
        return "$"
    result = store_str[0][ptr[0]]
    ptr[0] += 1
    return result


def push_back():
    ptr[0] -= 1


__main__()