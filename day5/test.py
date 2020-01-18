import package.intcode_computer as cpu

# answer should be 2,0,0,0,99
q1 = [1, 0, 0, 0, 99]

# answer should be 2,3,0,6,99
q2 = [2, 3, 0, 3, 99]

# answer should be 2,4,4,5,99,9801
q3 = [2, 4, 4, 5, 99, 0]

# answer should be 30,1,1,4,2,5,6,0,99
q4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]

separator = ','
l1 = cpu.get_final_list(q1)
l2 = cpu.get_final_list(q2)
l3 = cpu.get_final_list(q3)
l4 = cpu.get_final_list(q4)

print('q1: ', q1, ' The answer = ', l1)
print('q1 answer should be = 2,0,0,0,99')

print('q2: ', q2, ' The answer = ', l2)
print('q2 answer should be = 2,3,0,6,99')

print('q3: ', q3, ' The answer = ', l3)
print('q3 answer should be = 2,4,4,5,99,9801')

print('q4: ', q4, ' The answer = ', l4)
print('q4 answer should be = 30,1,1,4,2,5,6,0,99')
