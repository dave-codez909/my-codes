class shop:
    def __init__(self, name, brand, quantity):
        self.name = name
        self.brand = brand
        self.quantity = quantity

    def sell(self):
        print(f"we only sell {self.brand} and we only have {self.quantity}")

    def buy(self):
        amt = int(input("how many are you buying "))
        print(F"you have bought {amt} {self.brand}")
        rem = self.quantity - amt
        print(f"we now have {rem} {self.name} left")
        

        
coffee = shop("David's shop", "coffee", 400)

coffee.sell()
coffee.buy()
