class Base:
    def __init__(self, name, roll, role):
        self.name = name
        self.roll = roll
        self.role = role

class Intermediate(Base):
    def __init__(self, age, name, roll, role):
        super().__init__(name, roll, role)
        self.age = age

class Derived(Intermediate):
    def __init__(self, age, name, roll, role):
        super().__init__(age, name, roll, role)

    def Print_Data(self):
        print(f"The Name is : {self.name}")
        print(f"The Age is : {self.age}")
        print(f"The Role is : {self.role}")
        print(f"The Roll is : {self.roll}")

obj = Derived(21, "Lokesh Singh", 25, "Software Trainer")
obj.Print_Data()