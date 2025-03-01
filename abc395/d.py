n, q = map(int, input().split())
opl = [list(map(lambda e: int(e) - 1, input().split())) for _ in range(q)]

pd = {i: i for i in range(n)}  # 鳩p: 巣i
nd = {i: i for i in range(n)}  # 巣i: 数x
num = {i: i for i in range(n)}  # 数x: 巣i

for op in opl:
    if op[0] == 0:
        # 鳩aを巣bへ移動
        a, b = op[1:]
        pd[a] = num[b]
    elif op[0] == 1:
        # 巣aと巣bの番号を入れ替え
        a, b = op[1:]
        nd[num[a]], nd[num[b]] = nd[num[b]], nd[num[a]]
        num[a], num[b] = num[b], num[a]
    else:
        # 鳩aのいる巣の番号
        a = op[1]
        print(nd[pd[a]] + 1)
