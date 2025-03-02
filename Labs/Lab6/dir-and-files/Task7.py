task5 = open(r'Lab6\dir-and-files\Task5.py', 'r')
content = task5.read()
# with open(r'Lab6\dir-and-files\Task5.py', 'r') as source_file:
#     content = source_file.read()



task7 = open(r'Lab6\dir-and-files\Task7.txt', 'w')
task7.write(content)
# with open(r'Lab6\dir-and-files\Task7.txt', 'w') as target_file:
#     target_file.write(content)

print("Exelent! Task5.py is copied to Task7.txt")