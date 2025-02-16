n = int(input("Input n: "))

def tozero(n):
    for i in range(n,-1,-1):
        yield i

for i in tozero(n):
    print(i, end=" ")