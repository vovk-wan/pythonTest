nums = '0123456789'
alpha = 'ABCDIFGHIJKLMNOPQRSTUVWZYX'
cnt_num = 0
cnt_sym = 0
while True:
    password = input('Придумайте пароль: ')
    if len(password) < 8:
        print('Error. Пароль должен быть не меньше восьми символов.')
    else:
        for i in password:
            if i.isdigit():
                cnt_num += 1
            elif i in alpha:
                cnt_sym += 1
    if cnt_num < 3:
        print('Error. Пароль должен содержать минимум три  цифры')
    elif cnt_sym < 1:
        print('Error. Пароль должен содержать минимум одну заглавную букву')
    else:
        print('  ВСЁ ЗБС =) ')