import math


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def handle_opcode(opcode, params, list):
    if opcode is 99:
        return list
    elif opcode is 1:
        index0 = params[0]
        index1 = params[1]
        position = params[2]
        list[position] = add(list[index0], list[index1])
    elif opcode is 2:
        index0 = params[0]
        index1 = params[1]
        position = params[2]
        list[position] = multiply(list[index0], list[index1])
    elif opcode is 3:
        value = params[0]
        position = params[0]
        list[position] = value
    elif opcode is 4:
        position = params[0]
        return list[position]
    else:
        raise TypeError('unknow opcode =', opcode)
    return list


def get_final_list(list):
    params = 0
    pointer = 0
    while pointer < len(list):
        opcode = list[pointer]
        if opcode is 99:
            return list
        elif opcode is 1 or opcode is 2:
            params = 3
        elif opcode is 3 or opcode is 4:
            params = 1

        end = (pointer + 1) + params
        params = list[pointer + 1:end]
        result = handle_opcode(opcode, params, list)
        if opcode is 4:
            return result
        pointer += end
    return list
