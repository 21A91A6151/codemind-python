x=input()
x=x.split()
x=reversed(x)
for i in x:
    k=i[::-1]
    print(k,end=" ")