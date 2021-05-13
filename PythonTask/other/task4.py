def annuity_func(summ_s, years, procent_in_year):
    sums_s_let = summ_s
    count = 0
    annuity_coefficient = procent_in_year * (1 + procent_in_year) ** years / ((1 + procent_in_year) ** years - 1)
    #print(annuity_coefficient)
    while count < 3:
        count += 1
        print ("Период", count)
        print("Остаток долга на начало периода: ", summ_s)
        print("Выплачено процентов:", summ_s * procent_in_year)
        telo_in_credit = (round(sums_s_let * annuity_coefficient, 2) - summ_s * procent_in_year)
        print("Выплачено тела кредита:", telo_in_credit)
        summ_s -= telo_in_credit
    print("Остаток долга:", summ_s)
    print()
    new_years = (float(input("На сколько лет продляется договор? "))) / 100
    procent_in_year = procent_in_year +  new_years * 2
    print("Увеличена ставка процентов до:", int(procent_in_year * 100))
    sums_s_let = summ_s
    years_left = years - count + int(new_years * 100)
    annuity_coefficient = procent_in_year * (1 + procent_in_year) ** years_left / ((1 + procent_in_year) ** years_left - 1)
    #print(years_left, "осталось периодов")
    print()
    for number in range(years_left):
        print ("Период", number + 1)
        print("Остаток долга на начало периода: ", summ_s)
        print("Выплачено процентов:", summ_s * procent_in_year)
        telo_in_credit = (round(sums_s_let * annuity_coefficient, 2) - summ_s * procent_in_year)
        print("Выплачено тела кредита:", telo_in_credit)
        summ_s -= telo_in_credit
    print("Остаток долга:", summ_s)


summ_s = float(input("Введите сумму кредита: "))
years = int(input("На сколько лет выдан? "))
procent_in_year = float(input("Сколько процентов годовых? ")) / 100
annuity_func(summ_s, years, procent_in_year)