import os

def path_info(path):
    print("------------------------------------------------------------------------------")
    if os.access(path, os.F_OK):
        
        if os.path.isfile(path):
            print("File name:", os.path.basename(path))
        else: 
            print("This is not a file (probably a directory)")

        print("Directory:", os.path.dirname(path))

    else:
        print("Path does not exist")



path = r"C:\Users\Asus Tuf\Desktop\Files\PP2_Github\Labs\Lab6\dir-and-files\Task1.py" #File
path_info(path)

path = r"C:\Users\Asus Tuf\Desktop\Files\PP2_Github\Labs\Lab6\dir-and-files" #Directory
path_info(path)

path = r"C:\Users\Asus Tuf\Desktop\Files\PP2_Github\Labs\Lab6\something" #Does not exist    
path_info(path)
print("------------------------------------------------------------------------------")