n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
mod = 998244353
# dp[i][j]: i番目がj(0 or 1)のときの組み合わせ数
dp = [[0] * 2 for _ in range(n)]
dp[0] = [1, 1]
for i in range(n - 1):
    a1, b1 = l[i]
    a2, b2 = l[i + 1]
    if a1 != a2:
        dp[i + 1][0] += dp[i][0]
    if a1 != b2:
        dp[i + 1][1] += dp[i][0]
    if b1 != a2:
        dp[i + 1][0] += dp[i][1]
    if b1 != b2:
        dp[i + 1][1] += dp[i][1]
    dp[i + 1][0] %= mod
    dp[i + 1][1] %= mod
print(sum(dp[n - 1])%mod)
