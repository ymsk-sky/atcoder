n, p = map(int, input().split())
mod = 998244353

def inv(n):
    return pow(n, mod - 2, mod)

dp = [0] * (n + 1)
dp[n] = 1
dp[n - 1] = 100 * inv(100 - p) % mod

for i in range(n - 2, -1, -1):
    num = n - i
    dp[i] = dp[i + 1] * num * 100 * inv(100 - p) + dp[i + 2] * (num - 1) * 100 * inv(p)
    dp[i] %= mod

print(dp[0])

# print(281 * pow(100, mod - 2, mod) % mod)