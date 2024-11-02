import sys

sys.setrecursionlimit(10**8)

h, w, k = map(int, input().split())
sl = [input() for _ in range(h)]

vis = [[False] * w for _ in range(h)]
ans = 0
def dfs(i: int, j: int, cnt: int) -> None:
    if cnt == k:
        global ans
        ans += 1
        return
    vis[i][j] = True
    for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        u, v = i + p, j + q
        if 0 > u or u >= h or 0 > v or v >= w:
            continue
        if sl[u][v] == "#":
            continue
        if vis[u][v]:
            continue
        dfs(u, v, cnt + 1)
    vis[i][j] = False

for i in range(h):
    for j in range(w):
        if sl[i][j] == "#":
            continue
        dfs(i, j, 0)
print(ans)
