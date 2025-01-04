from collections import deque

INF = float("inf")

h, w = map(int, input().split())
sl = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if sl[i][j] == "S":
            si, sj = i, j
        if sl[i][j] == "G":
            gi, gj = i, j

# dist[i][j][k]: k: 前回がk=0: 縦, k=1: 横 のときの最小回数
dist = [[[INF] * 2 for _ in range(w)] for _ in range(h)]
dist[si][sj] = [0, 0]
que = deque([(si, sj, 0), (si, sj, 1)])
while que:
    i, j, k = que.popleft()
    if k == 0:
        for p, q in ((0, 1), (0, -1)):
            u, v = i + p, j + q
            if 0 > u or u >= h or 0 > v or v >= w:
                continue
            if sl[u][v] == "#":
                continue
            if dist[u][v][1] <= dist[i][j][0] + 1:
                continue
            dist[u][v][1] = dist[i][j][0] + 1
            que.append((u, v, 1))
    else:
        for p, q in ((1, 0), (-1, 0)):
            u, v = i + p, j + q
            if 0 > u or u >= h or 0 > v or v >= w:
                continue
            if sl[u][v] == "#":
                continue
            if dist[u][v][0] <= dist[i][j][1] + 1:
                continue
            dist[u][v][0] = dist[i][j][1] + 1
            que.append((u, v, 0))

ans = min(dist[gi][gj])
print(-1 if ans == INF else ans)
