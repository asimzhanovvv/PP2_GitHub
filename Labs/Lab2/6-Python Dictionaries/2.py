# Access Dictionary Items

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print("1. ", x)
x = thisdict.get("model")
print("2. ", x)

# Get Keys
x = thisdict.keys()
print("3. ", x)

# Get Values
x = thisdict.values()
print("4. ", x)

# Get Items
x = thisdict.items()
print("5. ", x)
