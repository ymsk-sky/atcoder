n=int(input())
l=list(map(int,input().split()))
m=max(l)
dp=[0 for _ in range(m+1)]
for a in l:
    i=a
    if dp[a]!=0:
        dp[a]=2
    else:
        for _ in range(m):
            if i>m:
                break
            dp[i]+=1
            i+=a
ans=0
for a in l:
    if dp[a]==1:
        ans+=1
print(ans)
