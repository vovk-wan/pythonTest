class Ship:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return '\nКорабля называется {model}'.format(model=self.__model)

    def sail(self):
        print('\nКорабль {model} поплыл!'.format(model=self.__model))


class WarShip(Ship):
    def __init__(self, model, weapons):
        super().__init__(model)
        self.__weapons = weapons

    def attack(self):
        print('\n{weapons}-- Booooom!!!          Booooom!!!\nBooooom!!!\nBooooom!!!\nBooooom!!!\n'
              'Booooom!!!  Booooom!!!\n           '.format(weapons=self.__weapons))


class CargoShip(Ship):
    def __init__(self, model, tonnage=0):
        super().__init__(model)
        self.__tonnage = tonnage

    def loading(self):
        print('\nЗагрузка')
        self.__tonnage += 1
        print('Общая загруженность {tonnage}'.format(
            tonnage=self.__tonnage))

    def unloading(self):
        print('\nРазгрузка')
        if self.__tonnage <= 0:
            print('Груза нет')
        else:
            self.__tonnage -= 1
        print('Общая загруженность {tonnage}'.format(
            tonnage=self.__tonnage))


destroyer = WarShip('destroyer', 'Gausse')

destroyer.sail()

destroyer.attack()

carrier = CargoShip('carrier', 1)

carrier.sail()
carrier.sail()

carrier.unloading()
carrier.unloading()
carrier.unloading()

carrier.loading()
carrier.loading()
carrier.loading()
carrier.loading()
carrier.unloading()