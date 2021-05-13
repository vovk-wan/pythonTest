class Point:

    def __init__(self, x=0, y=0):
        self.__x = 0
        self.__y = 0
        self.set_x(x)
        self.set_y(y)

    def __str__(self):
        return 'Апппупеть какая красивая точка'

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x
        else:
            raise ValueError('Ожидалось число.')

    def get_y(self):
        return self.__y

    def set_y(self, y):
        if isinstance(y, (int, float)):
            self.__y = y
        else:
            raise ValueError('Ожидалось число.')


p = Point(2, 33)
p.set_x(545)
print(p.get_y())
print(p._Point__x)
print(p)
