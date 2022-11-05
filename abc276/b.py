n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b)
    g[b - 1].append(a)
for a in g:
    print(len(a), *sorted(a))