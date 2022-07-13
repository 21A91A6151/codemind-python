x=input()
s=[]
for i in x:
    if i in 'AEIOUaeiou':
        if i not in s:
            s.append(i)
print(*s)