# Break
print("Break")
i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i += 1
print()


# Continue
print("Continue")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print()


# Else
print("Else")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")