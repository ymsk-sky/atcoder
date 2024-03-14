h, w, n = map(int, input().split())
t = input()
sl = [input() for _ in range(h)]
ans = 0
d = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
for i in range(1, h - 1):
    for j in range(1, w - 1):
        if sl[i][j] == "#":
            continue
        u, v = i, j
        for c in t:
            p, q = d[c]
            u, v = u + p, v + q
            if u < 0 or u >= h or v < 0 or v >= w:
                break
            if sl[u][v] == "#":
                break
        else:
            ans += 1
print(ans)
