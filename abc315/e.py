from collections import deque

n = int(input())
edges = []
for i in range(n):
    c, *pl = list(map(int, input().split()))
    pl = [p - 1 for p in pl]
    edges.append(pl)

INF = float("inf")
dist = [INF] * n
dist[0] = 0

que = deque([0])
ans = []
while que:
    crt = que.popleft()
    for nxt in edges[crt]:
        if dist[nxt] <= dist[crt] + 1:
            continue
        dist[nxt] = dist[crt] + 1
        que.append(nxt)
        ans.append(nxt + 1)

print(*ans[::-1])
