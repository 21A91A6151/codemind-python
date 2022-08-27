x=input()
x=x.split()
z=x[-1]
k=min(z)
s=k.lower()
if s in z:
    print(s)
else:
    print(k)