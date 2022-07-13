x=input()
x=x.lower()
s=[]
for i in x:
    if i==" ":
        continue
    if x.count(i)==1:
        if i not in s:
            s.append(i)
print(len(s))