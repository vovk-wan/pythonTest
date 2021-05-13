class PointNew:
    quantity = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        PointNew.quantity += 1

    def print_info(self):print('x = {}\ny = {}\nq = {}\n'.format(
        self.x,
        self.y,
        self.quantity
    ))


p1 = PointNew()
p2 = PointNew()
p2.print_info()
p3 = PointNew(1, 2)
p4 = PointNew(3, 4)
p1.print_info()

p4.print_info()