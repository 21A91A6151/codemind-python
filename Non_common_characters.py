x=input()
x=x.lower()
y=input()
y=y.lower()
k=0
s=[]
for i in y:
    if i not in x:
        if i==" ":
            continue
        if i not in s:
            s.append(i)
for i in x:
    if i not in y:
        if i==" ":
            continue
        if i not in s:
            s.append(i)
print(len(s))