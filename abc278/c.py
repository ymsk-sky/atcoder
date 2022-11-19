n, q = map(int, input().split())
d = dict()
ans = []
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        # aがbをフォロー
        if a in d:
            d[a].add(b)
        else:
            d[a] = set([b])
    elif t == 2:
        # aがbをフォロー解除
        if not a in d:
            continue
        if b in d[a]:
            d[a].remove(b)
    elif t == 3:
        # a,bが互いにフォローか確認
        f1, f2 = False, False
        if a in d:
            if b in d[a]:
                f1 = True
        if b in d:
            if a in d[b]:
                f2 = True
        if f1 and f2:
            ans.append("Yes")
        else:
            ans.append("No")
print(*ans, sep="\n")