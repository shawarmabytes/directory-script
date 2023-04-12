import os
import shutil

og = os.getcwd()+"\\"
#print(og)

folders = os.listdir(os.getcwd()) #list of folders in current directory
#print(folders)

dir = [] #initialize

for i in folders:
    dir.append(og+i)

print(dir) #list of directories

    


