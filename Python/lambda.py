
#lambda
square=lambda num:num**2
print(square(4))


add=lambda a,b:a+b
print(add(2,4))

#map

def square(num):
    return num**2
print(tuple(map(square,range(2,6))))


print(tuple(map(lambda num:num**2,[3,7,2,4])))

first_name=['ano','joyal','juhaina']
last_name=['sunny','sunny','basheer']
print(list(map(lambda f_name,l_name :f_name+''+l_name,first_name,last_name)))


#filter

print(list(filter(lambda a:a%2==0 ,[56,12,7,9,3,23,8])))

#Reduce

from functools import reduce
s=reduce(lambda a,b:a+b,[3,6,12,8])
print(s)

from functools import reduce
multi=reduce(lambda a,b:a*b,range(1,6))
print(multi)




