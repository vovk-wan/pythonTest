import os
import random


def find_file(path_dir, file_name='', result=list()):
    if os.path.exists(path_dir):
        for i_path in os.listdir(path_dir):
            path = os.path.join(path_dir, i_path)
            if os.path.isfile(path) and (file_name == i_path or not file_name):
                result.append(path)
            elif os.path.isdir(path):
                find_file(path, file_name, result)
    return result


file_list = find_file(os.path.abspath(os.path.join('..', '..', 'module21')), 'task1.py',)
random_file = random.choice(file_list)
file_script = open(random_file, 'r', encoding='utf8')
print(random_file)
for i_line in file_script:
    print(i_line, end='')


