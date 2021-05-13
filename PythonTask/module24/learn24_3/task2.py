class Famely:
    surname = 'New surname'
    money = 100543
    have_a_car = False

    def print_info(self):print('Surname: {}\nmoney: {}\nHave a car: {}\n'.format(
        self.surname, self.money, self.have_a_car
    ))

    def earn_money(self, amount):
        self.money += amount
        print('Earned money: {}\nCurrent moneyL: {}'.format(amount, self.money))

    def bay_car(self, price, discount=0):
        total_price = price - price * discount/100
        if self.money >= total_price:
            self.money -= total_price
            self.have_a_car = True
            print('House purchased! Current money {}\n'.format(self.money))
        else:
            print('Not enough money!\n' )


neighbors = Famely()

neighbors.print_info()

neighbors.bay_car(500000)

neighbors.earn_money(350000)

neighbors.bay_car(500000, 10)