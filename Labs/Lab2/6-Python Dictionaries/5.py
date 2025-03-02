# Remove Dictionary Items



# The pop() method 
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print("1. ", thisdict)

thisdict.popitem() # The popitem() method 
print("2. ", thisdict)



# The del keyword
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

del thisdict["model"]
print("3. ", thisdict)



# The clear() method
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print("4. ", thisdict)
