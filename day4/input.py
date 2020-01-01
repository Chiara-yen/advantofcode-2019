
import modules.password_computer as cpu

'''
Password criteria:

1. It is a six-digit number.
2. The value is within the range given in your puzzle input.
3. Two adjacent digits are the same (like 22 in 122345).
4. Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

'''

password_range = '402328-864247'

list = cpu.get_possible_passwords(password_range)
print('ans =', len(list))
