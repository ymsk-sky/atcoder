n, x, y = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(n)]
INF = float("inf")
# dp[i][j][k]: i番目までからj個を選出して甘さがkのときの最小しょっぱさ
dp = [[[INF] * (x + 1) for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0][0] = 0
for i in range(1, n + 1):
    a, b = abl[i - 1]
    dp[i][0][0] = dp[i - 1][0][0]
    for j in range(1, i + 1):
        for k in range(x + 1):
            dp[i][j][k] = dp[i - 1][j][k]
            if k - a >= 0:
                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][k - a] + b)
ans = 0
for j in range(n + 1):
    for k in range(x + 1):
        if dp[n][j][k] <= y:
            ans = max(ans, j)
print(min(ans + 1, n))


"""
1<=n<=80
1<=a,b<=10**4
1<=x,y<=10**4
"""
