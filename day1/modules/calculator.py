import math


def mass2fuel(m):
    f = math.floor(m/3 - 2)
    result = f if f > 0 else 0
    return result


def getFuel(m):
    result = mass2fuel(m)
    if mass2fuel(result) > 0:
        result += getFuel(result)

    return result


def getTotalFuel(list):
    total = 0.0
    for i in list:
        total += getFuel(i)

    return total
