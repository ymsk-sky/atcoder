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

"""

aa_a_a_a_a_a_a_a

3 4
a
b
c
a_b_c
a__b_c
a_b__c
b_a_c
b_c_a
c_a_b

cba

"""