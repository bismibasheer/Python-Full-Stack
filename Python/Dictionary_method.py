student={"name":"ano","age":23,12:"python"}
print(student['name'])

print(student.get("place","no found"))

student.update({'place':"kochi"})
print(student)

student.pop(12)
print(student)

student.popitem()
print(student)


student.keys()
print(student)


student.values()
print(student)
  


student.items()
print(student)  

l=("Ram","mode","storage",7)
k="unknown"
laptop=dict.fromkeys(l,k)
print(laptop)    

for k,v in student.items():
    print(k,v)

l=("Ram","mode","storage",7)
k=("16GB","Dell","516GB")
print(list(zip(l,k)))

for i,v in enumerate(l,start=1):
    print(i,v)




