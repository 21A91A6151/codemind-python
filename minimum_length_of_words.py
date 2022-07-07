x=input()
x=x.split()
s=[]
for i in x:
    k=len(i)
    s.append(k)
print(min(s))