n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append((v, w))
    edges[v].append((u, -w))

xl = [None] * n
for i in range(n):
    if xl[i] is not None:
        continue
    xl[i] = 0
    stack = [i]
    while stack:
        crt = stack.pop()
        for nxt, w in edges[crt]:
            if xl[nxt] is not None:
                continue
            xl[nxt] = xl[crt] + w
            stack.append(nxt)
print(*xl)
