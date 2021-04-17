from math import gcd
a,b=map(int,input().split())
ans=1
for x in range(a,b):
    l=[]
    for y in range(x+1,b+1):
        y2=y%x
        if y2 in l:
            break
        tmp=gcd(y2,x)
        ans=max(ans,tmp)
print(ans)
