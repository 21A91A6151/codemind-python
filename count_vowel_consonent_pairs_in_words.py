x=input()
x=x.lower()
s=x.split()
c=0
k=0
for i in s:
    for j in range(len(i)//2):
        if(i[j] in 'AEIOUaeiou') and i[-(j+1)] not in 'AEIOUaeiou)':
            c+=1
        if(i[j] not in 'AEIOUaeiou') and i[-(j+1)] in 'AEIOUaeiou)':
            c+=1
print(c)