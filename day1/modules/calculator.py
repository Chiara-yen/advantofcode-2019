import math


def mass2fuel(m):
    return math.floor(m/3 - 2)


def sum(x, y):
    return x + y


def getTotalFuel(list):
    total = 0.0
    extra = 0.0
    for i in list:
        total = sum(total, mass2fuel(i))

    temp = total
    print('init temp = ', temp)
    while(mass2fuel(temp) > 0):
        temp = mass2fuel(temp)
        print('in while: temp = ', temp)
        extra += temp

    print('total = ', total)
    print('extra = ', extra)
    return total + extra
