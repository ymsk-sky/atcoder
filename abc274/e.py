n, m = map(int, input().split())
xyl = [list(map(int, input().split())) for _ in range(n)]
pql = [list(map(int, input().split())) for _ in range(m)]

dist = [[0] * (n + m) for _ in range(n + m)]

for i in range(n + m):
    if i < n:
        a, b = xyl[i]
    else:
        a, b = pql[i - n]
    for j in range(i + 1, n + m):
        if j < n:
            c, d = xyl[j]
        else:
            c, d = pql[j - n]
        tmp = ((a - c) ** 2 + (b - d) ** 2) ** 0.5
        dist[i][j] = dist[j][i] = tmp

spd = 1

"""
1<=n<=12
0<=m<=5
-10**9<=x,y,p,q<=10**9
"""