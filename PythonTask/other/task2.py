n = int(input('Введите количество элементов: '))

new_list = [1 if i % 2 == 0 else i % 5 for i in range(n)]

print('Результат:', new_list)
