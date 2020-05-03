n,m=map(int,input().split())
hs=list(map(int,input().split()))
ab=[list(map(int,input().split())) for _ in range(m)]

ans=[1]*n
for a,b in ab:
    if hs[a-1]>hs[b-1]:
        ans[b-1]=0
    elif hs[a-1]<hs[b-1]:
        ans[a-1]=0
    elif hs[a-1]==hs[b-1]:
        ans[a-1]=0
        ans[b-1]=0
print(sum(ans))
