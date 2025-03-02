# Add list items


# append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print("1. ",thislist)

# insert() method
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print("2. ", thislist)

# extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("3. ", thislist)

# Add any iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print("4. ", thislist)