import os

dir_path='/home/ali/Desktop/shellScript/Projects'
files=os.listdir(dir_path)

for file in files:
    print(file)