class CanFly:
    def __init__(self):
        self.__height = 0
        self.__speed = 0

    def __str__(self):
        return 'высота {height}, скорость {speed}, полёт нормальный'.format(
            height=self.__height, speed=self.__speed
        )

    def set_speed(self, speed):
        self.__speed = speed

    def set_height(self, height):
        self.__height = height

    def takeoff(self):
        pass

    def fly(self):
        pass

    def landing(self):
        self.__speed = 0
        self.__height = 0


class Butterfly(CanFly):

    def takeoff(self):
        self.set_height(1)

    def fly(self):
        self.set_speed(0.5)


class Rocket(CanFly):
    def __str__(self):
        return super().__str__()

    def takeoff(self):
        self.set_height(500)

    def fly(self):
        self.set_speed(1000)

    def landing(self):
        super().landing()
        print('BOOOOM!!!!')

    def explosion(self):
        self.set_speed(10000)
        self.set_height(999999)
        print('BOOOM BADA BOOOOM!!! BAH BDISHHH')


r = Rocket()
print(r)
r.takeoff()
print(r)
r.fly()
print(r)
r.landing()
print(r)
r.explosion()
print(r)

b = Butterfly()
print(b)
b.takeoff()
print(b)
b.fly()
print(b)
b.landing()
print(b)
