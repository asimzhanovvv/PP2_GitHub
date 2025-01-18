# Python Numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z), '\n')

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a,' - ',type(a))
print(b, ' - ' ,type(b))
print(c, ' - ' ,type(c), '\n')

import random # import the random module

print('random number - ',random.randrange(1, 10)) # generate a random number between 1 and 9
