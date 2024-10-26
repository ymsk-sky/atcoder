n, m = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(m)]
s = set([(a - 1)*n + b for a, b in abl])
t = set()
ans = n**2 - m
for a, b in abl:
    for p, q in ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)):
        u, v = a + p, b + q
        if 1 > u or u > n or 1 > v or v > n:
            continue
        x = (u - 1)*n + v
        if x in s:
            continue
        if x in t:
            continue
        t.add(x)
        ans -= 1
print(ans)
