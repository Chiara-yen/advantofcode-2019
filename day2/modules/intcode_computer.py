import math


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def get_action(type):
    if type is 1:
        return add
    elif type is 2:
        return multiply
    elif type is 99:
        return None
    raise TypeError('unknow type =', type)


def handle_opcode(group, list, instruction):
    if len(group) < instruction:
        return None

    [type, index0, index1, position] = group
    action = get_action(type)

    if action is None:
        return None

    list[position] = action(list[index0], list[index1])
    return list


def get_final_string(l, separator, instruction):
    steps = math.floor(len(l) / instruction)
    start = 0
    while steps > 0:
        end = start + instruction
        group = l[start:end]
        result = handle_opcode(group, l, instruction)
        if result is None:
            break
        start += instruction
    string_list = list(map(str, l))
    return separator.join(string_list)
