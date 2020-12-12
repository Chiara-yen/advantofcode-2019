import package.intcode_computer as cpu

# answer should be 2,0,0,0,99
q1 = [1, 0, 0, 0, 99]
print('q1: ', q1)
print('q1 answer = ', cpu.get_final_list(q1))
print('q1 answer should be = 2,0,0,0,99 \n')

# answer should be 2,3,0,6,99
q2 = [2, 3, 0, 3, 99]
print('q2: ', q2)
print('q2 answer = ', cpu.get_final_list(q2))
print('q2 answer should be = 2,3,0,6,99 \n')

# answer should be 2,4,4,5,99,9801
q3 = [2, 4, 4, 5, 99, 0]
print('q3: ', q3)
print('q3 answer = ', cpu.get_final_list(q3))
print('q3 answer should be = 2,4,4,5,99,9801 \n')

# answer should be 30,1,1,4,2,5,6,0,99
q4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]
print('q4: ', q4)
print('q4 answer = ', cpu.get_final_list(q4))
print('q4 answer should be = 30,1,1,4,2,5,6,0,99 \n')

# answer should be 1101,100,-1,4,99
q5 = [1101, 100, -1, 4, 0]
print('q5: ', q5)
print('q5 answer = ', cpu.get_final_list(q5))
print('q5 answer should be = 1101,100,-1,4,99 \n')
