

result_map = {}


def pre_p(raw_re_map):
    copy(raw_re_map)
    remove_brace()


def copy(f_map):
    for key in f_map:
        result_map[key] = f_map[key]


def remove_brace():
    for key in result_map.keys():
        text = result_map[key]
        for inner in result_map.keys():
            if inner != key:
                text = text.replace("{" + inner + "}", result_map[inner])
        result_map[key] = text


