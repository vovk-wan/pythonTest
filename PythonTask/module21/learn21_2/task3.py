site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_value(struct_dict_f, key_f):
    if key_f in struct_dict_f:
        return struct_dict_f[key_f]
    else:
        for sub_struct_dict in struct_dict_f.values():
            if isinstance(sub_struct_dict, dict):
                result = find_value(sub_struct_dict, key_f)
                if result:
                    break
        else:
            result = None
        return result


key = input('Искомый ключ: ')
print('Значение:', find_value(site, key))
