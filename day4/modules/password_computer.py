passward_length = 6
range_separator = '-'


def is_six_digit(passward):
    return True if len(passward) == passward_length else False


def is_in_range(passward, range):
    [min, max] = range.split(range_separator)
    if int(min) < int(passward) and int(passward) < int(max):
        return True
    return False


def has_adjacent_digits(passward):
    temp = None
    digits_counts = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
    }
    for i in range(len(passward)):
        digit = passward[i]
        digits_counts[digit] += 1
    counts = digits_counts.values()

    if 5 in counts or 6 in counts:
        return False

    if 2 in counts:
        return True

    return False


def has_increase_digits(passward):
    temp = 0
    for i in range(len(passward)):
        if passward[i] < temp:
            return False
        temp = passward[i]
    return True


def validate(passward, range):
    if not is_six_digit(passward):
        return False

    if not is_in_range(passward, range):
        return False

    if not has_increase_digits(passward):
        return False

    if not has_adjacent_digits(passward):
        return False

    return True


def get_possible_passwords(range):
    [min, max] = range.split(range_separator)
    result = []
    current = int(min)
    while current <= int(max):
        is_valid = validate(str(current), range)
        if is_valid:
            result.append(str(current))
        current += 1
    return result
