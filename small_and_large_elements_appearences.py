x=input()
l=[]
k=[]
for i in x:
    if i==" ":
        continue
    if i in l:
        pass
    else:
        l.append(i)
for i in l:
    s=x.count(i)
    k.append(s)
m=min(l)
n=max(l)
w=l.index(m)
y=l.index(n)
a=k[w]
b=k[y]
print(m,a,n,b)