loan_amount = float(input('Введите сумму кредита: '))
deadline = int(input('На сколько лет выдан? '))
percent = int(input('Сколько процентов годовых? '))
p = percent / 100


def calc(deadLine_c):
    return (p * (1 + p) ** deadLine_c) / ((1 + p) ** deadLine_c - 1)


loan_body = 0
count = 1
new_deadline = 0
for year in range(1, 4):
    print('Период: ', year)
    print('Остаток долга на начало периода: ', loan_amount)
    paid_percent = loan_amount * p
    loan_body = round(calc(deadline + 1 - year) * loan_amount, 2) - paid_percent
    print('Выплачено процентов: ', paid_percent)
    print('Выпдачено тела кредита: ', loan_body)
    loan_amount -= loan_body
print('Остаток долга: ', loan_amount)

new_deadline = int(input('На сколько лет продлевается договор? '))
new_percent = int(input('Увеличение ставки до: '))
p = new_percent / 100
for year in range(1, deadline - 3 + new_deadline + 1):
    print('Период: ', year)
    print('Остаток долга на начало периода: ', loan_amount)
    paid_percent = loan_amount * p
    loan_body = round(calc(deadline + 1 - year) * loan_amount, 2) - paid_percent
    print('Выплачено процентов: ', paid_percent)
    print('Выплачено тела кредита: ', loan_body)
    loan_amount -= loan_body
print('Остаток долга: ', loan_amount)