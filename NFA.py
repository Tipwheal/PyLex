start_state = "x"
not_end_set = ["x"]
end_set = []
input_set = []
path_list = []


def get_next(start_set, path):
    result = []
    for all_path in path_list:
        if all_path[0] in start_set and all_path[1] == path and all_path[2] not in result:
            result.append(all_path[2])
    return result