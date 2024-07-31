class animals:
    def __init__(self, cat, dog, bird, lion):
        self.cat = cat
        self.dog = dog
        self.bird = bird
        self.lion = lion

    def sound(self):
        print (f'{self.cat} says meow, {self.dog} says woof, {self.bird} says chirp, {self.lion} roars!')    
