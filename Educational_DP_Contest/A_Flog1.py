n = int(input())
l = list(map(int, input().split()))

dp = [10 ** 6 for _ in range(n)]

dp[0] = 0
dp[1] = abs(l[1] - l[0])

for i in range(2, n):
    dp[i] = min(abs(l[i] - l[i - 1]) + dp[i - 1], abs(l[i] - l[i - 2]) + dp[i - 2])

print(dp[n - 1])
