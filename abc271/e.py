n, m, k = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
el = list(map(int, input().split()))
