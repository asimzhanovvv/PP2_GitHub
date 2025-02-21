import re
with open('text.txt') as file:
    text = file.read()

pattern = 'ab{2,3}'

result = re.findall(pattern, text)

print(result)