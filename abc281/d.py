N, K, D = map(int, input().split())
al = list(map(int, input().split()))

# dp[i][j][k]: i番目までのj個の和をDで割った余りがkとなるときの最大値
dp = [[[-1] * D for _ in range(K + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0
for i in range(N):
    a = al[i]
    for j in range(K + 1):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue
            # i番目を選ばない場合
            dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
            # i番目を選ぶ場合
            if j != K:
                dp[i + 1][j + 1][(k + a)%D] = max(dp[i + 1][j + 1][(k + a)%D], dp[i][j][k] + a)

print(dp[N][K][0])