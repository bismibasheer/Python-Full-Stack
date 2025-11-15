"""def Fun(**kwargs):
    print(kwargs)
    print(f"My name is {kwargs['n']} and i am {kwargs['a']} years old")
    print("Live in ", kwargs['place'])

name="Ano"
age=27
Fun(a=age,n=name,place="kochi")"""



def Add(*number):
    sum=0
    for k in number:
        sum+=k
    return sum
print("sum of number is",Add(45,3,8,34))    
