class Elemental:
    table = {
        'Вода + Огонь': 'Шторм',
        'Вода + Воздух + Земля': 'Говно-шторм',
        'Вода + Воздух + Земля + Огонь': 'Шторм огненного говна',
        'Вода + Воздух + Земля + Огонь + Огонь': 'Шторм плазменного говна',
        'Вода + Земля': 'Грязь',
        'Вода + Воздух': 'Пар',
        'Воздух + Огонь': 'Молния',
        'Воздух + Земля': 'Пыль',
        'Воздух + Земля + Огонь': 'Раскаленный метеоритный дождь',
        'Земля + Огонь': 'Лава'
    }

    def __init__(self, elemental):
        self.elemental = [elemental]

    def __add__(self, other):
        self.elemental.extend(other.elemental)
        return self

    def __repr__(self):
        new_elem = ' + '.join(sorted(self.elemental))
        result = Elemental.table.get(new_elem, 'Неизвестная комбинация')
        # print('Кастуем', new_elem)
        return new_elem + ' = ' + result + '\n'


spirit = Elemental('Воздух')
wather = Elemental('Вода')
earth = Elemental('Земля')
fire = Elemental('Огонь')
elems = [earth, spirit, fire, fire]
print(type(elems))
elem = wather
for e in elems:
    elem = elem + e
    print(elem)

elem = earth + fire + spirit
print(earth)

# зачет!
