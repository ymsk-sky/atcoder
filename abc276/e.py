h, w = map(int, input().split())
c = [input() for _ in range(h)]

si = sj = 0
for i in range(h):
    for j in range(w):
        if c[i][j] == "S":
            si, sj = i, j

dist = [[-1] * w for _ in range(h)]
dist[si][sj] = 0

def dfs(i, j):
    for u, v in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= i + u < h and 0 <= j + v < w:
            if c[i + u][j + v] == "#":
                continue
            if dist[i + u][j + v] > 0:
                continue
            elif dist[i + u][j + v] == 0:
                if dist[i][j] >= 3:
                    print("Yes")
                    exit()
            else:
                dist[i + u][j + v] = dist[i][j] + 1
                dfs(i + u, j + v)
                dist[i + u][j + v] = -1

dfs(si, sj)
print("No")