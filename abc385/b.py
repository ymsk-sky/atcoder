h, w, x, y = map(int, input().split())
sl = [input() for _ in range(h)]
t = input()

x, y = x - 1, y - 1
vis = [[0] * w for _ in range(h)]

for c in t:
    if c == "U":
        x = max(0, x - 1)
        if sl[x][y] == "#":
            x += 1
    elif c == "D":
        x = min(h - 1, x + 1)
        if sl[x][y] == "#":
            x -= 1
    elif c == "L":
        y = max(0, y - 1)
        if sl[x][y] == "#":
            y += 1
    elif c == "R":
        y = min(w - 1, y + 1)
        if sl[x][y] == "#":
            y -= 1
    if sl[x][y] == "@":
        vis[x][y] = 1

ans = sum([sum(v) for v in vis])
print(x + 1, y + 1, ans)
