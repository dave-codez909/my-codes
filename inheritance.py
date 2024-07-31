class parentClass:
    def method(self):
        print("parent method")


class childClass(parentClass):
    def method(self):
        print("child method")

obj = childClass()
obj.method() #output: child method       