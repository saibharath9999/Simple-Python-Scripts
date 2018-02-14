file=open("test.txt","w+")
file.write("Hello HoW Are You")
file.seek(0,0)  #To point cursor at beginning
print(file.read())