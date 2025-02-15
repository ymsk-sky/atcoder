n, m = map(int, input().split())
edges = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    if u == v:
        continue
    if u in edges[v] and v in edges[u]:
        continue
    edges[u].add(v)
    edges[v].add(u)

ans = m - sum([len(e) for e in edges])//2
print(ans)
