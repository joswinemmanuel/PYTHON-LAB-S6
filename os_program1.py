import os

cur_dir = os.getcwd()

os.mkdir(os.path.join(cur_dir, 'new_folder'))
os.chdir(os.path.join(cur_dir, 'new_folder'))

print(os.getcwd())
