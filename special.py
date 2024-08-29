class school:
    def __init__(self, classes, age, school_year):
        self.classes = classes
        self.age = age
        self.school_year = school_year

    def junior_class(self):
        return f"If you are in {self.classes} and you are {self.age} years old and in the {self.school_year} school year, you should move to the assembly."


class student(school):
    def __init__(self, classes, age, school_year, department, iq):
        super().__init__(classes, age, school_year)
        self.department = department
        self.iq = iq
        
    def senior_class(self):
        return (
            f"If you are in {self.classes} and you are {self.age} years old and in the {self.school_year} school year, "
            f"you should move to the assembly, but if you are in the {self.department} department and have an IQ of {self.iq}, "
            "you should stay behind for class."
        )
    
headboy = student("SS3", 16, "2023/2024", "Arts", 198)
print(headboy.senior_class())  # Call the method with parentheses
