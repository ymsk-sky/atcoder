from itertools import product
n,h=map(int,input().split())
a,b,c,d,e=map(int,input().split())
ans=float('inf')
for p,q in zip(product((a,c,0),repeat=n),product((b,d,-e),repeat=n)):
    money=sum(p)
    health=h+sum(q)
    if health>=0:
        ans=min(ans,money)
print(ans)
