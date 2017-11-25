import ReadLex
import DFAO


def write(path):
    file = open(path, "w+")
    file.write(get_info())
    file.close()


def get_info():
    result = ""
    result += "\n\n"
    for def_symbol in ReadLex.token_list:
        result += def_symbol + " = \"" + def_symbol + "\"\n"
    result += "input_list = " + str(DFAO.input_list) + "\n"
    result += "start_state = \"" + str(DFAO.start_state) + "\"\n"
    result += "not_end_list = " + str(DFAO.not_end_list) + "\n"
    result += "end_and_action = " + str(DFAO.end_and_action) + "\n"
    result += "path_map = " + str(DFAO.path_map) + "\n"
    result += "change_map = {\" \": \"\\\\w\", \"\\n\": \"\\\\n\", \".\": \"\\\\.\", \"+\": \"\\\\+\", " \
              "\"*\": \"\\\\*\", \"(\": \"\\\\L\", \")\": \"\\\\R\", \"|\": \"\\\\O\", \"/\": \"\\\\/\"," \
              "\"-\": \"\\\\-\"}\n"
    result += "store_str = []\n"
    result += "ptr = [0]\n"
    result += "\n\n"
    result += "def __main__():\n" \
              "    file = open(\"example.txt\", \"r\")\n" \
              "    lines = file.readlines()\n" \
              "    store_str.append(\"\".join(lines))\n" \
              "    file.close()\n" \
              "    cur_state = start_state\n" \
              "    n = next_char()\n" \
              "    cur_read = n\n" \
              "    while n != \"$\":\n" \
              "        if n in change_map.keys():\n" \
              "            n = change_map[n]\n" \
              "        if cur_state not in path_map.keys() or n not in path_map[cur_state].keys():\n" \
              "            if cur_state in end_and_action.keys():\n" \
              "                if end_and_action[cur_state] != \"{}\":\n" \
              "                    if end_and_action[cur_state] in [\"{ID}\", \"{NUM}\"]:\n" \
              "                        print(end_and_action[cur_state][1:-1] + \",\" + cur_read[:-1])\n" \
              "                    else:\n" \
              "                        print(end_and_action[cur_state][1:-1])\n" \
              "                push_back()\n" \
              "                cur_state = start_state\n" \
              "                cur_read = \"\"\n" \
              "            else:\n" \
              "                print(\"error \" + cur_read[:-1])\n" \
              "                return\n" \
              "        else:\n" \
              "            cur_state = path_map[cur_state][n]\n" \
              "        n = next_char()\n" \
              "        cur_read += n\n" \
              "    if cur_state not in path_map.keys() or n not in path_map[cur_state].keys():\n" \
              "        if cur_state in end_and_action.keys():\n" \
              "            if end_and_action[cur_state] != \"{}\":\n" \
              "                if end_and_action[cur_state] in [\"{ID}\", \"{NUM}\"]:\n" \
              "                    print(end_and_action[cur_state][1:-1] + \",\" + cur_read[:-1])\n" \
              "                else:\n" \
              "                    print(end_and_action[cur_state][1:-1])\n" \
              "            push_back()\n" \
              "        else:\n" \
              "            print(\"error \" + cur_read[:-1])\n" \
              "            return\n" \
              "\n\n" \
              "def next_char():\n" \
              "    if ptr[0] == len(store_str[0]):\n" \
              "        return \"$\"\n" \
              "    result = store_str[0][ptr[0]]\n" \
              "    ptr[0] += 1\n" \
              "    return result\n" \
              "\n\n" \
              "def push_back():\n" \
              "    ptr[0] -= 1\n" \
              "\n\n" \
              "__main__()"
    return result
