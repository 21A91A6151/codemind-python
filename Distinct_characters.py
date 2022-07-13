x=input()
x=x.lower()
s=[]
for i in x:
    if i==" ":
        continue
    if x.count(i)>=1:
        if i not in s:
            s.append(i)
k=sorted(s)
for i in k:
    print(i,end="")