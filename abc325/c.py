import sys
sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
sl = [input() for _ in range(h)]
l = [[0] * w for _ in range(h)]
def search(i, j):
    l[i][j] = 1
    for p in (-1, 0, 1):
        for q in (-1, 0, 1):
            if p == 0 and q == 0:
                continue
            u, v = i + p, j + q
            if u < 0 or u >= h or v < 0 or v >= w:
                continue
            if sl[u][v] == "#" and l[u][v] == 0:
                search(u, v)
cnt = 0
for i in range(h):
    for j in range(w):
        if sl[i][j] == ".":
            # センサでない
            continue
        if l[i][j]:
            # 既にカウント済み
            continue
        search(i, j)
        cnt += 1
print(cnt)
