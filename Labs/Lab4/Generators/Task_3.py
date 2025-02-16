n = int(input("Input n: "))

def devides(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for i in devides(n):
    print(i)