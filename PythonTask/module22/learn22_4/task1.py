import os


def find_file(path_dir, file_name=''):
    if os.path.exists(path_dir):
        for i_path in os.listdir(path_dir):
            path = os.path.join(path_dir, i_path)
            if os.path.isfile(path) and (file_name == i_path or not file_name):
                return path
            elif os.path.isdir(path):
                result = find_file(path, file_name)
                if result:
                    return result
        else:
            return None

path_abs = os.path.abspath(os.path.join('..', 'learn22_3', 'task'))
file_path = find_file(path_abs, 'task1.py')
file_out = open(os.path.join(path_abs, 'numbers.txt'), 'r', encoding='utf8')
summ = 0
for i_line in file_out:
    summ += int(i_line)

file_in = open(os.path.join(path_abs, 'answer.txt'), 'a', encoding='utf8')
file_in.write(str(summ))
file_in.close()
