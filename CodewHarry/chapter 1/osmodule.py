import os

# specify the directory you want to list
directory_path = '/python practice'
# List and print all files and derectories in this specified path
contents = os.listdir(directory_path)
#  printeach file and directory name
for item in contents:
     print(item)

#  smaller code
     import os

# List and print all files and folders in the current directory
for item in os.listdir():
    print(item)  

