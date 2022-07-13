x=input()
x=x.lower()
c=0
s=[]
for i in x:
    if i==" ":
        continue
    if x.count(i)==1:
        if i not in s:
            s.append(i)
            c+=1
print(c)