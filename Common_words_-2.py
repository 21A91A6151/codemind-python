x=input()
y=input()
y=y.split()
x=x.split()
k=0
for i in x:
    if i in y:
        if y.count(i)==1 and x.count(i)==1:
            k+=1
print(k)