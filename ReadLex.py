token_list = []
pre_map = {}
use_map = {}
append_func = []


def read_lex(path):
    lex_file = open(path, "r")
    lines = lex_file.readlines()
    lex_file.close()
    get_tokens(lines)
    get_pre_def(lines)
    get_useful(lines)
    get_function(lines)


def get_function(lines):
    start = False
    for line in lines:
        if line.startswith("%% func"):
            start = True
            continue
        if start:
            append_func.append(line[:-1])


def get_useful(lines):
    useful_mode = False
    for line in lines:
        if line.startswith("%% action"):
            useful_mode = True
            continue
        if line.startswith("%% func"):
            break
        if useful_mode:
            line = line.strip()
            if line != "":
                spl = str(line).split(" ")
                use_map[spl[0]] = "".join(spl[1:]).strip()


def get_pre_def(lines):
    re_mode = False
    for line in lines:
        if line.startswith("%% re def"):
            re_mode = True
            continue
        if line.startswith("%% action"):
            break
        if re_mode:
            line = line.strip()
            if line != "" and not line.startswith("/*"):
                spl = str(line).split(" ")
                pre_map[spl[0]] = "".join(spl[1:]).strip()


def get_tokens(lines):
    token_mode = False
    for line in lines:
        if line.startswith("%% token"):
            token_mode = True
            continue
        if line.startswith("%% re def"):
            break
        if token_mode:
            tokens = line.strip().split(",")
            for token in tokens:
                token = token.strip()
                if token != "":
                    token_list.append(token)
