import re
# with open('text.txt') as file:
#     text = file.read()

text = "HeLLoWorldThisIsPython"

pattern = '[A-Z][^A-Z]*'
result = re.findall(pattern, text)

for i in result:
    print(i, end=' ')