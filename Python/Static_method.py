class Student:
    @staticmethod
    def validate(mark):
        if mark>50:
            return "pass"
        else:
            return "Fail"
    def __init__(self,m):
        self.mark=m
    def result(self):
        print(Student.validate(self.mark))    
std=Student(65)
std.result()
