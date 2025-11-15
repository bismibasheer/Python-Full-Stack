"""count=1
while count<=5:
    print(count)
    count=count+1  """  

"""number=int(input("Enter the number : "))
num=1
fact=1
while num<=number:
    fact=fact*num
    num=num+1
print(f"Factorial of {number} is {fact}")"""



"""number=int(input("Enter the sequence count : "))
num=1
first,second=0,1
print(first,second,end=" ")
while num<=number-2:
    third=first+second
    print(third,end=" ")
    first,second=second,third
    num=num+1"""

"""num=1
while num<=10:
    
    if num==4:
        num=num+1
        continue
    print(num,end="")
    num=num+1"""


num=1
while num<=10:
    num=num+1
    if num==4:
        break
    print(num,end="")
  
    