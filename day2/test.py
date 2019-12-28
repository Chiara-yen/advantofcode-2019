import modules.intcode_computer as cpu

# answer should be 2,0,0,0,99
# q = [1, 0, 0, 0, 99]

# answer should be 2,3,0,6,99
# q = [2, 3, 0, 3, 99]

# answer should be 2,4,4,5,99,9801
# q = [2, 4, 4, 5, 99, 0]

# answer should be 30,1,1,4,2,5,6,0,99
q = [1, 1, 1, 4, 99, 5, 6, 0, 99]

separator = ','
instruction = 4
l = cpu.get_final_list(q, instruction)
string_list = list(map(str, l))
ans = separator.join(string_list)

print('Answer = ', ans)
