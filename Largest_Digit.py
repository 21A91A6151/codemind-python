x=int(input())
c=0
while x:
    d=x%10
    x=x//10
    if(d>=c):
        c=d
print(c)