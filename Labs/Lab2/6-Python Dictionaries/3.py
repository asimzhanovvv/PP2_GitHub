# Change Dictionary Items

thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print("1. ", thisdict)

thisdict.update({"year": 2020}) # Update method
print("2. ", thisdict) 