n,k=map(int,input().split())
xs=list(map(int,input().split()))
m=float('inf')
for l,r in zip(xs,xs[k-1:]):
    d=min(abs(l),abs(r))+abs(r-l)
    m=min(m,d)
print(m)
