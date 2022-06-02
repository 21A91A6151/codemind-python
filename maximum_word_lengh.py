x=input()
x=x.split()
z=0
for i in x:
    k=len(i)
    if(k>z):
        z=k
    else:
        continue
print(z)