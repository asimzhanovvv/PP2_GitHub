import re
with open('text.txt') as file:
    text = file.read()

pattern = r'[A-Z][a-z]+'

result = re.findall(pattern, text)

print(result)