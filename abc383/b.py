h, w, d = map(int, input().split())
sl = [input() for _ in range(h)]
ans = 0
l = []
for i in range(h):
    for j in range(w):
        if sl[i][j] == ".":
            l.append((i, j))
m = len(l)
for a in range(m):
    i0, j0 = l[a]
    for b in range(a, m):
        i1, j1 = l[b]
        state = [[0] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if sl[i][j] == "#":
                    continue
                if abs(i - i0) + abs(j - j0) <= d:
                    state[i][j] = 1
                if abs(i - i1) + abs(j - j1) <= d:
                    state[i][j] = 1
        tmp = sum([sum(s) for s in state])
        ans = max(ans, tmp)
print(ans)
