from sys import stdin
from collections import deque

def solve():
    input = stdin.readline

    n = int(input())
    sl = [list(input()) for _ in range(n)]
    pl = []
    for i in range(n):
        for j in range(n):
            if sl[i][j] == "P":
                pl.append((i, j))
    (i1, j1), (i2, j2) = pl
    INF = 10**10
    # dist[i][j]: i=i1*n+j1, j=i2*n+j2, p1=(i1, i1), p2=(i2, j2)の最小回数
    dist = [[INF] * n**2 for _ in range(n**2)]
    dist[i1*n + j1][i2*n + j2] = 0
    que = deque([(i1*n + j1, i2*n + j2)])
    while que:
        i, j = que.popleft()
        if i == j:
            # BFS(=距離近い順に処理しているので見つかったらそこで打ち切ってよい)
            break
        i1, j1, i2, j2 = i//n, i%n, j//n, j%n
        d = dist[i][j]
        for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            u1 = min(n - 1, max(0, i1 + p))
            v1 = min(n - 1, max(0, j1 + q))
            u2 = min(n - 1, max(0, i2 + p))
            v2 = min(n - 1, max(0, j2 + q))
            if sl[u1][v1] == "#":
                u1, v1 = i1, j1
            if sl[u2][v2] == "#":
                u2, v2 = i2, j2
            if dist[u1*n + v1][u2*n + v2] <= d + 1:
                continue
            dist[u1*n + v1][u2*n + v2] = d + 1
            que.append((u1*n + v1, u2*n + v2))
    ans = INF
    for i in range(n):
        for j in range(n):
            ans = min(ans, dist[i*n + j][i*n + j])
    print(-1 if ans == INF else ans)

solve()

"""
2<=n<=60
"""