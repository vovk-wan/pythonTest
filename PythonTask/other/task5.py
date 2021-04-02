import random


def random_str_for_task5(str_len):
    letters = 'abcdefgijklmnopqrstuvwxyz'  # h
    before_middle = random.randint(1, str_len // 2 - 1)
    after_middle = random.randint(str_len // 2 + 2, str_len - 2)
    str1 = ''
    for i in range(str_len):
        if i == before_middle or i == after_middle:
            str1 += 'h'
        else:
            str1 += random.choice(letters)
    return str1


random_string = random_str_for_task5(15)  #  '1111h1234567h2222'

first_h = random_string.index('h')
last_h = len(random_string) - 1 - random_string[::-1].index('h')

result_string = random_string[:first_h + 1] + random_string[last_h - 1: first_h: -1] + random_string[last_h:]

print('Строка:  ' + random_string)
print('Решение: ' + result_string)
