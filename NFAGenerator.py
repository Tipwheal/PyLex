import NFA

store = [1]
preserve = ['\\t', '\\n', '\w', 'A-Z', 'a-z', '0-9', "\+", "\."]
suf_list = ["*", "?", "+"]
convert = {
    "a-z": "a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z",
    "A-Z": "A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z",
    "0-9": "0|1|2|3|4|5|6|7|8|9"
}


def generate(pre_map, handle_list):
    for handle_str in handle_list:
        if handle_str.startswith("{"):
            handle_str = pre_map[handle_str[1:-1]]
        end_state = str(store[0])
        store[0] += 1
        add_path("x", end_state, handle_str, is_end=True)


def add_path(start, end, path, is_end=False):
    path = remove_outer_o(path)
    if is_end and end not in NFA.end_set:
        NFA.end_set.append(end)
    if not is_end and end not in NFA.not_end_set:
        NFA.not_end_set.append(end)
    if is_base_path(path):
        if path in convert.keys():
            add_path(start, end, convert[path], is_end)
        else:
            if path not in NFA.input_set:
                NFA.input_set.append(path)
            a_list = [start, path, end]
            if a_list not in NFA.path_list:
                NFA.path_list.append(a_list)
    elif is_append_path(path):
        if path[-1] == "*":
            mid = str(store[0])
            store[0] += 1
            add_path(start, mid, "ε")
            add_path(mid, mid, path[:-1])
            add_path(mid, end, "ε", is_end)
        elif path[-1] == "?":
            add_path(start, end, path[:-1], is_end)
            add_path(start, end, "ε", is_end)
        elif path[-1] == "+":
            mid = str(store[0])
            store[0] += 1
            add_path(start, mid, path[:-1])
            add_path(mid, end, path[:-1] + "*", is_end)
    elif is_or_path(path):
        d_list = divide_or_path(path)
        for p in d_list:
            add_path(start, end, p, is_end)
    elif is_dividable(path):
        d_list = divide_path(path)
        for i in range(len(d_list)):
            if i == 0:
                cur_x = start
                cur_y = str(store[0])
                store[0] += 1
            elif i == len(d_list) - 1:
                cur_x = cur_y
                cur_y = end
            else:
                cur_x = cur_y
                cur_y = str(store[0])
                store[0] += 1
            if cur_y == end:
                add_path(cur_x, cur_y, d_list[i], is_end)
            else:
                add_path(cur_x, cur_y, d_list[i])
    elif is_o_append(path):
        if path[-1] == "*":
            mid = str(store[0])
            store[0] += 1
            add_path(start, mid, "ε")
            add_path(mid, mid, path[:-1])
            add_path(mid, end, "ε", is_end)
        elif path[-1] == "?":
            add_path(start, end, path[:-1], is_end)
            add_path(start, end, "ε", is_end)
        elif path[-1] == "+":
            mid = str(store[0])
            store[0] += 1
            add_path(start, mid, path[:-1])
            add_path(mid, end, path[:-1] + "*", is_end)


def is_dividable(line):
    cur_left = 0
    num = 0
    for s in line:
        if cur_left == 0 and s not in suf_list:
            num += 1
        if s == "(":
            cur_left += 1
        elif s == ")":
            cur_left -= 1
    return num > 1


def divide_path(line):
    cur_read = ""
    result = []
    cur_left = 0
    for i in range(len(line) - 1):
        s = line[i]
        if s == "(":
            cur_left += 1
            cur_read += s
        elif s == ")":
            cur_left -= 1
            cur_read += s
        else:
            cur_read += s
        if cur_left == 0 and s != "\\":
            if line[i+1] not in suf_list:
                result.append(cur_read)
                cur_read = ""
    cur_read += line[-1]
    result.append(cur_read)
    return result


def is_or_path(line):
    cur_left = 0
    for i in range(len(line)):
        s = line[i]
        if s == "(":
            cur_left += 1
        elif s == ")":
            cur_left -= 1
        elif cur_left == 0 and s == "|":
            return True
    return False


def divide_or_path(line):
    cur_left = 0
    cur_read = ""
    result_list = []
    for i in range(len(line)):
        s = line[i]
        if s == "(":
            cur_left += 1
            cur_read += s
        elif s == ")":
            cur_left -= 1
            cur_read += s
        elif (cur_left == 0 and s == "|") or i == len(line) - 1:
            if i == len(line) - 1:
                cur_read += s
            result_list.append(cur_read)
            cur_read = ""
        else:
            cur_read += s
    return result_list


def is_o_append(line):
    if line[-1] in ["*", "?", "+"]:
        if line[0] == "(" and line[-2] == ")":
            return True
    return False


def remove_outer_o(line):
    while len(line) > 2 and line[0] == "(" and line[-1] == ")" and not is_or_path(line):
        line = line[1:-1]
    return line


def is_base_path(line):
    if "(" in line or ")" in line:
        return False
    if line in preserve:
        return True
    if "*" in line or "?" in line or "+" in line:
        return False
    if len(line) >= 2:
        return False
    return True


def is_append_path(line):
    if is_base_path(line[:-1]) and line[-1] in ["*", "?", "+"]:
        return True
    return False
