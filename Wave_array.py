x=int(input())
l=list(map(int,input().split()))
h=0
if l[0]<l[1]:
    for i in range(0,len(l)-2,2):
        if l[i]<l[i+1] and l[i+1]>l[i+2]:
            pass
        else:
            h+=1
    if h==0:
        print("yes")
    else:
        print("no")
else:
    for i in range(0,len(l)-2,2):
        if l[i]>l[i+1] and l[i+1]<l[i+2]:
            pass
        else:
            h+=1
    if h==0:
        print("yes")
    else:
        print("no")