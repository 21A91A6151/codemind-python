x=input()
x=x.lower()
k=x.split()
c=0
for i in k:
    s=i
    h=i[::-1]
    if h==s:
        c+=1
    else:
        pass
print(c)
    
    