n=input("enter:")
count=0
for i in range(0,len(n)):
    for j in range(len(n)-1,0,-1):
        if n[i]==n[j]:
            count+=1
            break
if count==len(n):
    print("palindrome")
else:
    print("not")


