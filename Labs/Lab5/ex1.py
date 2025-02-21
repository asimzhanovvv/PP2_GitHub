import re
with open('text.txt') as file:
    text = file.read()

pattern = 'ab*'

result = re.findall(pattern, text)

print(result)