import math
import re

# modes
POSITION_MODE = 0
IMMEDIATE_MODE = 1

# opcodes
OPCODE_HALT = 99
OPCODE_ADD = 1
OPCODE_MULTIPLY = 2
OPCODE_INPUT = 3
OPCODE_OUTPUT = 4


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def handle_opcode_with_modes(num):
    opcode = num % 100
    modes = '0'

    if num > 100:
        # print('!!!!!', num)
        modes = str((num - opcode) % 100)

    # print('!!!!!', modes)
    return [opcode, modes]


def handle_instruction(opcode, params, list):
    print('handle_instruction/ opcode:', opcode)
    print('handle_instruction/ params:', params)
    print('handle_instruction/ list:', list)

    if opcode is OPCODE_HALT:
        return list

    elif opcode is OPCODE_ADD:
        index0 = params[0]
        index1 = params[1]
        position = params[2]
        list[position] = add(list[index0], list[index1])

    elif opcode is OPCODE_MULTIPLY:
        index0 = params[0]
        index1 = params[1]
        position = params[2]
        list[position] = multiply(list[index0], list[index1])

    elif opcode is OPCODE_INPUT:
        value = params[0]
        position = params[0]
        list[position] = value

    elif opcode is OPCODE_OUTPUT:
        position = params[0]
        return list[position]

    else:
        raise TypeError('unknow opcode =', opcode)
    return list


def get_final_list(list):
    params = 0
    pointer = 0
    while pointer < len(list):
        opcode_with_modes = list[pointer]
        [opcode, modes] = handle_opcode_with_modes(opcode_with_modes)
        print('opcode: ', opcode, ' mode: ', modes)

        if opcode is OPCODE_HALT:
            return list
        elif opcode is OPCODE_ADD or opcode is OPCODE_MULTIPLY:
            params = 3
        elif opcode is OPCODE_INPUT or opcode is OPCODE_OUTPUT:
            params = 1

        end = (pointer + 1) + params
        params = list[pointer + 1:end]
        result = handle_instruction(opcode, params, list)
        if opcode is OPCODE_OUTPUT:
            return result
        pointer += end

        if pointer > 20:
            raise Error('too many iter')
            return None

    return list
