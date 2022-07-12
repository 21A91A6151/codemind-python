x=input()
x=x.lower()
x=x.split()
s=[]
for i in x:
    s.append(i)
k=sorted(s)
print(*k)