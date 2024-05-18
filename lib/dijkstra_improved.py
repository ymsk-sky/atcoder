"""先に値を更新するように修正
計算量がこちらのほうが少なくなる
"""

import heapq

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append((w, v - 1))
    edges[v].append((w, u - 1))

INF = float("inf")
dist = [INF] * n
dist[0] = 0

que = [(0, 0)]
heapq.heapify(que)
while que:
    cost, crt = heapq.heappop(que)
    if dist[crt] < cost:
        continue
    for nxt_cost, nxt in edges[crt]:
        if dist[nxt] <= cost + nxt_cost:
            continue
        dist[nxt] = cost + nxt_cost
        heapq.heappush(que, (cost + nxt_cost, nxt))

print(*dist)
