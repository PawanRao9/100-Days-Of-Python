# OS MODULE ........

import os

if(not os.path.exists("data")): # we can create the files with in directory
   os.mkdir("data")

# for i in range(0,100):
#     os.mkdir(f"data/file{i+1}")

# for i in range (0,100):           
#     os.rename(f"data/file{i+1}",f"data/day {i+1}")

# for i in range (0,100):
#     os.rename(f"data/day{i+1}",f"data/day {i+1}")    # this way we can modify our file names to include the day number in the name


folders = os.listdir("data")  # this will return a list of all the files and folders in the directory
print(folders)


for folder in folders:
   print(folder)


for folder in folders:  # this will print the name of each folder in the directory and shows the number of files in each folder
   print(folder)
   print(os.listdir(f"data/{folder}"))   


print("you are in the directory :",os.getcwd())   # this will print the current directory that you are in or the path of the directory that you are in

os.chdir('/Users') # this will change the directory to the users directory and you can use "os.getcwd()" to check the current directory
print(os.getcwd())


''' 1. File & Directory Operations
os.getcwd() – Get current working directory.

os.chdir(path) – Change current working directory.

os.listdir(path='.') – List all files/folders in a directory.

os.mkdir(path) – Create a new directory.

os.makedirs(path) – Create nested directories.

os.remove(path) – Delete a file.

os.rmdir(path) – Remove a directory.

os.rename(src, dst) – Rename/move a file or directory.

os.path.exists(path) – Check if a path exists.

os.path.isfile(path) / os.path.isdir(path) – Check if it’s a file or directory.'''


