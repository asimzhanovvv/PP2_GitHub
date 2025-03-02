import time
import os

path = r"C:\Users\Asus Tuf\Desktop\Files\PP2_Github\Labs\Lab6\dir-and-files\Task8.txt"

# Just a joke
def joke():
    time.sleep(1)
    print("[But I will create New file for you]")
    time.sleep(1)
    open(path, 'w')

    for i in range(5, 0, -1):
        print(f"[{i}]")
        time.sleep(1)

    print("[That was just a joke :)]")
    time.sleep(1)

    os.remove(path)
    print("[File was created and deleted]")   

if os.access(path, os.F_OK): # Check if file exists
    if os.access(path, os.W_OK): # Check access to delete
        os.remove(path)
        print("[File was deleted]")
    else:
        print("[You don't have access to delete this file]")
        joke()

else:
    print("[File was not found]")
    joke()