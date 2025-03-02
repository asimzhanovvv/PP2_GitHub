import os
path = r"C:\Users\Asus Tuf\Desktop\Files\PP2_Github\Labs\Lab6\dir-and-files\Task6\\"


for i in range(1,27):
    f = f'{path}{chr(i+64)}.txt'
    if os.path.exists(f):
        os.remove(f)

print('Files deleted successfully !')