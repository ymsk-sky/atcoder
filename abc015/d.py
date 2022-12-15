W = int(input())
N, K = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(N)]
# dp[i][j][k]: i番目まででj枚使い幅がkのときの最大値
dp = [[[0] * (W + 1) for _ in range(K + 1)] for _ in range(2)]
for i in range(1, N + 1):
    a, b = abl[i - 1]
    for j in range(1, K + 1):
        if i < j:
            break
        for k in range(W + 1):
            # i枚目不採用
            dp[i%2][j][k] = dp[1 - i%2][j][k]
            # i枚目採用
            if k - a >= 0:
                dp[i%2][j][k] = max(dp[i%2][j][k], dp[1 - i%2][j - 1][k - a] + b)
ans = 0
for j in range(1, K + 1):
    for k in range(W + 1):
        ans = max(ans, dp[N%2][j][k])
print(ans)