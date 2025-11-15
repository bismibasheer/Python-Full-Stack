class A:
    def greeting(self):
        print("Good Evening")          #Method Overriding
class B(A):
   def greeting(self):
        print("Hello class B")
ob=B()
ob.greeting()  


class A:
    def __init__(self,var,var1):
        self.a=var
        self.b=var1                    #Operator Overloading
    def __add__(self,other):
        return self.a+other.a,self.b+other.b

obj1=A(23,1)
obj2=A(6,5)
print(obj1+obj2)        