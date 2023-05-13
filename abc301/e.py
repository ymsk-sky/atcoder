from collections import deque

h, w, t = map(int, input().split())
al = [input() for _ in range(h)]

si = sj = gi = gj = -1
for i in range(h):
    for j in range(w):
        if al[i][j] == "S":
            si, sj = i, j
        if al[i][j] == "G":
            gi, gj = i, j

INF = float("inf")
dist = [[[INF] * 19 for _ in range(w)] for _ in range(h)]
dist[si][sj][0] = 0
que = deque([(si, sj, 0)])
while que:
    i, j, cnt = que.popleft()
    for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        u, v = i + p, j + q
        if u < 0 or u >= h or v < 0 or v >= w:
            continue
        a = al[u][v]
        if a == "#":
            continue
        if a == "." or a == "G":
            pass
        elif a == "o":
            pass

for x in range(18, -1, -1):
    if dist[gi][gj][x] <= t:
        print(x)
        exit()
print(-1)

"""
1<=h,w<=300
1<=t<=2*10**6

"o"は18個以下
"""
