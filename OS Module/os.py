import os
'''
import os → Imports the os module, which provides functions to interact with the operating system.
'''
# print(os.name) # → Returns the name of the OS ('posix' for Linux/Mac, 'nt' for Windows).

# # Also, known as mapping object that returns dictionary of the user's environment variables.
# env_dict = os.environ  
# # print(env_dict)

# print(os.environ["TMPDIR"]) # Extracting the environment variable. if no environment variable is exist then os.environ throw an error. 

# print(os.getenv("TMPDIR")) # Can also be use the getenv to access the environment variable. It does not throw error if there is no any environment variable, it simply return the None. 

# # To get know about the current working directory. 
# print(os.getcwd())  # Get the current working directory

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

--------------------------------------------------------
# Processing Nested Folders using os.walk()
for root, dirs, files in os.walk(folder_path):
    for file in files: # Loop through files. 
        if file.endswith(".jpg"):
            print(os.path.join(root, file)) # Print full path of each image. 
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

'''
# Listing Files and Folders. 
# os.listdir() → Returns a list of all files and directories in the current directory.

print(os.listdir()) # List all files and folders in the current directory. 
for folders, files in os.listdir():
    print(folders, files)
'''

'''
# Creating and Removing Directories
os.mkdir("new_folder") # create a new directory. 
os.rmdir("new_folder") # removing the directory.
'''

'''
# Intermediate Level: File & Path Operations
# Handling File Paths (os.path Module).
import os 
path = os.path.join("dataset", "images") # Join paths dynamically. 
print(path) # Output: "dataset/images"

# Check if path exists. 
os.path.exists(path) → Returns True if the path exists, else False.

# Get absolute path. 
os.path.abspath(path) → Converts a relative path into an absolute path.

# Split filename into name and extension. 
os.path.splittext("image.jpg) → Splits filename into name and extension (('image', '.jpg')).
'''

'''
# 🖼 Advanced Level: Image Dataset Handling.
# 7️⃣ Iterating Over Image Files.
image_folder = "/content/images/"

# os.listdir(image_folder) → Lists all files in "images/" folder.
for file in os.listdir(image_folder): # Looping through the files in the folder. 
    # if file.endswith((".jpg", ".png")): → Checks if the file is an image.
    if file.endswith((".jpg", ".png")): # Filter only images files. 
        print("Processing: ", file) # Print filename. 

# This is useful for filtering datasets with mixed file types.
'''


'''
# Sorting and Organizing Image Datasets
# sorting and organizing image datasets. 
os.makedirs("sorted_images", exist_ok=True) # Create folder if it does not exist. 

data_path = "/content/sample_data"
sorted_images = "/content/sorted_images"

for file in os.listdir(data_path): # Loop through the dataste folder. 
    if file.endswith(".jpg"): # Check if it's an image. 
        os.rename(
            os.path.join(data_path, file), 
            os.path.join(sorted_images, file)
        )
        # Moving file. 
'''

'''
# Automation & Performance Optimization.
# Removing the Corrupted Images. 
import os
import cv2  # OpenCV for image processing

image_folder = "dataset/"
for file in os.listdir(image_folder):
    path = os.path.join(image_folder, file)
    try:
        img = cv2.imread(path)  # Try to load the image
        if img is None:  # If image is corrupted
            print("Deleting corrupted image:", file)
            os.remove(path)  # Delete it
    except Exception as e:
        print("Error:", e)

cv2.imread(path) → Loads an image. If it fails, the file might be corrupted.
os.remove(path) → Deletes corrupted images automatically.
'''

'''
# Bulk Rename Files Using Regular Expressions.
import re

for file in os.listdir("images"):
    new_name = re.sub(r"\s+", "_", file)  # Replace spaces with underscores
    os.rename(os.path.join("images", file), os.path.join("images", new_name))

'''

'''
# Splitting Dataset into Train/Validation Sets.
import os
import random

files = os.listdir("dataset")
random.shuffle(files)  # Shuffle the dataset

split_ratio = 0.8  # 80% training, 20% validation
train_files = files[:int(len(files) * split_ratio)]
val_files = files[int(len(files) * split_ratio):]

# Move files to respective folders
os.makedirs("train", exist_ok=True)
os.makedirs("val", exist_ok=True)

for file in train_files:
    os.rename(os.path.join("dataset", file), os.path.join("train", file))

for file in val_files:
    os.rename(os.path.join("dataset", file), os.path.join("val", file))

'''