from collections import deque

n1, n2, m = map(int, input().split())
edges = [[] for _ in range(n1 + n2)]
for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)
INF = float("inf")

dist1 = [INF] * n1
dist1[0] = 0
que = deque([0])
while que:
    crt = que.popleft()
    for nxt in edges[crt]:
        if dist1[nxt] <= dist1[crt] + 1:
            continue
        dist1[nxt] = dist1[crt] + 1
        que.append(nxt)
d1 = max([d for d in dist1 if d != INF])

dist2 = [INF] * n2
dist2[n2 - 1] = 0
que = deque([n2 - 1])
while que:
    crt = que.popleft()
    for nxt in edges[crt + n1]:
        nxt -= n1
        if dist2[nxt] <= dist2[crt] + 1:
            continue
        dist2[nxt] = dist2[crt] + 1
        que.append(nxt)
d2 = max([d for d in dist2 if d != INF])

ans = d1 + d2 + 1
print(ans)
