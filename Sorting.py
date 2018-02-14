L=[]
for i in range(5):
    n=int(input("Enter Num:"))
    L.append(n)
NL=[]
while L:
    min=L[0]       #L[5,3,1,0]
    for x in L:
        if x < min:
            min=x
    NL.append(min)
    L.remove(min)
print(NL)
j=1
for i in range(len(NL)):
    if NL[i]==NL[-j]:
        print(NL[i])
        break
    print(NL[i])
    print(NL[-j])
    j+=1