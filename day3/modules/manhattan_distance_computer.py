import math


def opration_to_coordinate(origin, opration):
    [x, y] = origin
    direct = opration[:1]
    steps = int(opration[1:])
    if direct == 'R':
        x += steps
    if direct == 'L':
        x -= steps
    if direct == 'U':
        y += steps
    if direct == 'D':
        y -= steps
    return (x, y)


def split_string(s, separator):
    return s.split(separator)


def get_points_between(a, b):
    [ax, ay] = a
    [bx, by] = b

    x_direct = 0
    if bx - ax > 0:
        x_direct = +1
    elif bx - ax < 0:
        x_direct = -1

    y_direct = 0
    if by - ay > 0:
        y_direct = +1
    elif by - ay < 0:
        y_direct = -1

    result = []
    point = (ax, ay)
    while True:
        next_point_x = point[0] + x_direct
        next_point_y = point[1] + y_direct
        next_point = (next_point_x, next_point_y)
        result.append(next_point)
        if next_point_x == bx and next_point_y == by:
            break
        point = next_point

    return result


def get_distance_between(a, b):
    [ax, ay] = a
    [bx, by] = b
    result = abs(ax - bx) + abs(ay - by)
    return result


def oprations_string_to_coordinate_list(s):
    l = split_string(s, ',')
    for i in range(len(l)):
        if i == 0:
            l[i] = opration_to_coordinate((0, 0), l[i])
        else:
            l[i] = opration_to_coordinate(l[i - 1], l[i])
    return l


def get_all_coordinate_points_list(l):
    result = []
    for i in range(len(l)):
        if i == 0:
            result.extend(get_points_between((0, 0), l[i]))
        else:
            result.extend(get_points_between(l[i - 1], l[i]))
    return result


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def get_all_cross_points(wire1, wire2):
    l1 = get_all_coordinate_points_list(
        oprations_string_to_coordinate_list(wire1))
    l2 = get_all_coordinate_points_list(
        oprations_string_to_coordinate_list(wire2))
    return intersection(l1, l2)


def conver_cross_points_to_distances(l):
    def get_distance_between_origin(
        coord): return get_distance_between((0, 0), coord)
    return map(get_distance_between_origin, l)
