# Break 
print("Break")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
print()


# Continue
print("Continue")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
print()


# Range
print("Range")
for x in range(1,6,2):
    print(x)
print()

# Else
print("Else")
for x in range(6):
    print(x)
else:
    print("Finally finished!")
print()


# Pass
print("Pass")
for x in [0, 1, 2]:
    pass