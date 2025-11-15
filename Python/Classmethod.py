class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def new_student(cls,name,age):
        return cls(name,age)
std=Student("Bismi",30)
std2=Student.new_student("Ano",27)
print(std2.name)