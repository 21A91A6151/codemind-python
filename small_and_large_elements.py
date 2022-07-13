x=input()
x=x.split()
s=[]
for i in x:
    s.append(i)
print(min(s[0]),end=" ")
print(max(s[-1]),end=" ")