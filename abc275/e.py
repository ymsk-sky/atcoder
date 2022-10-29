n, m, k = map(int, input().split())
mod = 998244353

# dp[i][j]: i回目にjへこれる確率
dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[0][0] = 1

for i in range(k):
    for j in range(n + 1):
        for deme in range(1, m + 1):
            if j + deme > n:
                j2 = (j + deme) % n + 1
                dp[i + 1][-j2] += dp[i][j]
            else:
                dp[i + 1][j + deme] += dp[i][j]

x = sum(dp[k])
y = dp[k][n]
