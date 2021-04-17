from math import gcd
a,b=map(int,input().split())
ans=1
for x in range(a,b):
    for y in range(x+1,b+1):
        if x>=y:
            break
        tmp=gcd(x,y)
        ans=max(ans,tmp)
print(ans)
