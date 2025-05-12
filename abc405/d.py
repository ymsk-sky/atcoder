from collections import deque

h, w = map(int, input().split())
sl = [input() for _ in range(h)]

tl = [[""] * w for _ in range(h)]
que = deque()
for i in range(h):
    for j in range(w):
        if sl[i][j] == "#":
            tl[i][j] = "#"
        elif sl[i][j] == "E":
            tl[i][j] = "E"
            que.append((i, j))

def f(p: int, q: int) -> str:
    if p == 0:
        return " <>"[q]
    return " ^v"[p]

while que:
    i, j = que.popleft()
    for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        u, v = i + p, j + q
        if 0 > u or u >= h or 0 > v or v >= w:
            continue
        if sl[u][v] == "#" or sl[u][v] == "E":
            continue
        if tl[u][v] != "":
            continue
        tl[u][v] = f(p, q)
        que.append((u, v))

for t in tl:
    print(*t, sep="")
