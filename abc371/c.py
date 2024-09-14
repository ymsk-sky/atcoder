from itertools import permutations

n = int(input())
m_g = int(input())
uvl = [list(map(int, input().split())) for _ in range(m_g)]

m_h = int(input())
edges_h = [[False] * n for _ in range(n)]
for _ in range(m_h):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges_h[a][b] = edges_h[b][a] = True
al_l = []
for _ in range(n - 1):
    al = list(map(int, input().split()))
    al_l.append(al)

ans = float("INF")
for per in permutations(range(n)):
    edges_g = [[False] * n for _ in range(n)]
    for u, v in uvl:
        u, v = u - 1, v - 1
        edges_g[per[u]][per[v]] = edges_g[per[v]][per[u]] = True
    tmp = 0
    for i in range(n):
        for j in range(i + 1, n):
            if edges_g[i][j] == edges_h[i][j]:
                continue
            tmp += al_l[i][j - i - 1]
    ans = min(ans, tmp)
print(ans)
