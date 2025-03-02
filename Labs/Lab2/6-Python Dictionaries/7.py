# Copy Dictionaries

# copy() method
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict1 = thisdict.copy()
print("1. ", mydict1)

# dict() method
mydict2 = dict(thisdict)
print("2. ", mydict2)