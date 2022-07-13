x=input()
x=x.split()
for i in x:
    k=max(i)
    h=min(i)
    print(abs(ord(k)-ord(h)),end=" ")