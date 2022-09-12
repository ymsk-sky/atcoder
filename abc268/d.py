"""
1. 作成できる文字列をすべて作成しリストを作成
2. ソートしておく
3. tlをひとつずつ見ていき1.で作成したリストにあるかを確認
4. 3.の際, 二分探索で探すことでTLEを回避 O(M log N)
5. 見つかった場合は, その有無のリストを持っておきインデックスをFalseに変更していく
6. すべて探索した後, Trueのインデックスの文字列を出力
7. 無ければ-1を出力
"""

from bisect import bisect_left
from itertools import permutations

n, m = map(int, input().split())
sl = [input() for _ in range(n)]
tl = [input() for _ in range(m)]

if n == 1:
    if sl[0] in tl or len(sl[0]) < 3:
        print(-1)
    else:
        print(sl[0])
    exit()

def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f

f_min = n - 2
f_max = 16 - sum([len(s) for s in sl]) - 1

l = []
for per in permutations(sl):
    qers = []
    for f in range(f_min, f_max + 1): # f: 候補数
        k = 2 ** f
        for x in range(k):
            if popcount(x) == f_min:
                bs = []
                crt = "_"
                for y in range(f):
                    if x >> y & 1 == 1:
                        bs.append(crt)
                        crt = "_"
                    else:
                        crt += "_"
                bs.append(crt)
                bs.append("")
                qers.append(bs)

    for qer in qers:
        tmp = "".join(["".join([s, t]) for s, t in zip(per, qer)])
        l.append(tmp)

l.sort()

can = [True] * len(l)
for t in tl:
    ix = bisect_left(l, t)
    if ix < len(l):
        if l[ix] == t:
            can[ix] = False

for i, c in enumerate(can):
    if c:
        print(l[i])
        exit()
print(-1)
