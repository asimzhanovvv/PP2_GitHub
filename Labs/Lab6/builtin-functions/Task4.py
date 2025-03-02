import time

a = int(input())
b = int(input())
time.sleep(b/1000)

c = pow(a, 0.5)

print(f"Square root of {a} after {b} miliseconds is {c}")