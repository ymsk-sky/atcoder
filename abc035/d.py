import heapq

n, m, t = map(int, input().split())
al = list(map(int, input().split()))
edges = [[] for _ in range(n)]  # 行き
rvses = [[] for _ in range(n)]  # 帰り
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append((c, b))
    rvses[b].append((c, a))
INF = float("inf")
dist = [INF] * n
que = []
heapq.heapify(que)
heapq.heappush(que, (0, 0))
while que:
    cost, crt = heapq.heappop(que)
    if dist[crt] < cost:
        continue
    dist[crt] = cost
    for nxt_cost, nxt in edges[crt]:
        if dist[nxt] < cost + nxt_cost:
            continue
        heapq.heappush(que, (cost + nxt_cost, nxt))
bist = [INF] * n
heapq.heappush(que, (0, 0))
while que:
    cost, crt = heapq.heappop(que)
    if bist[crt] < cost:
        continue
    bist[crt] = cost
    for nxt_cost, nxt in rvses[crt]:
        if bist[nxt] < cost + nxt_cost:
            continue
        heapq.heappush(que, (cost + nxt_cost, nxt))

ans = 0
for i in range(n):
    remain = max(0, t - (dist[i] + bist[i]))
    tmp = remain*al[i]
    ans = max(ans, tmp)
print(ans)