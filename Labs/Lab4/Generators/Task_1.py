N = int(input("Input N: "))

def square(N):
    for i in range(1, N+1):
        yield i**2

for i in square(N):
    print(i)