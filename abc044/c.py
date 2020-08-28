from itertools import product
n,a=map(int,input().split())
l=list(map(int,input().split()))
ans=0
for p in product((0,1),repeat=n):
    s=0
    c=0
    for i,b in enumerate(p):
        if b==1:
            s+=l[i]
            c+=1
    if c!=0 and s/c==a:
        ans+=1
print(ans)
