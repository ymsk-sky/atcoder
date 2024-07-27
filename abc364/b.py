h, w = map(int, input().split())
si, sj = map(int, input().split())
cl = [input() for _ in range(h)]
x = input()
i, j = si - 1, sj - 1
for m in x:
    p, q = 0, 0
    if m == "L":
        q = -1
    elif m == "R":
        q = 1
    elif m == "U":
        p = -1
    elif m == "D":
        p = 1
    u, v = i + p, j + q
    if 0 > u or u >= h or 0 > v or v >= w:
        continue
    if cl[u][v] == "#":
        continue
    i, j = u, v
print(i + 1, j + 1)
