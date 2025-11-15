class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def add_detail(self):
        with open("std_details.txt","a") as file:
            file.write(f"{self.name}|{self.age}|{self.course}\n")

    @staticmethod
    def display_details():
        with open("std_details.txt", 'r') as file:
            content = file.readlines()
            for line in content:
                student = line.strip().split('|')
                print("Name :", student[0])
                print("Age :", student[1])
                print("Course :", student[2])
                print("--------------")
with open("std_details.txt","w") as myfile:
    pass
std_count=int(input("Enter the student count : "))
for k in range(std_count):
    name=input("Enter the student name : ")
    age=int(input("Enter the student age : "))
    course=input("Enter student course : ")
    std=Student(name,age,course)
    std.add_detail()

Student.display_details()