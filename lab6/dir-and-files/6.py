# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

# for i in range(65, 65+26):
#     filename = chr(i)+'.txt'
#     with open(chr(i) + ".txt", "w") as file:
#         file.writelines(chr(i))
import os.path
for i in range(65,65+26):
    f = open(os.path.expanduser(os.path.join(r'C:\Users\User\WorkSPACE\Рабочий стол\pp2\PP2\lab6\dir-and-files\check_for6',chr(i) + ".txt")), "a")