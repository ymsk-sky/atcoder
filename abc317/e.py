from bisect import bisect_right
from collections import deque

h, w = map(int, input().split())
al = [input() for _ in range(h)]

X = set("#>V<^")

si, sj, gi, gj = -1, -1, -1, -1
xl = {i: [-1] for i in range(h)}
yl = {i: [-1] for i in range(w)}
for i in range(h):
    for j in range(w):
        a = al[i][j]
        if a == "S":
            si, sj = i, j
        if a == "G":
            gi, gj = i, j
        if a in X:
            xl[i].append(j)
            yl[j].append(i)

dist = [[-1] * w for _ in range(h)]
dist[si][sj] = 0
que = deque([(si, sj)])
while que:
    i, j = que.popleft()
    for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        u, v = i + p, j + q
        if u < 0 or u >= h or v < 0 or v >= w:
            continue
        if al[u][v] in X:
            continue
        if dist[u][v] != -1:
            continue
        dist[u][v] = dist[i][j] + 1
        que.append((u, v))

print(*dist, sep="\n")
print(dist[gi][gj])
