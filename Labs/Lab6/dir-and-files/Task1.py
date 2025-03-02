import os

path = r"C:\Users\Asus Tuf\Desktop\Files\PP2_Github\Labs\Lab6"

contents_of_the_path = os.scandir(path)
files = []
dirs = []

for content in contents_of_the_path:
    if content.is_file():
        files.append(content.name)
    elif content.is_dir():
        dirs.append(content.name)

print(f"Files: {files}")
print(f"Dirs: {dirs}")
print(f"Total: {files + dirs}")