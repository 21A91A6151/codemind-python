x=input()
s=x[::-1]
z='AEIOUaeiou'
c=0
k=0
for i in range(len(x)//2):
    if x[i] in z and s[i] not in z:
        if x[i]!=' ':
            if s[i]!=' ':
                c+=1
    elif x[i] not in z and s[i] in z:
        if x[i]!=' ':
            if s[i]!=' ':
                c+=1
print(c)