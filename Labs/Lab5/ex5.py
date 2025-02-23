import re
with open('text.txt') as file:
    text = file.read()

pattern = 'a.*b'

result = re.findall(pattern, text)

print(result)