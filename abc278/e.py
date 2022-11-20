H, W, N, h, w = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(H)]

l = [[[0] * N for _ in range(W + 1)] for _ in range(H + 1)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        a = al[i - 1][j - 1]
        l[i][j][a - 1] += 1

for i in range(H):
    for j in range(W):
        for k in range(N):
            l[i + 1][j + 1][k] += l[i + 1][j][k]

for j in range(W):
    for i in range(H):
        for k in range(N):
            l[i + 1][j + 1][k] += l[i][j + 1][k]

ans = []
a = l[H][W]
def f(i, j):
    b = l[i - 1][j - 1]
    c = l[i - 1][j + w - 1]
    d = l[i + h - 1][j - 1]
    e = l[i + h - 1][j + w - 1]
    cnt = 0
    for x, y, z, u, v in zip(a, b, c, d, e):
        if x - (v - z - u + y) > 0:
            cnt += 1
    return cnt

for i in range(1, H - h + 2):
    tmp = []
    for j in range(1, W - w + 2):
        tmp.append(f(i, j))
    ans.append(tmp)
for an in ans:
    print(*an)
