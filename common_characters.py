x=input()
x=x.lower()
y=input()
y=y.lower()
l=[]
for i in x:
    if i in y:
        if i not in l:
            if i==" ":
                continue
            else:
                l.append(i)
k=sorted(l)
s=len(l)
if s==0:
    print("-1")
else:
    for i in k:
        print(i,end="")
        