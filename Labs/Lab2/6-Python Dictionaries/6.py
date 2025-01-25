# Loop Dictionaries

thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in thisdict:
    print(x) # keys
print()

for x in thisdict:
    print(thisdict[x]) # values
print()

for x in thisdict.keys(): # another way to get keys
    print(x)
print()

for x in thisdict.values(): # another way to get values
    print(x)
print()

for x, y in thisdict.items():
  print(x, y) # key and value