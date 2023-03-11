from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)

INF = float("inf")
dist = [INF] * n
dist[0] = 0

que = deque([0])
while que:
    crt = que.popleft()
    for nxt in edges[crt]:
        if dist[nxt] <= dist[crt] + 1:
            continue
        dist[nxt] = dist[crt] + 1
        que.append(nxt)
