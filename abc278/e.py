H, W, N, h, w = map(int, input().split())
l = [[[0] * N for _ in range(W + 1)] for _ in range(H + 1)]
for i in range(1, H + 1):
    al = list(map(int, input().split()))
    for j in range(1, W + 1):
        l[i][j][al[j - 1] - 1] = 1

# 右方向へ累積和
for i in range(H):
    for j in range(W):
        for k in range(N):
            l[i + 1][j + 1][k] += l[i + 1][j][k]
# 下方向へ累積和
for j in range(W):
    for i in range(H):
        for k in range(N):
            l[i + 1][j + 1][k] += l[i][j + 1][k]

ans = []
for i in range(1, H - h + 2):
    tmp = []
    for j in range(1, W - w + 2):
        cnt = 0
        for k in range(N):
            num = (l[i - 1][j - 1][k] - l[i - 1][j + w - 1][k]
                   - l[i + h - 1][j - 1][k] + l[i + h - 1][j + w - 1][k])
            if l[H][W][k] - num > 0:
                cnt += 1
        tmp.append(cnt)
    ans.append(tmp)
for an in ans:
    print(*an)