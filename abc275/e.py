N, M, K = map(int, input().split())
mod = 998244353
inv = pow(M, mod - 2, mod)
# dp[i][j]: マスjにいてi回目にkが出た
dp = [[0] * (N + 1) for _ in range(K + 1)]
dp[0][0] = 1
for i in range(1, K + 1):
    for j in range(N):
        for k in range(1, M + 1):
            if j + k > N:
                m = N - (j + k - N)
                dp[i][m] += dp[i - 1][j] * inv
                dp[i][m] %= mod
            else:
                dp[i][j + k] += dp[i - 1][j] * inv
                dp[i][j + k] %= mod
ans = 0
for i in range(K + 1):  # K回以下の和
    ans += dp[i][N]
    ans %= mod
print(ans % mod)