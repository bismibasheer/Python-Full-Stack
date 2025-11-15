"""Students=[]
while True:
    roll_no=int(input("Enter the student Rollno. : "))
    name=input("Enter the Student Name : ")
    print("Enter the mark of 3 Subjects")
    mark1=int(input("m1 = "))
    mark2=int(input("m2 : "))
    mark3=int(input("m3 : "))
    

    marks=(mark1+mark2+mark3)
    if marks>=130:
        grade="A grade"
    elif marks>=110:
        grade="B grade"
    elif marks>=90:
        grade="C grade"
    elif marks>=70:
        grade="d grade"
    else:
        grade="failed"
    
    Students=Students+[(name ,marks ,grade)]

    c=input("Do you want to continue(yes/no) :")
    if c!= "yes":
        break


for s in Students:
    print(s)"""



students={}
def Grade(avg):
    if avg>=95:
        return "A+ grade"
    elif avg>=90:
        return "A grade"
    elif avg>=85:
        return "B+ grade"
    elif avg>=80:
        return "B grade"
    elif avg>=70:
        return "c grade"
    elif avg>=60:
        return "d grade"
    else:
        return "failed"
while True:
    marks=[]
    roll_number=int(input("Enter the roll number :"))
    if roll_number in students:
        print("Roll number exists")
        continue
    std_name=input("Enter the name :")
    print("Enter the mark of 3 subjects :")
    for m in range(1,4):
        score=int(input("Enter the score :"))
        marks=marks+[score]
    avg=sum(marks)/3
    g=Grade(avg)

    students[roll_number]={"name":std_name,"marks":marks,"grade":g}
    choice=input("Do you wish to continue (yes/no) ? ")
    if choice!="yes":
        break
print(students)