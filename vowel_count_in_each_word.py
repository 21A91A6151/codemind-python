x=input()
x=x.split()
a=0
for i in x:
    for j in i:
        if j in 'aeiou':
            a+=1
    print(a,end=" ")
    a=0