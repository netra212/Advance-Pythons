# import os
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
print(os.rename("test_dir", "my_folder"))
