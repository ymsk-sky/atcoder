INF = float("inf")
n, x, k = map(int, input().split())
pucl = [list(map(int, input().split())) for _ in range(n)]

cs = set([c for _, _, c in pucl])
for i in range(1, n + 1):
    if i not in cs:
        pucl.append([0, 0, i])

pucl.sort(key=lambda e: e[2])
m = len(pucl)

# dp[c][j]: 色c以下をj円分購入のときの最大値
dp = [[-INF] * (x + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, m + 1):
    p, u, c = pucl[i - 1]
    if p == u == 0:
        dp[c] = dp[c - 1][:]
        continue
    for j in range(x, -1, -1):
        dp[c][j] = max(dp[c][j], dp[c - 1][j])
        if j - p < 0:
            continue
        dp[c][j] = max(dp[c][j], dp[c - 1][j - p] + u + k, dp[c][j - p] + u)

ans = max(dp[n])
print(ans)
