class A:
    def __init__(self):              #private
        self.__course="python"
    def display(self):
        print("hello")
ob=A()
print(ob._A__course)
ob.display()        


class A:
    def __init__(self):              #protect
        self._course="python"
    def display(self):
        print("hello")
ob=A()
print(ob._course)
ob.display()   