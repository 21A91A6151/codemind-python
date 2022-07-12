x=input()
x=x.lower()
y=input()
y=y.lower()
k=0
s=[]
for i in y:
    if i in x:
        if i in " ":
            continue
        if i not in s:
            s.append(i)
print(len(s))