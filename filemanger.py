import os
import shutil


path = input('Enter your path : ')

files = os.listdir(path)

for i in files:
    filename, file_extension = os.path.splitext(i)
    file_extension = file_extension[1:]
    folder_path = path+"\\"+file_extension
    if os.path.exists(folder_path):
        shutil.move(path+"\\"+i, path+"\\"+file_extension+"\\"+i)
    else:
        os.makedirs(folder_path)
        shutil.move(path+"\\"+i, path+"\\"+file_extension+"\\"+i)
