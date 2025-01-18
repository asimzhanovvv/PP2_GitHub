# Python - Format - Strings

# F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt, "\n")

# Modifiers
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt, "\n")

# Multiple Modifiers
quantity = 3
itemno = 567
price = 49
myorder = f"I want {quantity} pieces of item number {itemno} for {price:.2f} dollars."
print(myorder, "\n")

# Python codes in f-strings
price = 59
txt = f"The price is {20 * price} dollars"
print(txt) # The price is 1180 dollars