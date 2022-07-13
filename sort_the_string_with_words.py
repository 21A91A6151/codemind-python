x=input()
x=x.lower()
x=x.split()
s=[]
for i in x:
    if i==" ":
        continue
    if i not in s:
        s.append(i)
print(*sorted(s))