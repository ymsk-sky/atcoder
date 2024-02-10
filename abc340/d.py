import heapq

n = int(input())
edges = [[] for _ in range(n)]
for i in range(n - 1):
    a, b, x = map(int, input().split())
    edges[i].append((a, i + 1))
    edges[i].append((b, x - 1))

INF = float("inf")
dist = [INF] * n

que = [(0, 0)]
heapq.heapify(que)

while que:
    cost, crt = heapq.heappop(que)
    if dist[crt] <= cost:
        continue
    dist[crt] = cost
    for nxt_cost, nxt in edges[crt]:
        if dist[nxt] <= cost + nxt_cost:
            continue
        heapq.heappush(que, (cost + nxt_cost, nxt))

print(dist[-1])
