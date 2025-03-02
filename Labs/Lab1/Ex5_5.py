# Python - Global Variables

x = "awesome" # Global variable

def myfunc():
  print("Python is " + x, '\n')

myfunc()

# Another example of global variable

def myfunc1():
  global x # This will make the variable x global
  x = "fantastic"

myfunc1()

print("Python is " + x)