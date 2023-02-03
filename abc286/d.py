n, x = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]
dp = [[0] * (x + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    a, b = abl[i - 1]
    for j in range(b + 1):
        pass

print("Yes" if dp[n][x] else "No")


"""
1<=n<=50
1<=x<=10**4
1<=a<=100
1<=b<=50
"""
