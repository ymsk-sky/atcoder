from collections import deque

h, w = map(int, input().split())
sl = [input() for _ in range(h)]
nxt_chr = {"s": "n", "n": "u", "u": "k", "k": "e", "e": "s"}

vis = [[0] * w for _ in range(h)]
vis[0][0] = 1
que = deque([(0, 0)])
while que:
    i, j = que.popleft()
    crt = sl[i][j]
    for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        u, v = i + p, j + q
        if u < 0 or u >= h or v < 0 or v >= w:
            continue
        if vis[u][v]:
            continue
        if not sl[u][v] in nxt_chr:
            continue
        if sl[u][v] == nxt_chr[crt]:
            vis[u][v] = 1
            que.append((u, v))

print("Yes" if vis[h - 1][w - 1] else "No")

"""
snukeの順
"""
