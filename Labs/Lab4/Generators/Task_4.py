a = int(input("Input a: "))
b = int(input("Input b: "))

def squares(a,b):
    for i in range(a,b+1):
        yield i**2

for i in squares(a,b):
    print(i)