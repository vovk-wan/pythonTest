class Potato:
    states = {0: 'клубень', 1: 'росток', 2: 'зелёная', 3: 'созрела'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print('Картошка {}, сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))

    def isripe(self):
        if self.state == 3:
            return True
        return False


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_garden(self):
        print('Состояние грядки')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.isripe() for i_potato in self.potatoes]):
            print('Картошка не созрела.\n')
        else:
            print('Пора собирать урожай!\n')


my_garden = PotatoGarden(7)

my_garden.grow_garden()

my_garden.are_all_ripe()

for _ in range(3):
    my_garden.grow_garden()
    my_garden.are_all_ripe()