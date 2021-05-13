import os

path_dir = os.path.abspath(os.path.join(os.path.sep))

for i_elem in os.listdir(path_dir):
    print(os.path.join(path_dir, i_elem))