string_a=(input("Enter Word1:"))
string_b=(input("Enter Word2:"))
if(len(string_a)==len(string_b)):
    count = 0
    for i in string_a:
        if(i in string_b):
            count+=1
    if(count==len(string_b)):
        print("Anagram")
else:
    print ("Please Enter Words Of Same Length")