# Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.

import os

file = r'C:\Users\User\WorkSPACE\Рабочий стол\pp2\PP2\lab6\dir-and-files\check_for8.txt'
if os.access(file, os.F_OK)==True:
    os.remove(file)
else:
    print('Такого файла нет')