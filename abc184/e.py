from collections import deque

h, w = map(int, input().split())
al = [input() for _ in range(h)]
warp = [[] for _ in range(26)]
si = sj = gi = gj = 0
for i in range(h):
    for j in range(w):
        if al[i][j] == "S":
            si, sj = i, j
        elif al[i][j] == "G":
            gi, gj = i, j
        elif al[i][j].isalpha():
            warp[ord(al[i][j]) - 97].append((i, j))
used = [0] * 26
move = ((0, 1), (0, -1), (1, 0), (-1, 0))
INF = float("inf")
dist = [[INF] * w for _ in range(h)]
dist[si][sj] = 0
que = deque([(si, sj)])

while que:
    i, j = que.popleft()
    cost = dist[i][j]
    for p, q in move:
        u, v = i + p, j + q
        if 0 <= u < h and 0 <= v < w:
            if dist[u][v] <= cost + 1 or al[u][v] == "#":
                continue
            dist[u][v] = cost + 1
            que.append((u, v))
    oc = ord(al[i][j])
    if 97 <= oc <= 122:
        if used[oc - 97]:
            continue
        used[oc - 97] = 1
        for u, v in warp[oc - 97]:
            if (i, j) == (u, v) or dist[u][v] <= cost + 1:
                continue
            dist[u][v] = cost + 1
            que.append((u, v))

ans = dist[gi][gj]
print(-1 if ans == INF else ans)