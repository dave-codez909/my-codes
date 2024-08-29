class Car:
    def __init__(self, brand, model, year, color, tramission_type, engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.tramission_type = tramission_type
        self.engine = engine
    def speed(self):
        return self.engine
    
    def summary(self):
        return f"This car is a {self.color} {self.brand} {self.model}, made in {self.year}."
    



my_car = Car("mclaren", "autura", "2024", "orange", "automatic", "v6")
print (my_car   .summary)



        