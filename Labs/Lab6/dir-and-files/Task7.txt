list = [1, 2, 3, 4, 5, 'Hello', 'World']

file = open(r'Lab6\dir-and-files\Task5.txt', 'w') 

file.write(str(list))
print("-----------------------------------")
print('List has been written to Task5.txt')
print("-----------------------------------")