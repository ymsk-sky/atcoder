h, w = map(int, input().split())
cl = [input() for _ in range(h)]
n = min(h, w)
sl = [0] * n

for a in range(h):
    for b in range(w):
        if cl[a][b] != "#":
            continue
        n = 0
        f = 0
        while 1:
            for p, q in ((n + 1, n + 1), (n + 1, -(n + 1)), (-(n + 1), n + 1), (-(n + 1), -(n + 1))):
                u, v = a + p, b + q
                if 0 > u or u >= h or 0 > v or v >= w:
                    f = 1
                    break
                if cl[u][v] != "#":
                    f = 1
                    break
            if f:
                break
            n += 1
        if n != 0:
            sl[n - 1] += 1

print(*sl)
