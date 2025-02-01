import sys
from functools import lru_cache

sys.setrecursionlimit(10**7)

n = int(input())
s = [int(c) for c in input()]

t = s
process = [t]
for _ in range(n):
    m = len(t)
    u = []
    for i in range(0, m, 3):
        u.append(int(t[i] + t[i + 1] + t[i + 2] >= 2))
    process.append(u)
    t = u

TO = 1 - process[n][0]  # TO(0 or 1)へ変更する

@lru_cache(maxsize=None)
def f(i: int, j: int) -> int:
    """processのi階層目のj番目を変更するには何回か
    len(process) = n + 1
    """
    if i == 0:
        return 1
    # 一つ前に影響する3つ
    a, b, c = process[i - 1][3*j], process[i - 1][3*j + 1], process[i - 1][3*j + 2]
    if a != TO and b != TO and c != TO:
        # 3つとも異なる: 3つの内小さい2つを変更
        res = [f(i - 1, 3*j), f(i - 1, 3*j + 1), f(i - 1, 3*j + 2)]
        res = sum(res) - max(res)
    else:
        # 2つ異なる: 2つの内小さい1つを変更
        if a == TO:
            res = min(f(i - 1, 3*j + 1), f(i - 1, 3*j + 2))
        elif b == TO:
            res = min(f(i - 1, 3*j), f(i - 1, 3*j + 2))
        elif c == TO:
            res = min(f(i - 1, 3*j), f(i - 1, 3*j + 1))
    return res

ans = f(n, 0)
print(ans)
