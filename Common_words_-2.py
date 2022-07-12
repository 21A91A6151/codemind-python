x=input()
y=input()
x=x.split()
y=y.split()
k=0
s=[]
for i in x:
    if y.count(i)==1 and x.count(i)==1:
        if i not in s:
            s.append(i)
            k+=1
print(len(s))