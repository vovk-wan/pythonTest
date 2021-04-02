def ask_user(question, complaints='записать, не записать', retries=3 ):
    while True:
        answer = input(question)
        if answer.lower() == 'да':
            return 1
        elif answer == 'нет':
            return 0
        else:
            print(complaints, f'.осталась {retries} попыток ')
            retries -= 1
        if retries < 0:
            break

ask_user('record in file ', retries=2)
