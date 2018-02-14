s=input("Enter File Name:")
s=s+".txt"      #Adding .txt Implicitly
file1=open(s,"r")
file2=open("NewTest.txt","w+")
file2.write(file1.read())
file2.seek(0,0)
print(file2.read())