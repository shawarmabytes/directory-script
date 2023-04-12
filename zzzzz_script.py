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
dir.pop(-1) #remove zzzzz.py from list

try: 
    lister_str = []

    for i in range(len(dir)):
        os.chdir(dir[i])
        lister_list = os.listdir(os.getcwd()) #list of files in current directory
        #print(lister)

        for j in lister_list:
            lister_str.append(j)
except Exception:
    pass

#print(lister_str)

for i in range(len(dir)):
    container = dir[i] + "\\" + lister_str[i]
    print(container)
    shutil.move(container, og)
    os.chdir(og) #the last folder couldn't be deleted because it was the current last directory from line 22
    print("if directory, removing..")
    if os.path.isdir(dir[i]):
        os.rmdir(dir[i])
        print("removed")
    print("")
    


