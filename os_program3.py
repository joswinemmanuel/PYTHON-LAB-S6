import os

filepath, filename = os.path.split(os.getcwd())

print("File path is : ", filepath)
print("File name is : ", filename)

print(os.path.join(filepath, filename))
print(os.path.splitext("data.jpg")) 
