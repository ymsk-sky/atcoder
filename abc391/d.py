INF = float("inf")

n, w = map(int, input().split())
xyl = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
tal = [list(map(int, input().split())) for _ in range(q)]

wd = {i: [] for i in range(1, w + 1)}
for i, (x, y) in enumerate(xyl):
    wd[x].append((y, i))
for k in wd.keys():
    wd[k] = sorted(wd[k])

del_num = min([len(l) for l in wd.values()])  # 行が消える回数
"""各列の消える時間は以下の中の最大チ。
- 前の列の消える時間 + 1
- 同じ列として消えるマスの最大y
"""
del_t = [INF] * n
ll = [[] for _ in range(del_num)]
for v in wd.values():
    for i in range(del_num):
        ll[i].append(v[i])
bef = 0
for l in ll:
    crt = max([v for v, _ in l])
    crt = max(crt, bef + 1)
    for _, i in l:
        del_t[i] = crt
    bef = crt

for t, a in tal:
    if del_t[a - 1] <= t:
        # 既に消えている
        ans = "No"
    else:
        ans = "Yes"
    print(ans)



"""
6 2
1 1
1 2
1 3
2 4
2 6
2 7
2
7 3
9 3
"""