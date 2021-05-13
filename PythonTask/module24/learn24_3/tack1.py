class TayotaCar:
    color = 'red'
    price = 1e6
    max_speed = 300
    current_speed = 0

    def print_info(self):print('Color: {}\nPrise: {}\nMax speed: {}\nCurrent speed: {}'.format(
        self.color, self.price, self.max_speed, self.current_speed
    ))

    def set_current_speed(self, spped):
        if spped > self.max_speed:
            return self.current_speed
        else:
            self.current_speed = spped
        return self.current_speed

new_car = TayotaCar()
very_new_car = TayotaCar()
very_very_new_car = TayotaCar()

new_car.current_speed = 150
very_new_car.current_speed = 175
very_very_new_car.current_speed = 212

new_car.print_info()

speed = very_new_car.set_current_speed(3330)
print('new speed', speed)
print(very_very_new_car.current_speed)
print(very_new_car.current_speed)
print(new_car.current_speed)
