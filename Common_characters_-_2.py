x=input()
x=x.lower()
s=x.split()
k=s[0]
c=0
for i in k:
    for j in s:
        if i in j:
            continue
        else:
            break
    else:
        c+=1
print(c)