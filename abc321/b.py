n, x = map(int, input().split())
al = list(map(int, input().split()))
INF = float("inf")
ans = INF
for s in range(100, -1, -1):
    l = al.copy() + [s]
    a = max(l)
    b = min(l)
    if sum(l) - a - b >= x:
        ans = s
print(-1 if ans == INF else ans)
