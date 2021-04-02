import random

command1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
command2 = [round(random.uniform(5, 10), 2) for _ in range(20)]

winners = [command1[i] if command1[i] > command2[i] else command2[i] for i in range(len(command1))]

print('Первая команда:', command1)
print('Вторая команда:', command2)
print('Победители тура:', winners)

