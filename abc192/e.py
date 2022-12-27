import heapq

n, m, x, y = map(int, input().split())
x, y = x - 1, y - 1
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, t, k = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append((b, t, k))
    edges[b].append((a, t, k))
INF = float("inf")
dist = [INF] * n
que = []
heapq.heapify(que)
heapq.heappush(que, (0, x))
while que:
    cost, crt = heapq.heappop(que)
    if dist[crt] <= cost:
        continue
    dist[crt] = cost
    for nxt, t, k in edges[crt]:
        nxt_cost = t if cost%k == 0 else (k - cost%k)  + t
        if dist[nxt] <= cost + nxt_cost:
            continue
        heapq.heappush(que, (cost + nxt_cost, nxt))
ans = dist[y]
print(-1 if ans == INF else ans)