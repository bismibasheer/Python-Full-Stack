def loginrequired(fun):
    def wrapper(n,status):
        if status:
            fun(n)
        else:
            print("invalid user")
    return wrapper
@loginrequired
def Dashboard(name):
    print("welcome",name)  
Dashboard("Bismi",True) 
   
"""k=loginrequired(Dashboard)
print(k)
k("Bismi",True)"""              