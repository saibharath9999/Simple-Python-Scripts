n=input("Enter")
L=[]
NL=[]
count=0
for i in n:
   L.append(i)
for i in range(1,len(n)+1):
    i=n[-i]
    NL.append(i)
for i in range(len(n)):
    if L[i]==NL[i]:
        count+=1
if count==len(n):
    print("palindrome")
