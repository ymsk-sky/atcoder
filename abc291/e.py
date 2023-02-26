from collections import deque

n, m = map(int, input().split())
edges = [set() for _ in range(n)]
tos = [0] * n
for _ in range(m):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    edges[x].add(y)
    tos[y] = 1

if tos.count(0) != 1:
    print("No")
    exit()

INF = float("inf")
dist = [INF] * n

que = deque()
for i in range(n):
    if tos[i] == 0:
        dist[i] = 0
        que.append((0, i))
        break
while que:
    cost, crt = que.popleft()
    for nxt in edges[crt]:
        if dist[nxt] <= cost - 1:
            continue
        dist[nxt] = cost - 1
        que.append((cost - 1, nxt))

if INF in dist or len(set(dist)) != n:
    print("No")
    exit()
 
dist = [abs(d) + 1 for d in dist]
print("Yes")
print(*dist)
