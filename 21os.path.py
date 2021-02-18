
import os

path = os.getcwd()
file_list = os.walk(path)

for dirpath, dirname, filename in file_list:
    print(dirpath)
    print(dirname)
    print(filename)
    print('.........................................')