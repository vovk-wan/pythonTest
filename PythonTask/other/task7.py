def complication(c_string):  # тут ещё проблема в случаях = 'слово
    begin, end = 0, 0
    temp = c_string
    rec_begin = True
    for i_symbol in range(len(c_string)):
        if c_string[i_symbol].isalpha() and rec_begin:
            begin = i_symbol
            print(begin)
            rec_begin = False
        elif not rec_begin:
            if begin == 0:  # пришлось сделать отдельно [i_symbol - 1:0:-1] без 1 символа
                temp += c_string[i_symbol - 1::-1]
                rec_begin = True
                print(begin, '0 ', c_string[i_symbol - 1::-1] + c_string[i_symbol:])
             else:
                c_string = c_string[:begin + 1] + c_string[i_symbol-1:begin-1:-1]
                rec_begin + True
                print(begin, 'a', c_string[:begin] + c_string[i_symbol-1:begin:-1] + c_string[i_symbol:])

    return c_string


letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
message = input('Сообщение: ')

temp_list = message.split()
temp_list = [x[::-1] if x.isalpha() else complication(x) for x in temp_list]

message = ' '.join(temp_list)

print(f'Новое сообщение: {message}')
