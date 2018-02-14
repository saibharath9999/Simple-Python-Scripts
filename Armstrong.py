Num=str((input("Enter Number:")))
length=len(Num)
sum=0
for i in Num:
    i=int(i)
    sum=sum+i**length
    if(sum == int(Num)):
        print("Armstrong")
