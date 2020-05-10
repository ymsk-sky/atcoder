n,m,x=map(int,input().split())
cas=[list(map(int,input().split())) for _ in range(n)]
ans=float('inf')
for i in range(1, 2**n):
    v=0
    us=[0]*m
    for b,ca in zip(bin(i)[2:].zfill(n), cas):
        b=int(b)
        if b==0:
            continue
        v+=ca[0]
        for j,a in enumerate(ca[1:]):
            us[j]+=a
    for u in us:
        fg=0
        if u<x:
            fg=1
            break
    if fg==0:
        ans=min(ans,v)
if i==2**n-1 and fg==1:
    print(-1)
    exit()
print(ans)
