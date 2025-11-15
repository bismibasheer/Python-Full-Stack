a=12
b=2
try:
    print(a/b)
except ZeroDivisionError:
    print("cannot divided by zero")
except NameError:
    print("please provide a value")
except TypeError:
    print("please provide integer value")  
except Exception as e:
    print(e)
else:
    print("program executed,No Error raise")
finally:
    print("Completed")      


