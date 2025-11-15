from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def geeting(self):
        pass
class B(A):
    def geeting(self):
        print("Good Morning")
ob=B() 
ob.geeting()         
