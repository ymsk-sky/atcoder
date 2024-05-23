h, w, n = map(int, input().split())
cl = [["."] * w for _ in range(h)]
i, j, k = 0, 0, 0
l = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for _ in range(n):
    if cl[i][j] == ".":
        cl[i][j] = "#"
        k += 1
    else:
        cl[i][j] = "."
        k -= 1
    p, q = l[k % 4]
    i = (i + p) % h
    j = (j + q) % w
for c in cl:
    print(*c, sep="")
