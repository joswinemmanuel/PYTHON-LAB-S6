import os

print("All the files and folders in cwd is : ")
index = 1
for i in os.listdir(os.getcwd()):
    print(f"{index}) {i}")
    index += 1
