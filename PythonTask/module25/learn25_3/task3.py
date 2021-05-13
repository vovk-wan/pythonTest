class MyException(Exception):
    pass


with open('numbers.txt', mode='r', encoding='utf8') as numbers_file:
    for i_str in numbers_file:
        numbers = i_str.split()
        try:
            divisible = int(numbers[0])
            divisor = int(numbers[1])
            if divisible < divisor:
                answer = divisible / divisor
            else:
                try:
                    raise MyException('Фиг вам делим только меньше на больше')
                except MyException:
                    print('Фиг вам делим только меньше на больше')
            print(answer)
        except (ValueError, ZeroDivisionError):
            print('Ваше число не число')