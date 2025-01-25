# Remove Item

# remove() method 
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print("1. ", thisset)

# discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print("2. ", thisset)

# pop() method (random)
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print("3. ", x) # removed item
print("4. ", thisset) # the set after removal

# clear() method
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print("5. ", thisset) # empty set
del thisset # del keyword
