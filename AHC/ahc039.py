M = 10**5
n = int(input())  # 5000固定
saba = [list(map(int, input().split())) for _ in range(n)]
iwashi = [list(map(int, input().split())) for _ in range(n)]

# 1000x1000のブロックごとに分けて各ブロックの(saba - iwasi + 1)が正になる所を探索
BLOCK_H = BLOCK_W = 50000  # 2x2箇所
H = W = M // BLOCK_H
sl = [[0] * (W + 1) for _ in range(H + 1)]  # 左上(0, 0), 右下(i, j)の矩形のスコア(=累積和)
for i in range(1, H + 1):
    for j in range(1, W + 1):
        x, y = j * BLOCK_W, i * BLOCK_H
        score = 0
        for (x_saba, y_saba), (x_iwashi, y_iwashi) in zip(saba, iwashi):
            if x_saba <= x and y_saba <= y:
                score += 1
            if x_iwashi <= x and y_iwashi <= y:
                score -= 1
        sl[i][j] = score

# 採用箇所判定
use = [[False] * W for _ in range(H)]
cnt = 0
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if sl[i][j] + sl[i - 1][j - 1] - sl[i - 1][j] - sl[i][j - 1] > 0:
            use[i - 1][j - 1] = True
            cnt += 1

abl = []
if cnt == 1:
    pass
elif cnt == 2:
    pass
elif cnt == 3:
    pass

# 回答
m = len(abl)
if m < 4 or m > 1000:  # エラー回避
    print(4)
    for a, b in ((0, 0), (0, 100000), (50000, 100000), (50000, 0)):
        print(a, b)
    exit()
# 正しい回答
print(m)
for a, b in abl:
    print(a, b)


"""
頂点数: 1000 以下
辺の長さの総和: 4 * 10**5 以下
辺はx軸,y軸に平行
0 <= x,y <= 10**5

点数 = max(0, サバ - イワシ + 1)
-> サバを多く, イワシを少なく
"""
