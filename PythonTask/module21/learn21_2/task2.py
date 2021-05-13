def power(a, n):
    if n > 1:
        return (a * power(a, n - 1))
    elif n == 1:
        return a
    elif n <= -1:
        return 1 / (a * power(a, -n - 1))
    elif n == 0:
        return 1
    else:
        return None
float_num = float(input('Введите вещественное число: '))
int_num = int(input('Введите степень числа: '))
print(float_num, '**', int_num, '=', power(float_num, int_num))





#Правильный результат:
#Введите вещественное число: 1.5
#Введите степень числа: 5
#1.5 ** 5 = 7.59375