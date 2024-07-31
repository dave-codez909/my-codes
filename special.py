
def __str__(self):
    return self.name

class Car:
    def __init__(self, name, brand, year):
        self.name = name
        self.brand = brand
        self.year = year

car = Car("Toyota", "Camry", 2022)
print (car)