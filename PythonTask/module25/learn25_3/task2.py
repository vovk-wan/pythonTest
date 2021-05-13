class Robot:

    def __init__(self, model, specs):
        self.__model = model
        self.__specs = specs

    def operate(self, mess=''):
        if self.__specs:
            print(self.__specs, mess)


class HoverRobot(Robot):
    def __init__(self, model, bag):
        super().__init__(model, specs='Совершаю уборку')
        self.__bag = bag

    def operate(self, mess=''):
        super().operate()
        self.__bag += 1
        print('Загруженность {}'.format(self.__bag))


class SubmarineRobot(Robot):
    def __init__(self, model, deep, weapons):
        super().__init__(model, specs='Провожу охрану ')
        self.__deep = deep
        self.__weapons = weapons

    def get_weapons(self):
        return self.__weapons

    def operate(self, message=''):
        super().operate('\nс помощью {w}'.format(w=self.get_weapons()))
        self.__deep += 1
        print('Глубина {}'.format(self.__deep))


class SecurityRobot(Robot):
    def __init__(self, model, weapons):
        super().__init__(model, specs='Провожу охрану ')
        self.__weapons = weapons

    def get_weapons(self):
        return self.__weapons

    def operate(self, mess=''):
        super().operate('\nс помощью {w}'.format(w=self.get_weapons()))






r = HoverRobot(model='hov-r2d2', bag=0)
r.operate()

sec = SecurityRobot(model='robocop 001 ground level', weapons='пулемёт')
sec.operate()

sub = SubmarineRobot(model='robobot 002 underwater', deep=5, weapons='Гарпуномет' )
sub.operate()