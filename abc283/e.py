h, w = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]
cnt = 0
for i in range(h):
    # left, right, upper, lowerと同じならbitが1になる(0b0000~0b1111)
    li = [0] * w
    for j in range(w):
        a = al[i][j]
        if j == 0:
            left = -1
        else:
            left = al[i][j - 1]
        if j == w - 1:
            right = -1
        else:
            right = al[i][j + 1]
        if a == left:
            li[j] += 1
        if a == right:
            li[j] += 2
        if i == 0:
            upper = -1
        else:
            upper = al[i - 1][j]
        if i == h - 1:
            lower = -1
        else:
            lower = al[i + 1][j]
        if a == upper:
            li[j] += 4
        if a == lower:
            li[j] += 8
    
    for j in range(w):
        v = li[j]
        if (v >> 0)&1 or (v >> 1)&1:
            # 左右どちらかと同じため無関係
            continue
        else:
            pass
print(cnt)

"""
2<=h,w<=1000
a=0,1

行の01を反転

0 0 1
1 0 1
1 0 0
"""
