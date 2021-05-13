class Unit:
    def __init__(self, hitpoints=10):
        self.__hitpoints = 10
        self.set_hitpoints(hitpoints)
        '''Класс обладает запасам хитпоинтов "очков жизни" в виде целого положительного числа,
        и способен получать урон в виде понижения количества хитпонитов'''

    def set_hitpoints(self, hitpoints):
        try:
            self.__hitpoints = abs(int(hitpoints))
        except ValueError:
            print('Не верно задано количество жизни,\n'
                  'значение не менялось')

    def take_damage(self, damage=0):
        try:
            self.__hitpoints -= abs(int(damage))
        except ValueError:
            print('Не верно задан урон,\n'
                  'значение не изменяется')

    def get_hitpoints(self):
        return self.__hitpoints


class SoldierUnit(Unit):

    def take_damage(self, damage=10):
        super().take_damage(damage)


class EverymanUnit(Unit):

    def take_damage(self, damage=20):
        super().take_damage(damage * 2)


s = SoldierUnit(30)
print(s.get_hitpoints())
s.take_damage(10)

print(s.get_hitpoints())

every = EverymanUnit(50)
print(every.get_hitpoints())
every.take_damage(10)

print(every.get_hitpoints())
