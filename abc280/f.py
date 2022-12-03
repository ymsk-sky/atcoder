n, m, q = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append((c, b))
    edges[b].append((-c, a))

for _ in range(q):
    a, b = map(int, input().split())
