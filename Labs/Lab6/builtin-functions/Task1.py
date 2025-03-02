import functools

numbers = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]

result = functools.reduce(lambda x, y: x * y , numbers)

print (numbers)
print(result)
