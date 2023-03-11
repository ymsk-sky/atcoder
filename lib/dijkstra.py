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

que = []
heapq.heapify(que)
heapq.heappush(que, (0, 0))

while que:
    cost, crt = heapq.heappop(que)
    if dist[crt] <= cost:
        continue
    dist[crt] = cost
    for nxt_cost, nxt in edges[crt]:
        if dist[nxt] <= cost + nxt_cost:
            continue
        heapq.heappush(que, (cost + nxt_cost, nxt))
