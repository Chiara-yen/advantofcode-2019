import modules.password_computer as cpu

password_range = '000000-999999'

# meets criteria
a = '111111'
print(a, 'should be true = ', cpu.validate(a, password_range))

# does not meet criteria
b = '223450'
print(b, 'should be false = ', cpu.validate(b, password_range))

# does not meet criteria
c = '123789'
print(c, 'should be false = ', cpu.validate(c, password_range))

# meets criteria
d = '112233'
print(d, 'should be true = ', cpu.validate(d, password_range))

# does not meet criteria
e = '123444'
print(e, 'should be false = ', cpu.validate(e, password_range))

# meets criteria
f = '111122'
print(f, 'should be true = ', cpu.validate(f, password_range))

# meets criteria
g = '777889'
print(g, 'should be true = ', cpu.validate(g, password_range))

# meet criteria
h = '556789'
print(h, 'should be true = ', cpu.validate(h, password_range))
