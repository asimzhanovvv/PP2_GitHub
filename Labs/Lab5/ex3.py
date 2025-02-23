import re
with open('text.txt') as file:
    text = file.read()
# The price of the item_is $19.99, but with a_ discount, it’s now $14.99. 

pattern = '[a-z]_[a-z]'

result = re.findall(pattern, text)

print(result)