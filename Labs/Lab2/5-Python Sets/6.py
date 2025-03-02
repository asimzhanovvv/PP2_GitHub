# Join Sets



# Union/update method 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2 # set1.union(set2)
print("1. ", set3)

set1.update(set2)   
print("   ", set1)



# Intersection() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2 # set1.intersection(set2)
print("2. ", set3)

set1.intersection_update(set2)
print("   ", set1)



# Difference() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"} 
set3 = set1 - set2 # set1.difference(set2)
print("3. ", set3)

set1.difference_update(set2)
print("   ", set1)



# Symmetric Difference() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2 # set1.symmetric_difference(set2)
print("4. ", set3)

set1.symmetric_difference_update(set2)
print("   ", set1)