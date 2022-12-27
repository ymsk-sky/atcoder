import heapq

INF = float("inf")
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
own = [INF] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    if a == b:
        own[a] = min(own[a], c)
    else:
        edges[a].append((c, b))
dists = []

for i in range(n):
    dist = [INF] * n
    que = []
    heapq.heapify(que)
    heapq.heappush(que, (0, i))
    while que:
        cost, crt = heapq.heappop(que)
        if dist[crt] < cost:
            continue
        dist[crt] = cost
        for nxt_cost, nxt in edges[crt]:
            if dist[nxt] < cost + nxt_cost:
                continue
            heapq.heappush(que, (cost + nxt_cost, nxt))
    dists.append(dist)

for i in range(n):
    ans = own[i]
    for j in range(n):
        if i == j:
            continue
        tmp = dists[i][j] + dists[j][i]
        ans = min(ans, tmp)
    print(-1 if ans == INF else ans)