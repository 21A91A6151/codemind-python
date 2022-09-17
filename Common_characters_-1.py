x=input()
x=x.lower()
k=x.split()
c=0
s=k[0]
for i in s:
    for j in k:
        if i in j:
            continue
        else:
            break
    else:
        print(i,end="")
        c+=1
if c==0:
    print("-1")
