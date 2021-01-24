n=int(input())
al=list(map(int,input().split()))
ans=0
for l in range(n):
    x=al[l]
    for r in range(l,n):
        x=min(x,al[r])
        ans=max(ans,x*(r-l+1))
print(ans)
