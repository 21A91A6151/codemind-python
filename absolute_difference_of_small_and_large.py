x=input()
x=x.split()
for i in x:
    k=min(i)
    h=max(i)
    print(abs(ord(k)-ord(h)),end=" ")