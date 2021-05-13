import os


def find_files(path_dir, file_name='', result=list()):
    '''path_dir директория для поиска файлов (ищем в ней + вложенные директории)
    file_name (имя для поиска, по умолчанию все файлы)
    result список абсолютных путей найденных файлов
    '''
    if os.path.exists(path_dir):
        for i_path in os.listdir(path_dir):
            path = os.path.join(path_dir, i_path)
            if os.path.isfile(path) and (file_name == i_path or not file_name):
                result.append(path)
            elif os.path.isdir(path):
                find_files(path, file_name, result)
    return result


path_abs = os.path.abspath(os.path.join('..', '..', '..', '..', 'python_basic'))
found_files_list = find_files(path_abs, 'main.py')

text = ''
count = len(found_files_list)

file_in = open(os.path.join('answer.txt'), 'w', encoding='utf8')
for i_file in found_files_list:
    file_out = open(i_file, 'r', encoding='utf8')
    text = file_out.read()
    file_out.close()

    file_in.write(text + '\n' + '*'*40 + '\n')

if not file_in.closed:
    file_in.close()
print(f'Запись завершена, записано {count} файлов.')
