def count_letters(digital, symbol):
    digit_count = 0
    symbol_count = 0

    for symbols in text:
        if symbols == digital:
            digit_count += 1

        elif symbols == symbol:
            symbol_count += 1
    print('Количество цифр ', digital, ':', digit_count)
    print('Количество букв ', symbol, ':', symbol_count)


text = input('Введите текст: ')
digital = int(input('Какую цифру ищем?: '))
symbol = input('Какую букву ищем?: ')

count_letters(digital, symbol)