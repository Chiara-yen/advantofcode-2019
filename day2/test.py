import modules.intcode_computer as cpu

# answer should be 2,0,0,0,99
# list = [1, 0, 0, 0, 99]

# answer should be 2,3,0,6,99
# list = [2, 3, 0, 3, 99]

# answer should be 2,4,4,5,99,9801
# list = [2, 4, 4, 5, 99, 0]

# answer should be 30,1,1,4,2,5,6,0,99
list = [1, 1, 1, 4, 99, 5, 6, 0, 99]

separator = ','
ans = cpu.get_final_string(list, separator)

print('Answer = ', ans)
