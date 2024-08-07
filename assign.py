class Catholic:
    def __init__(self, name, birth_date, church, date, certificate):
        self.name = name
        self.birth_date = birth_date
        self.church = church
        self.date = date
        self.certificate = certificate

    def check_mass_attendance(self):
        print(f"If {self.name} does not come to church on {self.date}, get rid of {self.certificate} certificate.")

    def is_member(self):
        print(f"{self.name} is not a member of {self.church} Catholic church.")

# Sample usage
david = Catholic("david", "1990-05-15", "St. Paul's", "2022-07-14", "Baptism")

david.check_mass_attendance()
david.is_member()
