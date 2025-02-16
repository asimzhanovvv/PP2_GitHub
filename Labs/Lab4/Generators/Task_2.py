n = int(input("Input n: "))

def even(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

for i in even(n):
    if i == 0: print(i, end="")
    else: print(",", i, end="")