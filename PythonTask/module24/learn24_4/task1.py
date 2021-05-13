class TayotaCar:

    def __init__(self, color, price, max_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = 0

    def print_info(self):print('Color: {}\nPrise: {}\nMax speed: {}\nCurrent speed: {}'.format(
        self.color, self.price, self.max_speed, self.current_speed
    ))

    def set_current_speed(self, spped):
        if spped > self.max_speed:
            return self.current_speed
        else:
            self.current_speed = spped
        return self.current_speed


new_car = TayotaCar('red', price=11000000, max_speed=280)
new_car.print_info()

new_car.set_current_speed(250)
new_car.print_info()