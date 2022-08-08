n, k = map(int, input().split())
l = list(map(int, input().split()))

dp = [10 ** 6 for _ in range(n)]

dp[0] = 0
dp[1] = abs(l[1] - l[0])

for i in range(2, n):
    dp[i] = abs(l[i] - l[i - 1]) + dp[i - 1]
    for j in range(2, k + 1):
        if i - j >= 0:
            dp[i] = min(dp[i], abs(l[i] - l[i - j]) + dp[i - j])

print(dp[n - 1])
