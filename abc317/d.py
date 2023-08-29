n = int(input())
xyzl = [list(map(int, input().split())) for _ in range(n)]
M = sum([z for _, _, z in xyzl])
INF = float("inf")
# dp[i][j]: i番目まででj議席を獲得できる最小の鞘替え数
dp = [[INF] * (M + 1) for _ in range(n + 1)]
dp[0][0] = 0

def calc(x, y):
    if x > y:
        return 0
    dif = y - x
    return -(-dif//2)

for i in range(1, n + 1):
    x, y, z = xyzl[i - 1]
    for j in range(M + 1):
        d = calc(x, y)
        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - z] + d)

ans = INF
for i in range(1, n + 1):
    for j in range(-(-M//2), M + 1):
        if ans > dp[i][j]:
            ans = dp[i][j]
print(ans)
