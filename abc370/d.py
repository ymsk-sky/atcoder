from sortedcontainers import SortedSet

h, w, q = map(int, input().split())

H = [SortedSet([-1] + [j for j in range(w)] + [w]) for _ in range(h)]
W = [SortedSet([-1] + [i for i in range(h)] + [h]) for _ in range(w)]

for _ in range(q):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    if c in H[r]:
        # 壁あり
        H[r].discard(c)
        W[c].discard(r)
    else:
        # 壁なし
        # 縦方向
        i = W[c].bisect_left(r)  # (i-1)番目とi番目を消す
        _max = len(W[c]) - 1
        if i - 1 != 0:
            u = W[c][i - 1]
        if i != _max:
            v = W[c][i]
        if i - 1 != 0:
            W[c].discard(u)
            H[u].discard(c)
        if i != _max:
            W[c].discard(v)
            H[v].discard(c)
        # 横方向
        j = H[r].bisect_left(c)
        _max = len(H[r]) - 1
        if j - 1 != 0:
            u = H[r][j - 1]
        if j != _max:
            v = H[r][j]
        if j - 1 != 0:
            H[r].discard(u)
            W[u].discard(r)
        if j != _max:
            H[r].discard(v)
            W[v].discard(r)

ans = sum([len(ss) - 2 for ss in H])
print(ans)
