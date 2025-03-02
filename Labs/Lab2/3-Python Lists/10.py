# Join Lists

# + method
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print("1. ", list3)

# append method
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print("2. ", list1)

# extend method
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print("3. ", list1)
