from itertools import permutations

n, m, r = map(int, input().split())
xl = list(map(lambda x: int(x) - 1, input().split()))
INF = float("inf")
dist = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    dist[a][b] = dist[b][a] = c
for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = INF
for per in permutations(xl):
    tmp = 0
    for x, y in zip(per, per[1:]):
        tmp += dist[x][y]
    ans = min(ans, tmp)
print(ans)