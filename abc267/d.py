n, m = map(int, input().split())
al = list(map(int, input().split()))

p = [[0] * m for _ in range(n)]
for i in range(n):
    a = al[i]
    for j in range(m):
        p[i][j] = (j + 1) * a

bl = [[a, i] for i, a in enumerate(al)]
bl.sort(reverse=True)

ans = -float("inf")

for i in range(n - m + 1):
    tmp = 0
    cl = bl[i:i + m]
    cl.sort(key=lambda a: a[1])
    for j, (a, i) in enumerate(cl):
        tmp += p[i][j]
    ans = max(ans, tmp)

print(ans)

"""
   1    2    3    4
-3 1 -4 1 -5 9 -2 6 -5 3
[9, 6, 3, 1, 1, -2, -3, -4, -5, -5]

1+18+18+12
1+2+27+24
54
"""
