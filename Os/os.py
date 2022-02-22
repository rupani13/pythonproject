# all os Program
# Handling the Current Working Directory
import os
cwd = os.getcwd()
print("Current working directory:", cwd)

# Changing the Current working directory


def new_path():
    print("current working directory path:", os.getcwd())

new_path()
os.chdir('../')
new_path()

# Listing out Files and Directories with Python
path = "/"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# Remove directory
'''direct = 'All_Book'
location = "C:/Users/dell/PycharmProjects/PythonProject_SRN/"
path = os.path.join(location, direct)
os.rmdir(path)'''


# read or written depending on whether the mode
fd = "Book.txt"
file = open(fd, 'w')
file.write("The_Book")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
file = os.popen(fd, 'w')

# whether a file exists or not by passing the name of the file as a parameter

File_name = os.path.exists("Book.txt")
print(File_name)

# Find the size of path
size = os.path.getsize("Book.txt")
print("Size of the file is", size, " bytes.")


# Using OS create a new directory
direct = 'All_Book'
Parent_dir = '//'
path = os.path.join(Parent_dir, direct)
os.mkdir(path)
print("Directory '% s' created", direct)
directory = "Books"
parent_dir = "//"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '% s' created", directory)

