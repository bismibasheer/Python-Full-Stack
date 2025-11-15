class A:
    def __init__(self,av,i):
        self.a=av
        B.__init__(self,i)
class B:
    def __init__(self,ab):
        self.b=ab
class C(A,B):
    def Result(self):
        print(self.a+self.b)
       
obj=C(10,20)
obj.Result()
                       
        