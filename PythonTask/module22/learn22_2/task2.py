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
                    print(result)
        else:
            result = None
        return result

print('Найдены пути:')
find_file(os.path.abspath(os.path.join('..', '..', 'module21')), 'task1.py')
