H, W, N, h, w = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(H)]

all_cnt = {i: 0 for i in range(1, N + 1)}
for i in range(H):
    for j in range(W):
        a = al[i][j]
        all_cnt[a] += 1

hide = {i: 0 for i in range(1, N + 1)}
for i in range(h):
    for j in range(w):
        a = al[i][j]
        hide[a] += 1

# 左端の状態を記憶
tmp = {i: hide[i] for i in range(1, N + 1)}

ans = []

def check():
    cnt = 0
    for i in range(1, N + 1):
        if all_cnt[i] - hide[i] > 0:
            cnt += 1
    return cnt

# 右にずらす
def zura(i, j):
    for k in range(h):
        a = al[i + k][j]
        hide[a] -= 1
        a = al[i + k][j + w]
        hide[a] += 1

# 下にずらす
def zura2(i, j):
    for k in range(w):
        a = al[i][j + k]
        hide[a] -= 1
        a = al[i + h][j + k]
        hide[a] += 1

for i in range(H - h + 1):
    l = []
    l.append(check())
    for j in range(W - w):
        zura(i, j)
        l.append(check())
    if i != (H - h):
        for x in range(1, N + 1):
            hide[x] = tmp[x]
        zura2(i, j)
        for x in range(1, N + 1):
            tmp[x] = hide[x]
    ans.append(l)

for an in ans:
    print(*an)

"""
1<=H,W,N<=300
1<=h<=H
1<=w<=W
1<=a<=N
"""
