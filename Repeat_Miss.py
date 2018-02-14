L=[]
p=int(input("Enter a range:"))
for i in range(p):
    n=int(input("Enter Num:"))
    L.append(n)
for i in range(p):
    if i not in L:
        print ("Missng",i)
for j in range(p-1):
    if (int(L[j]) == int(L[j+1])):
        print ("Repeated",L[j])

print (L)
