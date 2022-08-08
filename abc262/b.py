n, m = map(int, input().split())
l = [[False] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    l[u - 1][v - 1] = True
    l[v - 1][u - 1] = True

ans = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if l[i][j] and l[j][k] and l[k][i]:
                ans += 1

print(ans)
