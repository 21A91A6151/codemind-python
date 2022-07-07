x=input()
c=0
s=[]
for i in x:
    if i in 'AEIOUaeiou':
        if i not in s:
            c+=1
            s.append(i)
            print(i,end=" ")
if(c==0):
    print("-1")