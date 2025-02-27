import os
# print(os.name)

# # Also, known as mapping object that returns dictionary of the user's environment variables.
# env_dict = os.environ  
# # print(env_dict)

# print(os.environ["TMPDIR"]) # Extracting the environment variable. if no environment variable is exist then os.environ throw an error. 

# print(os.getenv("TMPDIR")) # Can also be use the getenv to access the environment variable. It does not throw error if there is no any environment variable, it simply return the None. 

# # To get know about the current working directory. 
# print(os.getcwd())

# # To change the currently running directory. 
# print(os.chdir("/Users/netrakc/Desktop/Advance-Pythons/OS Module"))

# # Creating an directories. 
# print(os.mkdir("test_dir"))

# folder = "test_dir"
# if os.path.isdir(folder): # It will return true and delete the folder. 
#     print("Folder exist already.")
#     os.rmdir(folder)
#     print("Existed Folder deleted successfully.")
# else:
#     # If folder does not exist then create a new folder. 
#     print(os.mkdir("my_dir"))

# Creating an multiple directories at one time. 
# os.makedirs() --> will create the intermediate folders in a path if they don't already exist. 
# Or use to create an multiple subfolders.
# os.mkdir("test_dir")
# path = "/Users/netrakc/Desktop/Advance-Pythons/OS Module/test_dir/2024/02/27"
# print(os.makedirs(path))

# # os.remove() --> Used to remove certain files And os.rmdir() --> Used to remove folder.
# # Used for deleting files and directories respectively. 

# os.rename(src, dst)
# rename function will rename the file or folder. 
# print(os.rename("test_dir", "my_folder"))
'''This occurs in our current working directory. It will see an error if we try to rename a file that does not exist or that don't have permission to rename the file.'''

# os.startfile()
'''allows us to `start` a file with its associated program.Just like when we double click a PDF and it opens is Adobe Reader.'''
# print(os.startfile("....pdf"))

# os.walk()
'''os.walk() --> Gives us a way to iterate over a root level path. It means we can pass a path to this function and get access to all its sub-directories and files.Let's use one of the Python folders that we have handy to test this function with.'''

'''
import os

path = r"/content/images"

dir_list = []
file_list = []

# Implementing the os.walk()
class Walk:

    def __init__(self, dir_list, file_list, path):

        self.dir_list = dir_list
        self.file_list = file_list 
        self.path = path

    def walk_module(self, dir_list, file_list, path):

        for root, dirs, files in os.walk(self.path):
            print(root)

            for _dir in dirs:
                dir_list.append(_dir)
            
            for _file in files:
                file_list.append(_file)

walk = Walk(dir_list, file_list, path)
'''

# os.path -> sub-module of the os module that has lots of great functionality built into it. 
    # -> basename. 
    # -> dirname. 
    # -> exist. 
    # -> isdir and isfile. 
    # -> join. 
    # -> split()

# return the filename of the path. 
# base_path = "/Users/netrakc/Desktop/Advance-Pythons/OS Module/os.py"
# print("returning the filename of the path: ", os.path.basename(base_path))

# os.path.dirname. 
# return just the directory portion of the path. 
# print(os.path.dirname(r"..."))

# os.path.exists --> will tell if a path exist or not. 
# os.path.exists()

# os.path.isdir / os.path.isfile
# `isdir` & `isfile` are closely related to the exists method in that they also test for existence. 
# `isdir` -> Only checks if the path is directory or not. 
# `isfile` -> Only checks if the path is a file. 
# If we want to check if a path exist regardless of whether it is a file or a directory, then we'll want to use the exists method. 
# os.path.isfile(r"C:\Python27\Tools\pynche\ChipViewer.py") return True because this is a file. 
# os.path.isdir(r'C:\Python27\Tools\pynche\ChipViewer.py') return false because this is file not a directory. 

# os.path.join
# this gives us ability to join one or more path components together using the appropriate separator. 
# os.path.join("directory_name", "file_name.extension")
# In the above example, we joined a `directory path` and `file` together to get a fully qualified path. Note: `join` method does not check if result actually exists. 

# `os.path.split`` --> This method will split a path into a tuple that contains the directory and the file.
'''
Code:
=> os.path.split('C:\Python27\Tools\pynche\ChipViewer.py')
('directory_name', 'filename.extension')

As we see in the above code, it took the path and split in such a way that the last sub-folder became the second element of the tuple with the rest of the path in the first element. 

Code:
dirname, fname = os.path.split(r'C:\Python27\Tools\pynche\ChipViewer.py')

print(dirname)
'C:\\Python27\\Tools\\pynche'

print(fname)
'ChipViewer.py'
'''
