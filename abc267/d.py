n, m = map(int, input().split())
al = list(map(int, input().split()))

INF = float("inf")

# dp[i][j]: i番目まででj個選んだ時の最大値
dp = [[-INF] * (m + 1) for _ in range(n + 1)]
dp[1][1] = al[0]

for i in range(1, n + 1):
    a = al[i - 1]
    for j in range(1, m + 1):
        if j > i:
            # 選択不可(選択数に対して母数が不足)
            pass
        elif n - i < m - j:
            # 選択不可(残り個数が不足する)
            pass
        elif j == 1:
            dp[i][j] = max(dp[i - 1][j], a)
        else:
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j - 1] + a * j)

print(max(dp[-1]))