t = input()
l = len(t)
n = int(input())
sll = []
for _ in range(n):
    _, *sl = input().split()
    sll.append(sl)
INF = float("inf")
# dp[i][j]: i番目の袋の何れかを使ってtのj番目までを作るときの最小金額
dp = [[INF] * (l + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    sl = sll[i - 1]
    for j in range(l + 1):
        dp[i][j] = dp[i - 1][j]
    for s in sl:
        m = len(s)
        for j in range(1, l - m + 2):
            if s == t[j - 1:j - 1 + m]:
                dp[i][j + m - 1] = min(dp[i][j + m - 1], dp[i - 1][j - 1] + 1)

ans = min([dp[i][l] for i in range(n + 1)])
print(-1 if ans == INF else ans)
