class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def display_amount(self):
        print(f"${self.dollars}.{self.cents}")

    def set_amount(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def decrease_price(self, amount):
        if self.price.cents >= amount:
            self.price.cents -= amount
        else:
            self.price.dollars -= 1
            self.price.cents = 100 - (amount - self.price.cents)

    def display_info(self):
        print(f"Product: {self.name}, Price: ", end="")
        self.price.display_amount()


price1 = Money(10, 50)

product1 = Product("Phone", price1)

product1.display_info()

product1.decrease_price(3)

product1.display_info()