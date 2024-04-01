from collections import defaultdict

n, q = map(int, input().split())
xl = list(map(int, input().split()))

pos = defaultdict(list)  # 出現/消滅場所
l = [0] * (q + 1)
s = set()
for i in range(q):
    x = xl[i]
    if x in s:
        # sからxを削除
        s.discard(x)
        pos[x].append(i)
    else:
        # sにxを追加
        s.add(x)
        pos[x].append(i + 1)
    l[i + 1] = len(s)
# 累積和を求める
for i in range(q):
    l[i + 1] += l[i]
# 最後は消滅するので末尾を追加しておく
for k in pos.keys():
    pos[k].append(q)

al = [0] * n
for k in pos.keys():
    pl = pos[k]
    for i in range(0, len(pl) - 1, 2):
        p, q = pl[i + 1], pl[i]  # 出現場所, 消滅場所
        al[k - 1] += l[p] - l[q - 1]
print(*al)
