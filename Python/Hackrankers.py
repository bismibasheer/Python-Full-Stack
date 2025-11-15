n=int(input("Enter your Number"))
if n%2==0:
    if 2<=n<=5:
        print("not weird")
    elif 6<=n<=20:
        print("weird")
    elif n>20:
        print(" not weird")
    else:
        print("invalid")
else:
    print("weird")                