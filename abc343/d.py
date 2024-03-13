n, t = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(t)]

points = [0] * n
d = {0: n}
k = 1
for a, b in abl:
    p = points[a - 1]
    d[p] -= 1
    if d[p] == 0:
        del d[p]
        k -= 1
    points[a - 1] += b
    p = points[a - 1]
    if p in d:
        d[p] += 1
    else:
        d[p] = 1
        k += 1
    print(k)
