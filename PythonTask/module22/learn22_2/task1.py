import os


def find_file(path_dir, file_name=''):
    if os.path.exists(path_dir):
        for i_path in os.listdir(path_dir):
            path = os.path.join(path_dir, i_path)
            if os.path.isfile(path) and (file_name == i_path or not file_name):
                return path
            elif os.path.isdir(path):
                print("Its directory", path)
                result = find_file(path, file_name)
                if result:
                    break
        else:
            result = None
        return result


this_file = find_file(os.path.abspath(os.path.join('..', '..')), 'new.txt')
if this_file:
    print(this_file)
    print('Размер файла: ', os.path.getsize(this_file).bit_length())
else:
    print('Файл не найден.')
