class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def macbook(self):
        return f"The {self.brand} {self.model} has a price of {self.price} dollars."

# m1 = Laptop("Apple", "MacBook Air", 1500)

# print(m1.macbook())

class MyLaptop(Laptop):
    def __init__(self, brand, model, price, screen_size, chip, color):
        super().__init__(brand, model, price)  
        self.screen_size = screen_size
        self.chip = chip
        self.color = color

    def details(self):
        return (f"This is a {self.brand} {self.model} with a screen size of {self.screen_size} "
                f"inches, a {self.chip} chip, and a {self.color} color.")

m2 = MyLaptop("Apple", "MacBook Pro", 2000, 16, "M1", "Silver")

print(m2.details())
