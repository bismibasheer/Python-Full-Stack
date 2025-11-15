"""def Fun():
    def nf():
        print("Hi")
    nf()
    print("Outer Function")
Fun()   """     
        
def Fun():
    course="python"
    def nf():
        nonlocal course
        course=course+" Full Stack"
        print(course)
        print("hi")
    nf()
    print("Outer fun")
    print(course)
Fun()
