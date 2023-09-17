m = int(input())
sl = [input()*3 for _ in range(3)]
M = 3 * m
INF = float("inf")
ans = INF
for i in range(M):
    for j in range(M):
        if i == j:
            continue
        if sl[0][i] != sl[1][j]:
            continue
        for k in range(M):
            if k == i or k == j:
                continue
            if sl[0][i] == sl[2][k]:
                tmp = max(i, j, k)
                ans = min(ans, tmp)
print(-1 if ans == INF else ans)
