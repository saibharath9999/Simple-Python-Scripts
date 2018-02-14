n=int(input("enter range:"))
for i in range(n+1):
    count = 0
    i=str(i)
    length=len(i)
    for j in i:
        j=int(j)
        if(j==2):
            count+=1
    if(count==length):
        print(i)