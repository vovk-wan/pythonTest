site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def dict_unpack(dict_temp, shift_p='', name_struct=''):
    result = []
    shift_p = ''.join([' ' for _ in range(len(name_struct)//2+2)]) + shift_p
    for key_d, value_d in dict_temp.items():
        if isinstance(value_d, dict):  # если вложенный словарь распаковка
            result.append("{0}{1}:{{ \n{2}\n{0}}},".format(
                shift_p,
                str(key_d),
                dict_unpack(value_d, shift_p=''.join([' ' for _ in range(len(key_d)//2 )]) + shift_p))
            )  # смещение добавляем чтоб смотрелось красивее и вложенность было сразу видно
        else:  # если ключи - значения, возвращаем обработанной строкой
            result.append("{0}{1}: '{2}',".format(shift_p, str(key_d), str(value_d)))
    else:
        result[-1] = result[-1].rstrip(',')
    if name_struct != '':
        result.insert(0, name_struct + '{')
        result.append('}')

    return f'\n'.join(result)

print(dict_unpack(site, name_struct='site = '))  # для проверки