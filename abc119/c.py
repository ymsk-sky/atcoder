from itertools import product
n,a,b,c=map(int,input().split())
ls=[int(input()) for _ in range(n)]
ans=float('inf')
for p in product((0,1,2,3),repeat=n):
    if not ((1 in p) and (2 in p) and (3 in p)):
        continue
    x=0
    y=0
    z=0
    tmp=0
    for v,l in zip(p,ls):
        if v==0:
            continue
        if v==1:
            if x!=0:
                tmp+=10
            x+=l
        if v==2:
            if y!=0:
                tmp+=10
            y+=l
        if v==3:
            if z!=0:
                tmp+=10
            z+=l
    tmp+=(abs(x-a)+abs(y-b)+abs(z-c))
    ans=min(ans,tmp)
print(ans)
