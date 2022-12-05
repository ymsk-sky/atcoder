n, p = map(int, input().split())
mod = 998244353
def inv(x):
    return pow(x, mod - 2, mod)

prob = p * inv(100) % mod

# dp[i]: 残りがiのときの回数の期待値
dp = [0] * (n + 2)
dp[-1] = dp[0] = 0

for i in range(1, n + 1):
    dp[i] = (dp[i - 2]*prob + dp[i - 1]*(1 - prob) + 1) % mod
print(dp[n])