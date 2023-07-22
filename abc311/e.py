h, w, n = map(int, input().split())
abl = set([tuple(map(int, input().split())) for _ in range(n)])

dp = [[-1] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if (i + 1, j + 1) in abl:
            dp[i][j] = 0
        else:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

ans = 0
for i in range(h):
    ans += sum(dp[i])
print(ans)

"""
1<=h,w<=3000
0<=n<=min(h*w, 10**5)
"""
