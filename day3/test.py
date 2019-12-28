import modules.manhattan_distance_computer as cpu

# closet cross point (3,3) therefore, its distance is 3 + 3 = 6
# min distance should be 6
# best steps should be 30
w1 = 'R8,U5,L5,D3'
w2 = 'U7,R6,D4,L4'

# min distance should be 159
# best steps should be 610
w3 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
w4 = 'U62,R66,U55,R34,D71,R55,D58,R83'

# min distance should be 135
# best steps should be 410
w5 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
w6 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

l1 = cpu.get_all_coordinate_points_list(
    cpu.oprations_string_to_coordinate_list(w5))
l2 = cpu.get_all_coordinate_points_list(
    cpu.oprations_string_to_coordinate_list(w6))
cross_points = cpu.intersection(l1, l2)
d = cpu.conver_cross_points_to_distances(cross_points)
best_steps = cpu.get_best_steps_between_coordinate_points_lists(l1, l2)

print('cross_points =', cross_points)
print('min(d) =', min(d))
print('best_steps =', best_steps)
