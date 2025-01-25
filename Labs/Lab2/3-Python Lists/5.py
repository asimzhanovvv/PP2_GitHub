# Remove list items

# remove() method
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") # removes the first occurence of the item
print("1. ",thislist)

# pop() method
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # removes the item at the specified index
print("2. ",thislist)

# del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0] # removes the item at the specified index
print("3. ",thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print("4. ", thislist) # clears the list
del thislist # deletes the list