s=input()
t='chokudai'
mod=10**9+7
n=len(s)
dp=[[-1]*9 for _ in range(n+1)]
for i in range(n+1):
    for j in range(9):
        if j==0:
            dp[i][j]=1
        else:
            if i==0:
                dp[i][j]=0
            else:
                if s[i-1]==t[j-1]:
                    dp[i][j]=(dp[i-1][j]+dp[i-1][j-1])%mod
                else:
                    dp[i][j]=dp[i-1][j]
print(dp[n][8])
