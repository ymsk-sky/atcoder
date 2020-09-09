w,h=map(int,input().split())
m=10**9+7
dp=[[0]*w for _ in range(h)]
dp[0][0]=1
for i in range(h):
    for j in range(w):
        v=0
        if j!=0:
            v+=dp[i][j-1]
        if i!=0:
            v+=dp[i-1][j]
        dp[i][j]+=v
print(dp[-1][-1]%m)
