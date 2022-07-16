x=int(input())
max=0
min=0
for i in range(0,x+1):
    if 2**i<=x:
        max=i
for j in range(x+1):
    if 2**j>=x:
        min=j
        break
if abs(x-(2**max))<=abs(x-(2**min)):
    print(abs(x-(2**max)))
else:
    print(abs(x-(2**min)))