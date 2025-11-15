
for row in range(1,6):
    num=row
    counter=4
    for n in range(row):
        print(num,end="")
        num=num+counter
        counter-=1
    print("")    