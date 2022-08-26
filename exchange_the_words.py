x=input()
k=x.split()
l=[]
for i in k:
    l.append(i)
l=l[::-1]
print(*l)