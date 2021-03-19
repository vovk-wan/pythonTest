def invert(number):
    temp1 = int(number)
    number_inv_int = temp1
    count = 0
    while number_inv_int > 0:
        number_inv_int //= 10
        count += 1
    while temp1 > 0:
        count -= 1
        number_inv_int += (temp1 % 10) * 10 ** count
        temp1 //= 10
    temp2 = 0
    number_inv_float = round(number - int(number), 5)
    count = 0
    while number_inv_float > 0:
        temp2 += int(number_inv_float * 10) * 10 ** count
        number_inv_float = round(number_inv_float * 10 - int(number_inv_float * 10), 5)
        count += 1
    number_inv_float = temp2 / 10 ** count
    number_inv = number_inv_int + number_inv_float
    return number_inv

numberN = 12.34
numberK = 56.78

N_inv = invert(numberN)
print('\nПервое число наоборот:', N_inv)
K_inv = invert(numberK)
print('Второе число наоборот:', K_inv)

summ = float(N_inv) + float(K_inv)
print('Сумма:', summ)