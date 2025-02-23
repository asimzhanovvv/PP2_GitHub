import re
with open('text.txt') as file:
    text = file.read()

pattern = '[\s,.]'

result = re.sub(pattern, ':', text)
print(result)