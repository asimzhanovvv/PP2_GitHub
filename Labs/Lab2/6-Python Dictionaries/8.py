# Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print("1. ", myfamily)
print("2. ", myfamily["child2"]["name"])
print()

for x, y in myfamily.items():
    print(x)
    
    for z in y:
        print(z + ':', y[z])
    print()