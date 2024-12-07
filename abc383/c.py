from collections import deque

INF = float("inf")

h, w, d = map(int, input().split())
sl = [input() for _ in range(h)]

que = deque([])
dist = [[INF] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if sl[i][j] == "H":
            dist[i][j] = 0
            que.append((i, j))

while que:
    i, j = que.popleft()
    for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        u, v = i + p, j + q
        if 0 > u or u >= h or 0 > v or v >= w:
            continue
        if sl[u][v] == "#":
            continue
        if dist[u][v] <= dist[i][j] + 1:
            continue
        dist[u][v] = dist[i][j] + 1
        if dist[u][v] < d:
            que.append((u, v))

ans = 0
for i in range(h):
    for j in range(w):
        if dist[i][j] <= d:
            ans += 1
print(ans)
