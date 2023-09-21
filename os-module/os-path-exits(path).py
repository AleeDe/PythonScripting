import os
#In this program we check wether file  or directory is presnt or not
path_check='/home/ali/Desktop/Python Scriting'
if (os.path.exists(path_check)):
    print("path exists")
else:
    print("path not exists")