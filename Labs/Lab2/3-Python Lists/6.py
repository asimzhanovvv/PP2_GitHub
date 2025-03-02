# Loops List

# For Loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
print()

# While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]