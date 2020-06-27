x=int(input())
a=1
for b in range(1,x+1):
    for p in range(2,x+1):
        t=b**p
        if t>x:
            break
        a=max(a,t)
print(a)
