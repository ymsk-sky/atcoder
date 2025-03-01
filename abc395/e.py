import heapq

INF = float("inf")

n, m, x = map(int, input().split())
edges = [[] for _ in range(n)]
revs = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)
    revs[v].append(u)

dist = [[INF] * 2 for _ in range(n)]
dist[0][0] = 0
dist[0][1] = x

que = []
heapq.heappush(que, (0, 0, 0))
heapq.heappush(que, (x, 0, 1))

while que:
    cost, crt, rev = heapq.heappop(que)
    if dist[crt][rev] < cost:
        continue
    if rev:
        for nxt in revs[crt]:
            if dist[nxt][rev] <= cost + 1:
                continue
            dist[nxt][rev] = cost + 1
            heapq.heappush(que, (cost + 1, nxt, rev))
    else:
        for nxt in edges[crt]:
            if dist[nxt][rev] <= cost + 1:
                continue
            dist[nxt][rev] = cost + 1
            heapq.heappush(que, (cost + 1, nxt, rev))
    if dist[crt][1 - rev] > cost + x:
        heapq.heappush(que, (cost + x, crt, 1 - rev))

ans = min(dist[n - 1])
print(ans)
