n,m=map(int,input().split())
kss=[list(map(int,input().split())) for _ in range(m)]
ps=list(map(int,input().split()))
ans=0
for i in range(2**n):
    stt=bin(i)[2:].zfill(n)
    cmp=0
    for ks,p in zip(kss, ps):
        c=0
        for k in ks[1:]:
            if stt[k-1]=='1':
                c+=1
        if c%2==p:
            cmp+=1
        else:
            break
    if cmp==m:
        ans+=1
print(ans)
