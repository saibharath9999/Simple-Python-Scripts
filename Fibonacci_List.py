'''fibo=[0,1]
for i in range (5):
    fibo.append(fibo[-1]+fibo[-2])

print (fibo)'''


def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

Terms=int(input("Enter NUmber:"))
if (Terms < 0):
    print("Enter positive Number")
else:
    for i in range(Terms):
        print(fibo(i))

