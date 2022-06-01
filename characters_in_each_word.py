x=input()
s=0
for i in x:
    if i==" ":
        print(s,end=" ")
        s=0
    else:
        s+=1
print(s)
        