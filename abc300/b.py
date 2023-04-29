h, w = map(int, input().split())
al = [list(input()) for _ in range(h)]
bl = [list(input()) for _ in range(h)]

for s in range(h):
    # 縦方向シフトをs回
    for t in range(w):
        # 横方向シフトをt回
        l = al.copy()  # alをコピー
        # 縦方向シフト
        l = list(list(m) for m in zip(*l))
        for j in range(w):
            l[j] = l[j][s:] + l[j][:s]
        l = list(list(m) for m in zip(*l))
        # 横方向シフト
        for i in range(h):
            l[i] = l[i][t:] + l[i][:t]
        if l == bl:
            print("Yes")
            exit()
print("No")
