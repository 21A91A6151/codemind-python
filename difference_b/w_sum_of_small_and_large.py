x=input()
x=x.split()
z=0
s=0
for i in x:
    k=min(i)
    s=s+ord(k)
    h=max(i)
    z=z+ord(h)
print(abs(z-s))