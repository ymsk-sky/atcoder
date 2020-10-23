n,m=map(int,input().split())
stairs=[1]*(n+1)
mod=10**9+7
# 階段の壊れている位置
for _ in range(m):
    a=int(input())
    stairs[a]=0
# 動的計画法(DP法)
dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    if stairs[i]:
        dp[i]=dp[i-1]+dp[i-2]
print(dp[-1]%mod)
