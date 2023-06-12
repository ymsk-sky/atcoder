h, w = map(int, input().split())
sl = [input() for _ in range(h)]
t = h
b = -1
r = w
l = -1
for i in range(h):
    for j in range(w):
        if sl[i][j] == "#":
            t = min(t, i)
            b = max(b, i)
            r = min(r, j)
            l = max(l, j)

for i in range(t, b + 1):
    for j in range(r, l + 1):
        if sl[i][j] == ".":
            print(i + 1, j + 1)
            exit()
