from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    edges[a - 1].append((w, b - 1))


vis = [[False] * (1 << 10) for _ in range(n)]
vis[0][0] = True
que = deque([(0, 0)])
while que:
    s, crt = que.popleft()
    for w, nxt in edges[crt]:
        t = s ^ w
        if vis[nxt][t]:
            continue
        vis[nxt][t] = True
        que.append((t, nxt))

for j in range(1 << 10):
    if vis[n - 1][j]:
        print(j)
        break
else:
    print(-1)
