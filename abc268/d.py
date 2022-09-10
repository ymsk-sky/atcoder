"""
1. 作成できる文字列をすべて作成しリストを作成
2. ソートしておく
3. tlをひとつずつ見ていき1.で作成したリストにあるかを確認
4. 3.の際, 二分探索で探すことでTLEを回避 O(M log N)
5. 見つかった場合は, その有無のリストを持っておきインデックスをFalseに変更していく
6. すべて探索した後, Trueのインデックスの文字列を出力
7. 無ければ-1を出力
"""

from itertools import permutations
n, m = map(int, input().split())
sl = [input() for _ in range(n)]
tl = [input() for _ in range(m)]
l = set(["c_a_b"])
bn_min = n - 1
bn_max = 16 - sum([len(s) for s in sl])
for p in permutations(sl):
    for bn in range(bn_min - 1, bn_max):
        # bn個からn-2個選ぶ
        bs = ["__", "_", "_"]
        tmp_s = "".join([s + b for s, b in zip(sl, bs)])
        l.append(tmp_s)

ans = l - set(tl)
if len(ans) == 0:
    print(-1)
else:
    print(ans.pop())
