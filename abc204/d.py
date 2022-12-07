n = int(input())
tl = list(map(int, input().split()))
INF = float("inf")
# dp[i][j]: i番目まで料理が終わっており, Aの時間がjのときのBの時間
dp = [[INF] * (n * 10**3 + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    t = tl[i - 1]
    for j in range(n * 10**3 + 1):
        # A使用
        if j - t >= 0:
            dp[i][j] = dp[i - 1][j - t]
        # B使用
        dp[i][j] = min(dp[i][j], dp[i - 1][j] + t)

ans = INF
for j in range(n * 10**3 + 1):
    # j:Aの時間, dp[n][j]:Bの時間
    tmp = max(j, dp[n][j])
    ans = min(ans, tmp)
print(ans)