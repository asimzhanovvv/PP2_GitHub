# Python Variables - Assign Multiple Values

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z, '\n')

x = y = z = "Orange" # x = "Orange", y = "Orange", z = "Orange"
print(x + " " + y + " " + z + ' - x, y and z are same', '\n')

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)    # apple
print(y)    # banana
print(z)    # cherry
