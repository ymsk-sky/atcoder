n, m = map(int, input().split())
INF = float("inf")
dist = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a - 1][b - 1] = c
for i in range(n):
    dist[i][i] = 0

ans = 0
for k in range(n):
    for s in range(n):
        for t in range(n):
            if dist[s][t] > dist[s][k] + dist[k][t]:
                dist[s][t] = dist[s][k] + dist[k][t]
            if dist[s][t] != INF:
                ans += dist[s][t]
print(ans)