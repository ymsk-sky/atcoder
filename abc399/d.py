t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    al = list(map(int, input().split()))
    pos = {i: [] for i in range(n)}
    for i, a in enumerate(al):
        pos[a - 1].append(i)
    fin = [False] * n  # 既に隣同士
    for i in range(n):
        p, q = pos[i]
        if p + 1 == q:
            fin[i] = True
    res = set()
    # print(list(range(2*n)))
    # print(al)
    for i in range(n):
        if fin[i]:
            continue
        p, q = pos[i]
        tmp = set()
        # print(f"数字{i + 1}について")
        for u in (p - 1, p + 1):
            for v in (q - 1, q + 1):
                if 0 > u or u >= 2*n or 0 > v or v >= 2*n:
                    continue
                if u == v:
                    continue
                # print(f"\t{u} {v} を比較")
                if al[u] == al[v] and not fin[al[u] - 1]:
                    tmp.add(al[u])
        for j in tmp:
            a, b = sorted([i + 1, j])
            res.add((a, b))
    ans.append(len(res))
    # print(sorted([[r[0] + 1, r[1] + 1] for r in res]))
print(*ans, sep="\n")


"""
1
5
1 2 3 4 5 1 2 3 4 5
"""