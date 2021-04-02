import random


def move_zero(m_list):  # красивого решения с перестановкой не нашел очень много условий получается
    count_zero = m_list.count(0)
    len_list = len(m_list)
    if count_zero > 0:
        count_move = 0
        while m_list.index(0) < len_list - count_zero:
            for i in range(m_list.index(0), len_list - 1 - count_move):
                m_list[i] = m_list[i+1]
            m_list[len_list - 1 - count_move] = 0
            count_move += 1


number_list = [random.randint(0, 5) for _ in range(15)]  # [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0]

print('Сгенерированный список:       ', number_list)

temp_list = number_list[:]
move_zero(temp_list)
print('перестановка:                 ', temp_list)

count_0 = temp_list.count(0)
temp_list[len(temp_list) - count_0:] = []
print('перестановка - 0:             ', temp_list)


number_list = [i for i in number_list if i != 0] + [0 for _ in range(count_0)]
print('\nПерезапись списка без 0,\nи добавление 0 в конец списка:',  number_list)
number_list[len(number_list) - count_0:] = []
print('Удаление 0 в конце списка:    ',  number_list)
