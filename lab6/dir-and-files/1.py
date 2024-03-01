# Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path = r'C:\Users\User\WorkSPACE\Рабочий стол\pp2\PP2\lab6\dir-and-files\check1_for1'
print("Directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nFiles:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])