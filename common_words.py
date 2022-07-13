x=input()
x=x.lower()
y=input()
y=y.lower()
y=y.split()
x=x.split()
k=0
s=[]
for i in y:
    if i in x:
        if i not in s:
            s.append(i)
print(*s)