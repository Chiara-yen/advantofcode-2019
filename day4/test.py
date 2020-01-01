import modules.password_computer as cpu

password_range = '000000-864247'

# meets criteria
a = '111111'
print('a isValid = ', cpu.validate(a, password_range))

# does not meet criteria
b = '223450'
print('b isValid = ', cpu.validate(b, password_range))

# does not meet criteria
c = '123789'
print('c isValid = ', cpu.validate(c, password_range))
