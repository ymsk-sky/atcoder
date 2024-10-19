import heapq

INF = float("inf")
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
revrs = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append(b)
    revrs[b].append(a)

dist = [INF] * n
dist[0] = 0
que = [(0, 0)]
while que:
    cost, crt = heapq.heappop(que)
    if dist[crt] < cost:
        continue
    for nxt in edges[crt]:
        if dist[nxt] <= cost + 1:
            continue
        dist[nxt] = cost + 1
        heapq.heappush(que, (cost + 1, nxt))

dist_rev = [INF] * n
dist_rev[0] = 0
que = [(0, 0)]
while que:
    cost, crt = heapq.heappop(que)
    if dist_rev[crt] < cost:
        continue
    for nxt in revrs[crt]:
        if dist_rev[nxt] <= cost + 1:
            continue
        dist_rev[nxt] = cost + 1
        heapq.heappush(que, (cost + 1, nxt))

ans = INF
for i in range(1, n):
    tmp = dist[i] + dist_rev[i]
    ans = min(ans, tmp)
print(-1 if ans == INF else ans)
