n,k=map(int,input().split())
lrs=[list(map(int,input().split())) for _ in range(k)]
m=998244353
dp=[0]*(n+1)
s=[0]*(n+1)
dp[1]=1
s[1]=1
for i in range(1,n+1):
    for l,r in lrs:
        dp[i]+=(s[max(i-l,0)]-s[max(i-r-1,0)])%m
    s[i]=(s[i-1]+dp[i])%m
print(dp[n]%m)
