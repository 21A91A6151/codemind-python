x=input()
x=x.split()
s=[]
for i in x:
    s.append(i)
print(*s[::-1])