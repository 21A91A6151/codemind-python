x=input()
l=[]
c=0
for i in range(len(x)):
    if x[i] in 'aeiou':
        c+=1
    else:
        l.append(c)
        c=0
l.append(c)
print(max(l))