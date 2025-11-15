import copy
k=[[2,5],["Bismi",9]]
shallow=copy.copy(k)
shallow[1][0]
print("oringinal value",k)
print("shallow copy",shallow)



l=k=[[2,5],["Bismi",9]]
deep=copy.deepcopy(l)
deep[1][0]="Ano"
print("original value",l)
print("deep copy",deep)