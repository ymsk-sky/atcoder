n,k=map(int,input().split())
hs=sorted([int(input()) for _ in range(n)])
m=float('inf')
for l,h in zip(hs,hs[k-1:]):
    m=min(m,h-l)
print(m)
