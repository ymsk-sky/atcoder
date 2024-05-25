n, t = map(int, input().split())
al = list(map(int, input().split()))

bingo = [[0] * n for _ in range(n)]
for x, a in enumerate(al, start=1):
    a -= 1
    bingo[a//n][a%n] = x
INF = float("inf")
ans = INF
for i in range(n):
    # 縦
    l = bingo[i]
    if 0 not in l:
        ans = min(ans, max(l))
    # 横
    l = [bingo[j][i] for j in range(n)]
    if 0 not in l:
        ans = min(ans, max(l))
# 斜め
l = [bingo[i][i] for i in range(n)]
if 0 not in l:
    ans = min(ans, max(l))
l = [bingo[i][n - i - 1] for i in range(n)]
if 0 not in l:
    ans = min(ans, max(l))

print(-1 if ans == INF else ans)
