pos=int(input("enter Position:"))  #2 3 5 7 11
List=[]
for i in range(2,50):
    for j in range(2,i):
        if(i%j)==0:
           break
    else:
        List.append(i)
if pos in List:
    print("0")
else:
    for k in range(len(List)):
        if(pos < List[k]):
            print(List[k]-pos)
            break