"""course="python"
for s in course:
    print(s)
lists=[23,45,"Ano"]
for value in lists:
    print(value)
for tuple in (23,45,"ano"):
    print(tuple)
for set in {23,45,23,"ano"}:
    print(set)
student={"name":"Ano","age":23,"job":"IT Analyst"}
for s in student:
    print(s,":",student[s])            
         """


"""string=input("enter the string")
c_count=dict()
for k in string:
    if k in c_count:
        c_count[k]=c_count[k]+1
    else:
        c_count[k]=1  #c_count['j']=1
print(c_count)
for key in c_count:
    print(key,"=",c_count[key])            """


"""for pattern in range(5):
    print ("*" * pattern)"""


"""for n in range(1,6):
    for c in range(1,n+1):
        print(c,end="")
    print("")   """

"""num=int(input("enter the number"))
fac=1
for i in range(1,num+1):
    fac=fac*i
print(f"Factorial of {num} is {fac}")  """  


star=1
for row in range(1,6):
    for sp in range(5-row):
        print(" ",end="")
    for column in range(star):
        print("*",end="")
    star+=2
    print("")