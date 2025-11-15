class A:
    def __init__(self,t):
        self.title=t
        
class B(A):
    def display(self):
        print(self.title)
obj=B("class B")
obj.display()        


class Base:
    def Method1(self):
        print("this function is in parent class")
class Derived(Base):
    def Method2(self):
        print("this function is in Child class")
obj=Derived()
obj.Method1()
obj.Method2()

            