class TayotaCar:
    color = 'red'
    price = 1e6
    max_speed = 300
    current_speed = 0


new_car = TayotaCar()
very_new_car = TayotaCar()
very_very_new_car = TayotaCar()

new_car.current_speed = 150
very_new_car.current_speed = 175
very_very_new_car.current_speed = 212

print(new_car.price)
print(very_very_new_car.current_speed)
print(very_new_car.current_speed)
print(new_car.current_speed)
