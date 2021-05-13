class Human:
    __count = 0

    def __init__(self, name, age):
        self.__name = ''
        self.__age = 0
        self.set_age(age)
        self.set_name(name)
        Human.__count += 1

    def __str__(self):
        return 'Здравствуйте, меня зовут {} мне {} лет всего нас {} человек.'.format(
            self.__name, self.__age, self.__count
        )

    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self.__name = name
        else:
            raise ValueError('Имя должно состоять только из букв')

    def set_age(self, age):
        if isinstance(age, int) and age in range(0, 100):
            self.__age = age
        else:
            raise ValueError('Возраст должен быть числом от 0 до 99')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_count(self):
        return self.__count


vas = Human('Вася', 33)
kol = Human('Коля', 15)
mash = Human('Маша', 25)

print('Вася', vas)
print(vas._Human__count)
print('Коля', kol)
print('Маша', mash)

print(mash.get_count())
print(Human._Human__count)
Human._Human__count = 25
print(Human._Human__count)