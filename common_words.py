x=input()
x=x.lower()
y=input()
y=y.lower()
x=x.split()
y=y.split()
for i in y:
    if i in x:
        print(i,end=" ")