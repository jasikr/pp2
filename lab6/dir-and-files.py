#ex1
import os

for root, directories, files in os.walk(r"C:\Users\Evrika\Desktop\lab6"):
    print(root)
    for directory in directories:
        print(directory)
    for file in files:
        print(file)

#ex2
import os


def spec_path(path):
    if os.access(path, os.F_OK):
        print("The path exists")
    else:
        print("The path does not exist")

    if os.access(path, os.R_OK):
        print("The path is readable")
    else:
        print("The path is not readable")

    if os.access(path, os.W_OK):
        print("The path is writable")
    else:
        print("The path is not writable")

    if os.access(path, os.X_OK):
        print("The path is executable")
    else:
        print("The path is not executable")

#ex3
import os

path = r"C:\Users\Evrika\Desktop\lab6\hellowrld"

if os.path.exists(path) == True:
    print(f"Directory name:{os.path.dirname(path)}")
    print(f"Files in this Directory: {os.path.basename(path)}")
else:
    print("You have zero!")

#ex4
import os

with open('c:/Users/Evrika/Desktop/lab6/hellowrld.txt', 'r') as text:
    x = sum(1 for line in text)
print(x)

#ex5
import os
list = list(input().split())
with open('example file.txt', 'w') as file:
    for i in list:
        file.write(str(i) + ' ')

#ex6
import os, string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w'):
        pass

#ex7
import os
with open('example file.txt', 'r') as r:
    with open('example_file_copy.txt', 'w') as w:
        for line in r:
            w.write(line)

#ex8
import os

path="A.txt"
def delete_path(path):
    if not os.path.exists(path):
        print("Path does not exist")
        return 0
    os.remove(path)
    print("Deleted")

delete_path(path)